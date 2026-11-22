<?php /* Shared header. Expects $page_title, $page_desc, $current. */ ?>
<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<?php if (!empty($page_base)): ?><meta name="robots" content="noindex">
<base href="<?= h($page_base) ?>">
<?php endif; ?>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><?= h($page_title) ?></title>
<meta name="description" content="<?= h($page_desc) ?>">
<meta name="theme-color" content="#26082A">
<link rel="icon" href="assets/img/favicon.png">
<meta property="og:title" content="<?= h($page_title) ?>">
<meta property="og:description" content="<?= h($page_desc) ?>">
<meta property="og:image" content="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@400;500;600&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v=5">
<script>try{if(sessionStorage.getItem("rishya-intro")||matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("no-intro");else document.documentElement.classList.add("intro-on")}catch(e){document.documentElement.classList.add("no-intro")}</script>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "HealthAndBeautyBusiness", "name": "Rishya Beauty Lounge", "alternateName": "Looks Beauty Salon", "url": "https://looksbeautysalon.ca/", "telephone": "+17783927296", "email": "looksbeautysalon.ca@gmail.com", "image": "https://looksbeautysalon.ca/assets/img/logo.png", "priceRange": "$$", "address": {"@type": "PostalAddress", "streetAddress": "58 Saddlecreek Crescent NE", "addressLocality": "Calgary", "addressRegion": "AB", "postalCode": "T3J 4R9", "addressCountry": "CA"}, "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "11:00", "closes": "17:00"}], "areaServed": ["Calgary", "Airdrie", "Balzac", "Chestermere"], "sameAs": ["https://www.instagram.com/looksbeautysalon.ca/"]}</script>
</head>
<body>
<div class="intro" aria-hidden="true">
  <span class="intro-panel ip-top"></span><span class="intro-panel ip-bot"></span>
  <div class="intro-inner">
    <span class="intro-glow"></span>
    <img class="intro-logo" src="assets/img/logo.png" alt="" width="120" height="120">
    <p class="intro-word"><span style="--i:0">R</span><span style="--i:1">i</span><span style="--i:2">s</span><span style="--i:3">h</span><span style="--i:4">y</span><span style="--i:5">a</span></p>
    <span class="intro-line"></span>
    <p class="intro-tag">Beauty Lounge</p>
  </div>
</div>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.php" aria-label="Rishya Beauty Lounge home">
      <img src="assets/img/logo.png" alt="Rishya Beauty Lounge logo" width="62" height="62">
      <span><b>Rishya</b><small>BEAUTY LOUNGE</small></span>
    </a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg></button>
    <nav class="nav-links" id="nav-links" aria-label="Main">
      <a href="index.php"<?= nav_cur("index.php") ?>>Home</a><a href="massage.php"<?= nav_cur("massage.php") ?>>Massage</a><a href="beauty.php"<?= nav_cur("beauty.php") ?>>Beauty & PMU</a><a href="index.php#about"<?= nav_cur("index.php#about") ?>>About</a><a href="contact.php"<?= nav_cur("contact.php") ?>>Visit</a>
      <a class="btn btn-gold" href="https://wa.me/17783927296?text=Hi%21%20I%27d%20like%20to%20book%20an%20appointment." target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 21l1.65-4.6A8.5 8.5 0 1 1 7.6 19.4L3 21z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .9a4.6 4.6 0 0 1-2.8-2.8l.9-1-1-2L9 8.5z" fill="currentColor"/></svg>Book now</a>
    </nav>
  </div>
</header>
<main id="main">
