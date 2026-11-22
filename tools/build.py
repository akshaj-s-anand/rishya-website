#!/usr/bin/env python3
"""Generates the static Rishya Beauty Lounge site (v2: plum + champagne/peachy-gold, from Rishi's flyer)."""
import json, sys, urllib.parse
from pathlib import Path

OUT = Path(sys.argv[1])
PHONE_DISPLAY = "778-392-7296"
PHONE_E164 = "+17783927296"
WA = "https://wa.me/17783927296"
MAPS = "https://www.google.com/maps/search/?api=1&query=58+Saddlecreek+Crescent+NE+Calgary+AB+T3J+4R9"

def wa(text="Hi! I'd like to book an appointment."):
    return f"{WA}?text={urllib.parse.quote(text)}"

S = 'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
I = {
 "wa": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 21l1.65-4.6A8.5 8.5 0 1 1 7.6 19.4L3 21z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .9a4.6 4.6 0 0 1-2.8-2.8l.9-1-1-2L9 8.5z" fill="currentColor"/></svg>',
 "phone": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "pin": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "star": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="currentColor"/></svg>',
 "lotus": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M12 4c2.2 3 2.2 7 0 10.5C9.8 11 9.8 7 12 4Z"/><path d="M12 14.5C8.5 13.8 5.5 11.5 4.5 7.5c4 .3 6.6 3 7.5 7Z"/><path d="M12 14.5c3.5-.7 6.5-3 7.5-7-4 .3-6.6 3-7.5 7Z"/><path d="M3 16c3.2 0 6.4 1.2 9 3.8 2.6-2.6 5.8-3.8 9-3.8"/></svg>',
 "leaf": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M5 19C5 10 10 4 20 4c0 10-6 15-15 15Z"/><path d="M5 19 14 10"/></svg>',
 "person": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><circle cx="12" cy="6" r="2.5"/><path d="M5 20c1-4 3.5-6 7-6s6 2 7 6"/><path d="M4 12h16"/></svg>',
 "heart": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8Z"/></svg>',
 "user": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
 "sparkle": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3Z"/><path d="M19 16l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7.7-2Z"/></svg>',
 "receipt": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M5 2v20l2.5-1.5L10 22l2-1.5 2 1.5 2.5-1.5L19 22V2l-2.5 1.5L14 2l-2 1.5L10 2 7.5 3.5 5 2Z"/><path d="M9 8h6M9 12h6M9 16h4"/></svg>',
 "shield": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "maple": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M12 2l1.6 3.4L16 4.6l-.6 4 3-.8-1 2.6L21 12l-4 2.2.8 2.3-4.3-.7V21h-1v-5.2l-4.3.7.8-2.3L3 12l3.6-1.6-1-2.6 3 .8-.6-4 2.4.8L12 2Z"/></svg>',
 "arrow": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "menu": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>',
 "ig": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 "mail": f'<svg viewBox="0 0 24 24" {S} aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "sprig": '<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M20 110C45 80 70 55 108 18"/><path d="M40 86c-8-10-6-22 4-28 4 12 2 21-4 28Z"/><path d="M40 86c12 4 22 0 26-10-12-3-21 1-26 10Z"/><path d="M60 64c-7-11-4-22 6-27 3 12 0 21-6 27Z"/><path d="M60 64c12 3 22-2 25-12-12-2-20 3-25 12Z"/><path d="M82 40c-5-10-2-19 7-23 2 10-1 18-7 23Z"/><path d="M82 40c10 2 18-2 21-10-10-2-17 2-21 10Z"/></svg>',
}

