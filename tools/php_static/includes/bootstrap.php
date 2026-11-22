<?php
// Shared setup for every page and the API.
declare(strict_types=1);

$cfgLocal = __DIR__ . '/config.local.php';
if (is_file($cfgLocal)) {
    require $cfgLocal;               // defines GEMINI_API_KEY etc. (never committed)
}
defined('GEMINI_API_KEY')   || define('GEMINI_API_KEY', getenv('GEMINI_API_KEY') ?: '');
defined('GEMINI_MODEL')     || define('GEMINI_MODEL', getenv('GEMINI_MODEL') ?: 'gemini-flash-latest');
defined('ALLOWED_ORIGINS')  || define('ALLOWED_ORIGINS', ['https://looksbeautysalon.ca', 'https://www.looksbeautysalon.ca']);
defined('CHAT_RATE_LIMIT')  || define('CHAT_RATE_LIMIT', 20);   // messages per visitor per hour

function h(string $s): string { return htmlspecialchars($s, ENT_QUOTES, 'UTF-8'); }
function nav_cur(string $href): string {
    global $current;
    return (isset($current) && $current === $href) ? ' aria-current="page"' : '';
}
