<?php
// POST {"message": "...", "history": [{"role":"user|assistant","text":"..."}]}  ->  {"reply": "..."}
declare(strict_types=1);
require __DIR__ . '/../includes/bootstrap.php';
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function out(int $code, string $reply): never {
    http_response_code($code);
    echo json_encode(['reply' => $reply], JSON_UNESCAPED_UNICODE);
    exit;
}
$fallback = 'Sorry, I can\'t answer right now. Please message us on WhatsApp and we\'ll reply personally.';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') out(405, 'Method not allowed.');

// Only accept requests from our own site (or localhost while testing).
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
$host   = $_SERVER['HTTP_HOST'] ?? '';
if ($origin !== '') {
    $oh = parse_url($origin, PHP_URL_HOST) ?: '';
    $ok = in_array($origin, ALLOWED_ORIGINS, true) || $oh === 'localhost' || $oh === '127.0.0.1' || $oh === explode(':', $host)[0];
    if (!$ok) out(403, 'Forbidden.');
}

// Simple per-visitor rate limit (file based, no database needed).
$ip   = $_SERVER['REMOTE_ADDR'] ?? 'x';
$file = sys_get_temp_dir() . '/rishya_chat_' . md5($ip);
$now  = time();
$hits = array_filter(is_file($file) ? (json_decode((string)file_get_contents($file), true) ?: []) : [], fn($t) => $t > $now - 3600);
if (count($hits) >= CHAT_RATE_LIMIT) out(429, 'You\'ve asked a lot of questions! Please message us on WhatsApp and we\'ll help you personally.');
$hits[] = $now; @file_put_contents($file, json_encode(array_values($hits)), LOCK_EX);

$in  = json_decode((string)file_get_contents('php://input'), true) ?: [];
$msg = trim((string)($in['message'] ?? ''));
if ($msg === '' || mb_strlen($msg) > 400) out(400, 'Please type a shorter question.');
if (GEMINI_API_KEY === '') out(503, $fallback);

$knowledge = (string)file_get_contents(__DIR__ . '/../includes/knowledge.txt');
$system = <<<TXT
You are the friendly website assistant for Rishya Beauty Lounge in NE Calgary.
Answer ONLY using the website content below. Be warm, brief (2-4 sentences), and use CAD prices exactly as written.
If the answer is not in the content, say you're not sure and suggest messaging on WhatsApp (number in the content below).
Never invent prices, credentials, insurance coverage or availability. Do not give medical advice; for health conditions or pregnancy, suggest they discuss it with the therapist.
You cannot book appointments: for booking, point them to WhatsApp or the phone number.
Reply in the visitor's language. Plain text only, no markdown. When a link helps (Google Maps directions, WhatsApp), paste the full URL exactly as written in the website content; never invent links.

=== WEBSITE CONTENT ===
{$knowledge}
TXT;

$contents = [];
foreach (array_slice(is_array($in['history'] ?? null) ? $in['history'] : [], -8) as $t) {
    $text = mb_substr(trim((string)($t['text'] ?? '')), 0, 800);
    if ($text === '') continue;
    $contents[] = ['role' => ($t['role'] ?? '') === 'assistant' ? 'model' : 'user', 'parts' => [['text' => $text]]];
}
$contents[] = ['role' => 'user', 'parts' => [['text' => $msg]]];

$payload = [
    'system_instruction' => ['parts' => [['text' => $system]]],
    'contents' => $contents,
    'generationConfig' => ['temperature' => 0.3, 'maxOutputTokens' => 1024],
];
// Try the configured model first; if Google is busy (429/5xx/timeout), fall back to lighter models.
$models = array_values(array_unique(array_filter([GEMINI_MODEL, 'gemini-flash-lite-latest', 'gemini-2.5-flash'])));
$reply = '';
foreach ($models as $model) {
    $url = 'https://generativelanguage.googleapis.com/v1beta/models/' . rawurlencode($model) . ':generateContent';
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_TIMEOUT => 12,
        CURLOPT_HTTPHEADER => ['Content-Type: application/json', 'x-goog-api-key: ' . GEMINI_API_KEY],
        CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_UNICODE),
    ]);
    $res  = curl_exec($ch);
    $code = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $cerr = curl_error($ch);
    curl_close($ch);

    $data = json_decode((string)$res, true);
    foreach ($data['candidates'][0]['content']['parts'] ?? [] as $p) {
        if (empty($p['thought'])) $reply .= $p['text'] ?? '';
    }
    if ($code === 200 && trim($reply) !== '') break;
    error_log('Rishya chat: ' . $model . ' HTTP ' . $code . ' ' . $cerr . ' ' . substr((string)$res, 0, 300));
    $reply = '';
    if ($code !== 0 && $code !== 429 && $code < 500) break; // bad key/request: other models won't help
}
if (trim($reply) === '') out(502, $fallback);
out(200, trim($reply));