# ---------- content (massage menu + prices from Rishi's Nov 2026 flyer) ----------
MASSAGE_MENU = [
 ("Relaxation Deep Tissue", [("60 min", "$110"), ("90 min", "$160")], "Firm, slow pressure for tight, overworked muscles. Includes hot stone and hot towel.", "deep-warm.jpg"),
 ("Therapeutic Massage", [("90 min", "$170")], "Our most complete session. Includes cupping, trigger points, hot stone and hot towel.", "m-cupping.jpg"),
 ("Hot Stone Swedish Massage", [("60 min", "$110"), ("90 min", "$160")], "Long, flowing Swedish strokes with smooth warmed stones to melt tension.", "m-hotstone.jpg"),
 ("Lymphatic Drainage", [("60 min", "$120"), ("90 min", "$170")], "A gentle, rhythmic light-touch technique that feels calm and soothing.", "m-lymph.jpg"),
 ("Prenatal & Postnatal Massage", [("60 min", "$125"), ("90 min", "$170")], "Side-lying comfort with supportive pillows. Add-on: stomach massage $30.", "m-prenatal.jpg"),
 ("TMJ Massage", [("60 min", "$120")], "Relieves jaw tension, reduces pain and improves mobility.", "m-tmj.jpg"),
 ("Head, Neck, Shoulder & Foot", [("60 min", "$100")], "Focused work where most of us hold stress, finished with a foot massage.", "m-neck.jpg"),
 ("Healing Energy Massage", [("60 min", "$100")], "A slow, grounding session to calm the mind and restore balance.", "m-healing.jpg"),
 ("Relaxation Facial Massage", [("60 min", "$100")], "Includes deep cleansing, exfoliation, steam, face pack and face massage.", "facial.jpg"),
 ("Buccal Facial Massage", [("60 min", "$120")], "A sculpting facial massage that works the cheek and jaw muscles for a lifted look.", "m-buccal.jpg"),
]
ENHANCE = [
 ("Aromatherapy", "+ $20", "m-aroma.jpg"),
 ("Hot Stone", "+ 10 min · + $20", "m-hotstone.jpg"),
 ("Foot Therapy", "+ 10 min · + $20", "m-foot.jpg"),
 ("Scalp Therapy", "+ 10 min · + $20", "m-neck.jpg"),
]
# Beauty: (kicker, title, text, image, tags)
BEAUTY = [
 ("Permanent makeup", "Brows", "Microblading, hybrid, powder and nano brows, shaped and colour-matched to your face. Free consultation.", "micro.jpg", ["Microblading", "Hybrid", "Powder", "Nano"]),
 ("Permanent makeup", "Lip Blushing", "Soft, semi-permanent colour that enhances your natural lip tone and shape.", "lip.jpg", ["Lip blush", "Colour correction"]),
 ("Permanent makeup", "Eyelash Enhancement", "A fine line along the lash line for fuller-looking lashes, every day.", "eyelash.jpg", ["Lash line", "Natural look"]),
 ("Esthetics", "Facials", "Deep cleansing, microdermabrasion and enzyme peel facials for fresh, glowing skin.", "facial.jpg", ["Deep cleansing", "Microdermabrasion", "Enzyme peel"]),
 ("Esthetics", "Lash Services", "Lash treatments for a soft, wide-awake look without daily mascara.", "m-lash.jpg", ["Lashes"]),
 ("Esthetics", "Waxing", "Full body waxing with soft and hard wax, chosen for each area.", "ai-wax.jpg", ["Full body", "Face", "Brows"]),
 ("Esthetics", "Manicure & Pedicure", "Shaping, cuticle care and polish for hands and feet.", "ai-mani-pedi.jpg", ["Manicure", "Pedicure"]),
]
BROWS = [
 ("Microblading", "Individual hair strokes created by hand for the most natural look.", "micro.jpg"),
 ("Hybrid Brows", "Hair strokes at the front with soft shading through the tail.", "ai-hybrid-brows.jpg"),
 ("Powder Brows", "A full, soft-shaded look, like brow powder that lasts.", "powder.jpg"),
 ("Nano Brows", "Ultra-fine hair strokes created with a digital machine.", "ai-nano-brows.jpg"),
]
REVIEWS = [
 ("I've gone here a couple of times and it's the best salon I've been to. She does amazing eyebrows and facials, and gives skin care tips which are very helpful!", "Kanwaljit S."),
 ("It was very calming and peaceful. Pedicure and manicure were really done well. Facial was very relaxing and the results were really good.", "Swas S."),
 ("She is very kind, nice and a professional person. I really love her treatment ❤️", "Kiran K."),
 ("I visited this place for the first time and like the environment, and the way of work is very good. Great work!", "Amandeep K."),
]
FAQ = [
 ("What should I wear or bring?", "Just yourself. You stay covered with linens throughout, and only the area being worked on is uncovered."),
 ("Can I add an enhancement?", "Yes. Aromatherapy, hot stone, foot therapy or scalp therapy can be added to any 60 or 90 minute massage."),
 ("Do you offer a consultation for permanent makeup?", "Yes, permanent makeup starts with a free consultation so we can plan shape and colour together."),
 ("How do I cancel or reschedule?", "Text us as early as you can and we will find you a new time."),
]
NAV = [("index.html", "Home"), ("massage.html", "Massage"), ("beauty.html", "Beauty & PMU"), ("index.html#about", "About"), ("contact.html", "Visit")]

SCHEMA = {
 "@context": "https://schema.org", "@type": "HealthAndBeautyBusiness",
 "name": "Rishya Beauty Lounge", "alternateName": "Looks Beauty Salon",
 "url": "https://looksbeautysalon.ca/", "telephone": PHONE_E164, "email": "looksbeautysalon.ca@gmail.com",
 "image": "https://looksbeautysalon.ca/assets/img/logo.png", "priceRange": "$$",
 "address": {"@type": "PostalAddress", "streetAddress": "58 Saddlecreek Crescent NE", "addressLocality": "Calgary", "addressRegion": "AB", "postalCode": "T3J 4R9", "addressCountry": "CA"},
 "openingHoursSpecification": [
   {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "18:00"},
   {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "11:00", "closes": "17:00"}],
 "areaServed": ["Calgary", "Airdrie", "Balzac", "Chestermere"],
 "sameAs": ["https://www.instagram.com/looksbeautysalon.ca/"],
}

