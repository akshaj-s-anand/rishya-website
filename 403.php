<?php
require __DIR__ . '/includes/bootstrap.php';
http_response_code(403);
$page_title = "Access denied | Rishya Beauty Lounge";
$page_desc = "You don't have permission to view this page. Everything you need is just a click away.";
$current = '';
$page_base = rtrim(str_replace('\\', '/', dirname($_SERVER['SCRIPT_NAME'] ?? '/')), '/') . '/';
require __DIR__ . '/includes/header.php';
?>
<section class="plum err">
  <div class="wrap">
    <span class="script">This room is private</span>
    <p class="err-code" aria-hidden="true">4<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4c2.2 3 2.2 7 0 10.5C9.8 11 9.8 7 12 4Z"/><path d="M12 14.5C8.5 13.8 5.5 11.5 4.5 7.5c4 .3 6.6 3 7.5 7Z"/><path d="M12 14.5c3.5-.7 6.5-3 7.5-7-4 .3-6.6 3-7.5 7Z"/><path d="M3 16c3.2 0 6.4 1.2 9 3.8 2.6-2.6 5.8-3.8 9-3.8"/></svg></span>3</p>
    <h1>Access denied</h1><div class="orn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4c2.2 3 2.2 7 0 10.5C9.8 11 9.8 7 12 4Z"/><path d="M12 14.5C8.5 13.8 5.5 11.5 4.5 7.5c4 .3 6.6 3 7.5 7Z"/><path d="M12 14.5c3.5-.7 6.5-3 7.5-7-4 .3-6.6 3-7.5 7Z"/><path d="M3 16c3.2 0 6.4 1.2 9 3.8 2.6-2.6 5.8-3.8 9-3.8"/></svg></div>
    <p class="lead">You don't have permission to view this page. Everything you need is just a click away.</p>
    <div class="actions"><a class="btn btn-gold" href="index.php">Back to home</a><a class="btn btn-line" href="https://wa.me/17783927296?text=Hi%21%20I%20hit%20an%20error%20%28403%29%20on%20your%20website." target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 21l1.65-4.6A8.5 8.5 0 1 1 7.6 19.4L3 21z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .9a4.6 4.6 0 0 1-2.8-2.8l.9-1-1-2L9 8.5z" fill="currentColor"/></svg>Message us</a></div>
    <nav class="err-links" aria-label="Popular pages"><a href="massage.php">Massage menu <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a><a href="beauty.php">Beauty &amp; PMU <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a><a href="contact.php">Visit &amp; book <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></nav>
  </div>
</section>
<?php require __DIR__ . '/includes/footer.php'; ?>
