<?php
// Copy this file to config.local.php (same folder) and fill in your key.
// config.local.php is git-ignored, so the key never goes to GitHub.
define('GEMINI_API_KEY', 'PASTE-YOUR-KEY-HERE');
define('GEMINI_MODEL', 'gemini-flash-latest');   // any Gemini model name from Google AI Studio
// Add your live domain(s); localhost is always allowed for testing.
define('ALLOWED_ORIGINS', ['https://looksbeautysalon.ca', 'https://www.looksbeautysalon.ca']);
define('CHAT_RATE_LIMIT', 20);