CUR = ' aria-current="page"'
WA_LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16.04 3C9.02 3 3.3 8.7 3.3 15.72c0 2.24.59 4.43 1.7 6.36L3.2 28.8l6.9-1.8a12.7 12.7 0 0 0 5.93 1.5h.01c7.02 0 12.74-5.7 12.74-12.72C28.78 8.7 23.06 3 16.04 3Zm0 23.35h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-4.1 1.07 1.1-3.99-.25-.41a10.57 10.57 0 0 1-1.62-5.64c0-5.84 4.76-10.6 10.68-10.6 5.84 0 10.6 4.76 10.6 10.6 0 5.85-4.76 10.68-10.6 10.68Zm5.82-7.93c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.72.16-.21.32-.82 1.04-1 1.25-.19.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.9-1.78-2.22-.19-.32-.02-.49.14-.65.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.72-1.73-.98-2.37-.26-.62-.52-.54-.72-.55h-.61c-.21 0-.56.08-.85.4-.29.32-1.12 1.09-1.12 2.66 0 1.57 1.14 3.08 1.3 3.3.16.21 2.25 3.43 5.45 4.81.76.33 1.36.53 1.82.67.77.24 1.46.21 2.01.13.61-.09 1.89-.77 2.16-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37Z"/></svg>'

def page(title, desc, body, current, head_extra=""):
    links = "".join(f'<a href="{h}"{CUR if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">{head_extra}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#26082A">
<link rel="icon" href="assets/img/favicon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@400;500;600&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v=4">
<script>try{{if(sessionStorage.getItem("rishya-intro")||matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("no-intro");else document.documentElement.classList.add("intro-on")}}catch(e){{document.documentElement.classList.add("no-intro")}}</script>
<script type="application/ld+json">{json.dumps(SCHEMA)}</script>
</head>
<body>
<div class="intro" aria-hidden="true">
  <span class="intro-panel ip-top"></span><span class="intro-panel ip-bot"></span>
  <div class="intro-inner">
    <span class="intro-glow"></span>
    <img class="intro-logo" src="assets/img/logo.png" alt="" width="120" height="120">
    <p class="intro-word">{"".join(f'<span style="--i:{n}">{c}</span>' for n,c in enumerate("Rishya"))}</p>
    <span class="intro-line"></span>
    <p class="intro-tag">Beauty Lounge</p>
  </div>
</div>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="Rishya Beauty Lounge home">
      <img src="assets/img/logo.png" alt="Rishya Beauty Lounge logo" width="62" height="62">
      <span><b>Rishya</b><small>BEAUTY LOUNGE</small></span>
    </a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">{I['menu']}</button>
    <nav class="nav-links" id="nav-links" aria-label="Main">
      {links}
      <a class="btn btn-gold" href="{wa()}" target="_blank" rel="noopener">{I['wa']}Book now</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div style="display:grid;gap:12px">
      <a class="brand" href="index.html"><img src="assets/img/logo.png" alt="" width="58" height="58"><span><b>Rishya Beauty Lounge</b><small>MASSAGE · PERMANENT MAKEUP · ESTHETICS</small></span></a>
      <p class="mbw">Mind · Body · Balance · Wellness</p>
      <p class="fine">58 Saddlecreek Crescent NE, Calgary AB T3J 4R9 · By appointment only<br>© 2026 Rishya Beauty Lounge</p>
    </div>
    <nav class="footer-links" aria-label="Footer">{''.join(f'<a href="{h}">{t}</a>' for h,t in NAV)}</nav>
    <div class="contact">
      <a href="tel:{PHONE_E164}">{I['phone']}{PHONE_DISPLAY}</a>
      <a href="https://www.instagram.com/looksbeautysalon.ca/" target="_blank" rel="noopener">{I['ig']}@looksbeautysalon.ca</a>
      <a href="mailto:looksbeautysalon.ca@gmail.com">{I['mail']}looksbeautysalon.ca@gmail.com</a>
    </div>
  </div>
</footer>
<a class="wa-float" href="{wa("Hi! I'd like to book an appointment.")}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_LOGO}<span>Chat with us</span></a>
<script src="assets/kb.js?v=1" defer></script>
<script src="assets/chat.js?v=3" defer></script>
<script>
const b=document.querySelector('.menu-btn'),n=document.getElementById('nav-links');
b.addEventListener('click',()=>{{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);}});
(()=>{{const d=document.documentElement,x=document.querySelector('.intro');if(!x)return;
if(!d.classList.contains('intro-on')){{x.remove();return}}
try{{sessionStorage.setItem('rishya-intro','1')}}catch(e){{}}
const done=()=>{{d.classList.remove('intro-on');x.remove()}};
x.addEventListener('click',()=>{{x.classList.add('skip-now');setTimeout(done,650)}});
setTimeout(done,3600);}})();
</script>
</body>
</html>
"""

# ---------- blocks ----------
def orn(): return f'<div class="orn">{I["lotus"]}</div>'

def head(eyebrow, title, lead="", script="", center=True):
    return f"""<div class="head{' center' if center else ''}">
  {f'<span class="script">{script}</span>' if script else ''}<span class="eyebrow">{eyebrow}</span>
  <h2>{title}</h2>{orn()}
  {f'<p class="lead">{lead}</p>' if lead else ''}
</div>"""

def actions(label="Text to book", msg=None, dark=True):
    return f"""<div class="actions">
  <a class="btn btn-gold" href="{wa(msg) if msg else wa()}" target="_blank" rel="noopener">{I['wa']}{label}</a>
  <a class="btn {'btn-line' if dark else 'btn-line-dark'}" href="tel:{PHONE_E164}">{I['phone']}Call {PHONE_DISPLAY}</a>
</div>"""

def mcards(items):
    out = []
    for t, prices, d, img in items:
        pr = "".join(f"<div>{m}<b>{p}</b></div>" for m, p in prices)
        out.append(f"""<article class="mcard">
  <div class="ph"><img src="assets/img/{img}" alt="{t}" width="240" height="240"></div>
  <div><h3>{t}</h3><div class="prices">{pr}</div><p>{d}</p>
  <a class="bk" href="{wa(f"Hi! I'd like to book: {t}")}" target="_blank" rel="noopener">Book this →</a></div>
</article>""")
    return "".join(out)

def tiles(items, more_link=None):
    out = []
    for k, t, d, img, tags in items:
        out.append(f"""<article class="tile">
  <div class="im"><img src="assets/img/{img}" alt="{t}" width="800" height="600"></div>
  <div class="bd"><span class="kicker">{k}</span><h3>{t}</h3><p>{d}</p>
  <ul>{''.join(f'<li>{x}</li>' for x in tags)}</ul>
  <a class="link" href="{more_link or wa(f"Hi! I'd like to book: {t}")}"{'' if more_link else ' target="_blank" rel="noopener"'}>{'Explore' if more_link else 'Book'} {I['arrow']}</a></div>
</article>""")
    return "".join(out)

PILLS = f"""<div class="pillbar"><div class="wrap"><ul>
  <li>{I['person']}Professional</li><li>{I['heart']}Personalized</li><li>{I['leaf']}Results driven</li><li>{I['clock']}By appointment only</li>
</ul></div></div>"""

BENEFITS = f"""<section class="plum">
  <div class="wrap">
    {head("Why massage", "Take care of your mind, body &amp; soul", script="A healthier you")}
    <div class="benefits">
      <div class="benefit"><span class="coin">{I['lotus']}</span><span>Reduce stress</span></div>
      <div class="benefit"><span class="coin">{I['leaf']}</span><span>Relieve pain</span></div>
      <div class="benefit"><span class="coin">{I['person']}</span><span>Improve flexibility</span></div>
      <div class="benefit"><span class="coin">{I['heart']}</span><span>Restore balance</span></div>
    </div>
  </div>
</section>"""

ABOUT = f"""<section class="champ" id="about">
  <div class="wrap about">
    <figure class="portrait"><div class="ring"><img src="assets/img/therapist-portrait.jpg" alt="Your therapist at Rishya Beauty Lounge" width="900" height="900"></div><span class="sprig">{I['sprig']}</span></figure>
    <div class="copy">
      <span class="script">Meet your therapist</span>
      <span class="eyebrow">The hands behind Rishya</span>
      <h2>Care that feels personal</h2>
      <div class="orn" style="justify-content:flex-start">{I['lotus']}</div>
      <p class="lead">Rishya Beauty Lounge is a calm, private studio in NE Calgary where every appointment is one-on-one. Whether I am working on a deep tissue massage or a set of brows, I bring the same attention to detail to every client.</p>
      <p>From pain relief to a quiet hour to yourself, or brows and lips you can wake up with, I take time to listen first and tailor every treatment to you.</p>
      <ul class="creds">
        <li>{I['lotus']}Massage therapy &amp; stretch lab</li>
        <li>{I['sparkle']}Permanent makeup, brows, lashes &amp; esthetics</li>
        <li>{I['star']}30 Google reviews from local clients</li>
      </ul>
      <div class="actions" style="justify-content:flex-start">
        <a class="btn btn-plum" href="{wa()}" target="_blank" rel="noopener">{I['wa']}Book with me</a>
      </div>
    </div>
  </div>
</section>"""

REVIEWS_HTML = f"""<section class="cream" id="reviews">
  <div class="wrap">
    {head("30 Google reviews", "Kind words from clients", script="Loved by our clients")}
    <div class="reviews">
      {''.join(f'<figure class="review"><div class="stars">{I["star"]*5}</div><blockquote>“{q}”</blockquote><figcaption><cite>{n} · Google</cite></figcaption></figure>' for q,n in REVIEWS)}
    </div>
    <p style="margin-top:28px;text-align:center"><a class="btn btn-line-dark" href="https://www.google.com/maps/search/?api=1&query=Looks+Beauty+Salon+58+Saddlecreek+Crescent+NE+Calgary" target="_blank" rel="noopener">Read all reviews on Google</a></p>
  </div>
</section>"""

BAND = f"""<div class="band"><div class="wrap">
  <span class="script">Relax · Rejuvenate · Heal</span>
  <p>By appointment only · Text to book {PHONE_DISPLAY}</p>
  <a class="btn btn-plum" href="{wa()}" target="_blank" rel="noopener">{I['wa']}Book now</a>
</div></div>"""

VISIT = f"""<section class="plum" id="visit">
  <div class="wrap visit">
    <div style="display:grid;gap:18px">
      <span class="script">Invest in your wellbeing</span>
      <span class="eyebrow">Visit the lounge</span><h2>Find us in NE Calgary</h2>
      <ul>
        <li>{I['pin']}<span>58 Saddlecreek Crescent NE, Calgary, AB T3J 4R9</span></li>
        <li>{I['clock']}<span>Mon–Fri 9:00–18:00 · Sat 11:00–17:00 · Sun closed</span></li>
        <li>{I['phone']}<span><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a> · call, text or WhatsApp</span></li>
      </ul>
      <p style="color:var(--gold-100)">Serving Saddle Ridge and NE Calgary, plus Airdrie, Balzac and Chestermere.</p>
      {actions()}
    </div>
    <iframe class="map" title="Map to Rishya Beauty Lounge" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=58+Saddlecreek+Crescent+NE,+Calgary,+AB+T3J+4R9&output=embed"></iframe>
  </div>
</section>"""

FAQ_HTML = f"""<section class="faq">
  <div class="wrap" style="max-width:860px">
    {head("Good to know", "Questions before you book")}
    <div>{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)}</div>
  </div>
</section>"""

def page_hero(eyebrow, title, script, lead, bg, label, msg):
    return f"""<section class="plum page-hero">
  <div class="bg"><img src="assets/img/{bg}" alt=""></div>
  <div class="wrap">
    <span class="script">{script}</span>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>{orn()}
    <p class="lead">{lead}</p>
    {actions(label, msg)}
  </div>
</section>"""

# ---------- pages ----------
home = f"""<section class="hero">
  <div class="hero-grid">
    <div class="hero-left">
      <h1>Rishya Beauty Lounge<span class="gold-text">Massage · Permanent Makeup · Esthetics</span></h1>
      <p class="taglines">Relax<i>|</i>Rejuvenate<i>|</i>Heal</p>
      <span class="script">Take care of your mind, body &amp; soul</span>
      <p class="lead">A calm, private studio in NE Calgary for massage therapy, permanent makeup and beauty treatments.</p>
      {actions("Text to book")}
    </div>
    <div class="hero-right">
      <figure class="cutout"><span class="halo" aria-hidden="true"></span><img src="assets/img/rishi-blazer-cutout.webp?v=1" alt="Your therapist at Rishya Beauty Lounge" width="760" height="1108" fetchpriority="high"></figure>
    </div>
  </div>
</section>
{PILLS}
<section class="champ">
  <div class="wrap">
    {head("Two sides of Rishya", "Massage &amp; beauty, under one roof", "Book a therapeutic massage, refresh your skin, or wake up with perfect brows. Every appointment is private and one-on-one.", script="Welcome")}
    <div class="sides">
      <a class="side" href="massage.html"><img src="assets/img/m-hotstone.jpg" alt="Hot stone massage"><div class="txt"><span class="eyebrow" style="color:var(--gold-300)">Massage therapy</span><h3>Massage &amp; Stretch Lab</h3><p>Deep tissue, hot stone, lymphatic, prenatal, TMJ and more, from $100.</p><span class="go">View massage menu {I['arrow']}</span></div></a>
      <a class="side" href="beauty.html"><img src="assets/img/micro.jpg" alt="Microblading brows"><div class="txt"><span class="eyebrow" style="color:var(--gold-300)">Permanent makeup &amp; esthetics</span><h3>Beauty &amp; PMU Studio</h3><p>Brows, lip blushing, lashes, facials, waxing and nails.</p><span class="go">Explore beauty services {I['arrow']}</span></div></a>
    </div>
  </div>
</section>
{BENEFITS}
<section>
  <div class="wrap">
    {head("Services &amp; pricing", "Massage therapy", "A few client favourites. See the full menu for every treatment and enhancement.", script="Invest in your wellbeing")}
    <div class="menu">{mcards(MASSAGE_MENU[:6])}</div>
    <p style="margin-top:32px;text-align:center"><a class="btn btn-plum" href="massage.html">See the full massage menu</a></p>
  </div>
</section>
<section class="cream">
  <div class="wrap">
    {head("Permanent makeup &amp; esthetics", "Beauty services", "Soft, natural results with a free consultation for every permanent makeup service.", script="Wake up beautiful")}
    <div class="tiles">{tiles(BEAUTY[:6], "beauty.html")}</div>
  </div>
</section>
{ABOUT}
{REVIEWS_HTML}
{BAND}
{VISIT}"""

massage = f"""{page_hero("Massage / Stretch Lab · NE Calgary", "Massage Therapy", "Good energy, good health, better you", "Registered massage therapy in a quiet, private room. Every session is tailored to how you feel today.", "m-room.jpg", "Book a massage", "Hi! I'd like to book a massage.")}
{PILLS}
<section class="champ">
  <div class="wrap">
    {head("Services &amp; pricing", "Massage menu", "Not sure which one to choose? Text us how you feel and we will suggest the right fit.", script="Relax · Rejuvenate · Heal")}
    <div class="menu">{mcards(MASSAGE_MENU)}</div>
  </div>
</section>
<section class="cream">
  <div class="wrap">
    {head("Can be added to any 60 or 90 min massage", "Massage enhancements")}
    <div class="enh">{''.join(f'<article><div class="im"><img src="assets/img/{img}" alt="{t}"></div><h3>{t}</h3><p>{p}</p></article>' for t,p,img in ENHANCE)}</div>
  </div>
</section>
<section class="plum" style="padding:56px 0">
  <div class="wrap">
    <div class="trust3">
      <div>{I['receipt']}<span><b>Receipt available</b><small>For your records</small></span></div>
      <div>{I['shield']}<span><b>Direct billing</b><small>Ask us about your plan</small></span></div>
      <div>{I['maple']}<span><b>RMT</b><small>Registered Massage Therapist</small></span></div>
    </div>
  </div>
</section>
{BENEFITS}
{FAQ_HTML}
{BAND}
{VISIT}"""

beauty = f"""{page_hero("Permanent makeup &amp; esthetics · NE Calgary", "Beauty &amp; PMU Studio", "Wake up beautiful", "Brows, lips, lashes, facials, waxing and nails, with a free consultation for every permanent makeup service.", "micro.jpg", "Book a free consultation", "Hi! I'd like to book a free permanent makeup consultation.")}
{PILLS}
<section class="champ">
  <div class="wrap">
    {head("Permanent makeup", "Brows, made for your face", "Every brow is mapped to your features and colour-matched to your skin tone.", script="Signature brows")}
    <div class="tiles" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">{tiles([("Brows", t, d, img, []) for t, d, img in BROWS])}</div>
  </div>
</section>
<section class="cream">
  <div class="wrap">
    {head("Face, lashes, hands &amp; body", "All beauty services", script="Feel your best")}
    <div class="tiles">{tiles(BEAUTY[1:])}</div>
  </div>
</section>
{ABOUT}
{REVIEWS_HTML}
{BAND}
{VISIT}"""

contact = f"""{page_hero("Visit &amp; book", "Book your visit", "We can't wait to see you", "We are by appointment only. The quickest way to book is a text or WhatsApp message.", "m-room.jpg", "Text to book", None)}
{VISIT}
{FAQ_HTML}"""

PAGES = [
 ("index.html", "Rishya Beauty Lounge | Massage Therapy & Permanent Makeup in NE Calgary", "Massage therapy, permanent makeup, facials, brows, lashes and waxing in NE Calgary. By appointment only. Text to book.", home),
 ("massage.html", "Massage Therapy Menu & Prices | Rishya Beauty Lounge, NE Calgary", "Deep tissue, hot stone Swedish, lymphatic drainage, prenatal, TMJ, buccal facial and therapeutic massage from $100 in NE Calgary.", massage),
 ("beauty.html", "Permanent Makeup, Brows & Esthetics | Rishya Beauty Lounge, NE Calgary", "Microblading, hybrid, powder and nano brows, lip blushing, lashes, facials, waxing, manicure and pedicure in NE Calgary.", beauty),
 ("contact.html", "Visit & Book | Rishya Beauty Lounge, Saddlecreek Cres NE Calgary", "58 Saddlecreek Crescent NE, Calgary. Mon–Fri 9–6, Sat 11–5. By appointment only. Call or text 778-392-7296.", contact),
]
for f, t, d, b in PAGES:
    (OUT / f).write_text(page(t, d, b, f), encoding="utf-8")
# knowledge file for the chat widget (demo mode now, PHP/AI later)
def keys(n):
    n=n.lower(); k={n}
    for w in ["deep tissue","therapeutic","hot stone","lymphatic","prenatal","postnatal","tmj","jaw","head, neck","healing energy","relaxation facial","buccal","brow","microblad","lip","eyelash enhancement","facial","lash","wax","manicure","pedicure","nail"]:
        if w in n: k.add(w)
    return sorted(k)
KBD = {
 "phone": PHONE_DISPLAY, "maps": MAPS, "address": "58 Saddlecreek Crescent NE, Calgary, AB T3J 4R9",
 "hours": "Monday to Friday 9:00 to 18:00 and Saturday 11:00 to 17:00 (closed Sunday)",
 "massages": [{"name": t, "prices": [f"{m} {p}" for m, p in pr], "desc": d, "keys": keys(t) + (["jaw"] if "TMJ" in t else []) + (["pregnan"] if "Prenatal" in t else [])} for t, pr, d, _ in MASSAGE_MENU],
 "enhancements": [f"{t} {p}" for t, p, _ in ENHANCE],
 "beauty": [{"name": t, "desc": d, "note": "Free consultation." if k == "Permanent makeup" else "", "keys": keys(t)} for k, t, d, _, _ in BEAUTY] + [{"name": t, "desc": d, "note": "Free consultation.", "keys": keys(t)} for t, d, _ in BROWS],
}
for x in KBD["beauty"]:
    if x["name"] in ("Brows","Microblading","Hybrid Brows","Powder Brows","Nano Brows"): x["keys"] = sorted(set(x["keys"]+["brow"]))
(OUT / "assets" / "kb.json").write_text(json.dumps(KBD, indent=1), encoding="utf-8")
(OUT / "assets" / "kb.js").write_text("window.RISHYA_KB=" + json.dumps(KBD) + ";", encoding="utf-8")
# ---------- error pages ----------
ERRORS = {
 404: ("Page not found", "This page has drifted away", "The page you're looking for doesn't exist or has moved. Let's get you back somewhere relaxing."),
 403: ("Access denied", "This room is private", "You don't have permission to view this page. Everything you need is just a click away."),
 500: ("Something went wrong", "A little hiccup on our side", "Our website had a problem loading this page. Please try again in a moment, or message us and we'll help right away."),
 503: ("Taking a short break", "Back in a moment", "We're doing a little maintenance. Please check back shortly, or message us on WhatsApp in the meantime."),
}
def error_body(code):
    t, script, msg = ERRORS[code]
    return f"""<section class="plum err">
  <div class="wrap">
    <span class="script">{script}</span>
    <p class="err-code" aria-hidden="true">{str(code)[0]}<span>{I['lotus']}</span>{str(code)[2]}</p>
    <h1>{t}</h1>{orn()}
    <p class="lead">{msg}</p>
    <div class="actions"><a class="btn btn-gold" href="index.html">Back to home</a><a class="btn btn-line" href="{wa(f"Hi! I hit an error ({code}) on your website.")}" target="_blank" rel="noopener">{I['wa']}Message us</a></div>
    <nav class="err-links" aria-label="Popular pages"><a href="massage.html">Massage menu {I['arrow']}</a><a href="beauty.html">Beauty &amp; PMU {I['arrow']}</a><a href="contact.html">Visit &amp; book {I['arrow']}</a></nav>
  </div>
</section>"""
ERR_HEAD = '\n<meta name="robots" content="noindex">'
# GitHub Pages serves 404.html for any missing path; <base> keeps assets working in sub-folders
(OUT / "404.html").write_text(page("Page not found | Rishya Beauty Lounge", ERRORS[404][2], error_body(404), "", ERR_HEAD + '\n<base href="/rishya-website/">'), encoding="utf-8")
print("built", [p[0] for p in PAGES] + ["404.html"])

# ======================= PHP build (2nd arg = output dir) =======================
if len(sys.argv) > 2:
    import re, shutil
    PHP = Path(sys.argv[2]); PHP.mkdir(parents=True, exist_ok=True)
    for sub in ("includes", "api", "assets"):
        (PHP / sub).mkdir(exist_ok=True)
    # copy static assets from the HTML build
    shutil.copytree(OUT / "assets", PHP / "assets", dirs_exist_ok=True)
    shutil.copytree(Path(__file__).resolve().parent / "php_static", PHP, dirs_exist_ok=True)
    def to_php_links(s):
        return re.sub(r'href="(index|massage|beauty|contact)\.html', r'href="\1.php', s)
    T, D, C = "@@TITLE@@", "@@DESC@@", "@@CUR@@"
    shell = page(T, D, "@@BODY@@", C)
    head, foot = shell.split("@@BODY@@")
    head = to_php_links(head)
    # nav current state via PHP
    for h, t in NAV:
        hp = to_php_links(f'href="{h}"')
        head = head.replace(f'<a {hp}>{t}</a>', f'<a {hp}<?= nav_cur("{hp[6:-1]}") ?>>{t}</a>')
    head = head.replace(T, "<?= h($page_title) ?>").replace(D, "<?= h($page_desc) ?>")
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<?php if (!empty($page_base)): ?><meta name="robots" content="noindex">\n<base href="<?= h($page_base) ?>">\n<?php endif; ?>', 1)
    foot = to_php_links(foot).replace('<script src="assets/kb.js?v=1" defer></script>', '<script>window.RISHYA_CHAT_ENDPOINT = "api/ask.php";</script>')
    (PHP / "includes" / "header.php").write_text("<?php /* Shared header. Expects $page_title, $page_desc, $current. */ ?>\n" + head, encoding="utf-8")
    (PHP / "includes" / "footer.php").write_text(foot, encoding="utf-8")
    for f, t, d, b in PAGES:
        pf = f.replace(".html", ".php")
        (PHP / pf).write_text(
            "<?php\nrequire __DIR__ . '/includes/bootstrap.php';\n"
            f"$page_title = {json.dumps(t)};\n$page_desc = {json.dumps(d)};\n$current = '{pf}';\n"
            "require __DIR__ . '/includes/header.php';\n?>\n" + to_php_links(b) + "\n<?php require __DIR__ . '/includes/footer.php'; ?>\n", encoding="utf-8")
    # error pages (Apache: see .htaccess ErrorDocument; nginx: error_page)
    for code in ERRORS:
        (PHP / f"{code}.php").write_text(
            "<?php\nrequire __DIR__ . '/includes/bootstrap.php';\n"
            f"http_response_code({code});\n"
            + ("header('Retry-After: 3600');\n" if code == 503 else "")
            + f"$page_title = {json.dumps(ERRORS[code][0] + ' | Rishya Beauty Lounge')};\n$page_desc = {json.dumps(ERRORS[code][2])};\n$current = '';\n"
            "$page_base = rtrim(str_replace('\\\\', '/', dirname($_SERVER['SCRIPT_NAME'] ?? '/')), '/') . '/';\n"
            "require __DIR__ . '/includes/header.php';\n?>\n" + to_php_links(error_body(code)) + "\n<?php require __DIR__ . '/includes/footer.php'; ?>\n", encoding="utf-8")
    # knowledge text for the AI
    L = ["RISHYA BEAUTY LOUNGE - WEBSITE CONTENT (the only source of truth)", "",
         "Business: Rishya Beauty Lounge (also known as Looks Beauty Salon). Private studio in NE Calgary. Massage therapy / stretch lab, permanent makeup (PMU) and esthetics. By appointment only.",
         f"Address: {KBD['address']}. Serves Saddle Ridge, NE Calgary, Airdrie, Balzac and Chestermere.",
         f"Google Maps location / directions link: {MAPS}",
         "Website pages: Massage menu = massage.php, Beauty & PMU = beauty.php, Visit & book (map, hours, FAQ) = contact.php.",
         f"Hours: {KBD['hours']}.",
         f"Booking: WhatsApp or text {PHONE_DISPLAY} ({WA}), or call {PHONE_DISPLAY}. Instagram @looksbeautysalon.ca. Email looksbeautysalon.ca@gmail.com.",
         "", "MASSAGE MENU AND PRICES (CAD):"]
    L += [f"- {t}: {', '.join(f'{m} {p}' for m, p in pr)}. {d}" for t, pr, d, _ in MASSAGE_MENU]
    L += ["", "MASSAGE ENHANCEMENTS (add to any 60 or 90 min massage): " + "; ".join(KBD["enhancements"]) + ".",
          "", "PERMANENT MAKEUP AND ESTHETICS (prices on request; permanent makeup starts with a free consultation):"]
    L += [f"- {t} ({k}): {d} Options: {', '.join(tags)}." if tags else f"- {t} ({k}): {d}" for k, t, d, _, tags in BEAUTY]
    L += [f"- {t} (brow style): {d}" for t, d, _ in BROWS]
    L += ["", "FAQ:"] + [f"- Q: {q} A: {a}" for q, a in FAQ]
    L += ["", "Client reviews (Google, about 30 reviews): " + " | ".join(f'"{q}" ({n})' for q, n in REVIEWS)]
    L += ["", "NOT ON THE WEBSITE (do not guess): beauty/PMU prices, gift cards, insurance coverage details, parking, cancellation fees, therapist credentials beyond what is written above."]
    (PHP / "includes" / "knowledge.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("built php ->", PHP)
