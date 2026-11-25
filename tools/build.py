#!/usr/bin/env python3
"""Builds the v3 "editorial spa" Rishya site (static HTML) into the repo root.
Run from anywhere:  python3 tools/build.py
Shared header/footer + page bodies live here so every page stays in sync."""
import json, os, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "3"  # cache-bust for css/js
PHONE = "778-392-7296"
TEL = "+17783927296"
WA = "https://wa.me/17783927296?text=Hi%21%20I%27d%20like%20to%20book%20an%20appointment."
ADDR = "58 Saddlecreek Crescent NE, Calgary, AB T3J 4R9"
MAPS = "https://www.google.com/maps/search/?api=1&query=58+Saddlecreek+Crescent+NE+Calgary+AB+T3J+4R9"
MAP_EMBED = "https://www.google.com/maps?q=58+Saddlecreek+Crescent+NE,+Calgary,+AB+T3J+4R9&output=embed"
IG = "https://www.instagram.com/looksbeautysalon.ca/"
EMAIL = "looksbeautysalon.ca@gmail.com"
REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Looks+Beauty+Salon+58+Saddlecreek+Crescent+NE+Calgary"

def wa(msg):
    from urllib.parse import quote
    return "https://wa.me/17783927296?text=" + quote(msg)

ICON = {
 "wa": '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16.04 3C9.02 3 3.3 8.7 3.3 15.72c0 2.24.59 4.43 1.7 6.36L3.2 28.8l6.9-1.8a12.7 12.7 0 0 0 5.93 1.5h.01c7.02 0 12.74-5.7 12.74-12.72C28.78 8.7 23.06 3 16.04 3Zm0 23.35h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-4.1 1.07 1.1-3.99-.25-.41a10.57 10.57 0 0 1-1.620-5.64c0-5.84 4.76-10.6 10.68-10.6 5.84 0 10.6 4.76 10.6 10.6 0 5.850-4.76 10.68-10.6 10.68Zm5.82-7.93c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.72.16-.21.32-.82 1.04-1 1.25-.19.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.9-1.78-2.22-.19-.32-.02-.49.14-.65.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.72-1.73-.98-2.37-.26-.62-.52-.54-.72-.55h-.61c-.21 0-.56.08-.85.4-.29.32-1.120 1.09-1.12 2.66 0 1.57 1.14 3.08 1.3 3.3.16.21 2.25 3.43 5.45 4.81.76.33 1.36.53 1.82.67.77.24 1.46.21 2.01.13.61-.09 1.89-.77 2.16-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37Z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h10"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
 "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>',
 "receipt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 2v20l3-2 3 2 2-2 2 2 3-2 3 2V2l-3 2-3-2-2 2-2-2-3 2Z"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "card": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg>',
}

# ---------- content ----------
MASSAGES = [
 ("Relaxation Deep Tissue", [("60 min","$110"),("90 min","$160")], "Firm, slow pressure for tight, overworked muscles. Includes hot stone and hot towel.", "v3-deep-tissue.jpg", "Client favourite"),
 ("Therapeutic Massage", [("90 min","$170")], "Our most complete session. Includes cupping, trigger points, hot stone and hot towel.", "m-cupping.jpg", "Most complete"),
 ("Hot Stone Swedish Massage", [("60 min","$110"),("90 min","$160")], "Long, flowing Swedish strokes with smooth warmed stones to melt tension.", "m-hotstone.jpg", ""),
 ("Lymphatic Drainage", [("60 min","$120"),("90 min","$170")], "A gentle, rhythmic light-touch technique that feels calm and soothing.", "m-lymph.jpg", ""),
 ("Prenatal & Postnatal Massage", [("60 min","$125"),("90 min","$170")], "Side-lying comfort with supportive pillows. Add-on: stomach massage $30.", "m-prenatal.jpg", ""),
 ("TMJ Massage", [("60 min","$120")], "Relieves jaw tension, reduces pain and improves mobility.", "m-tmj.jpg", ""),
 ("Head, Neck, Shoulder & Foot", [("60 min","$100")], "Focused work where most of us hold stress, finished with a foot massage.", "m-neck.jpg", ""),
 ("Healing Energy Massage", [("60 min","$100")], "A slow, grounding session to calm the mind and restore balance.", "m-healing.jpg", ""),
 ("Relaxation Facial Massage", [("60 min","$100")], "Includes deep cleansing, exfoliation, steam, face pack and face massage.", "v3-facial.jpg", ""),
 ("Buccal Facial Massage", [("60 min","$120")], "A sculpting facial massage that works the cheek and jaw muscles for a lifted look.", "m-buccal.jpg", ""),
]
ENH = [("Aromatherapy","+ $20","m-aroma.jpg"),("Hot Stone","+ 10 min · $20","m-hotstone.jpg"),("Foot Therapy","+ 10 min · $20","m-foot.jpg"),("Scalp Therapy","+ 10 min · $20","m-neck.jpg")]
BROWS = [
 ("Microblading","Individual hair strokes created by hand for the most natural look.","micro.jpg"),
 ("Hybrid Brows","Hair strokes at the front with soft shading through the tail.","ai-hybrid-brows.jpg"),
 ("Powder Brows","A full, soft-shaded look, like brow powder that lasts.","powder.jpg"),
 ("Nano Brows","Ultra-fine hair strokes created with a digital machine.","ai-nano-brows.jpg"),
]
BEAUTY = [
 ("Permanent makeup","Lip Blushing","Soft, semi-permanent colour that enhances your natural lip tone and shape.",["Lip blush","Colour correction"],"lip.jpg"),
 ("Permanent makeup","Eyelash Enhancement","A fine line along the lash line for fuller-looking lashes, every day.",["Lash line","Natural look"],"v3-lash-line.jpg"),
 ("Esthetics","Facials","Deep cleansing, microdermabrasion and enzyme peel facials for fresh, glowing skin.",["Deep cleansing","Microdermabrasion","Enzyme peel"],"v3-facial.jpg"),
 ("Esthetics","Lash Services","Lash treatments for a soft, wide-awake look without daily mascara.",["Lashes"],"m-lash.jpg"),
 ("Esthetics","Waxing","Full body waxing with soft and hard wax, chosen for each area.",["Full body","Face","Brows"],"ai-wax.jpg"),
 ("Esthetics","Manicure & Pedicure","Shaping, cuticle care and polish for hands and feet.",["Manicure","Pedicure"],"ai-mani-pedi.jpg"),
]
REVIEWS = [
 ("I've gone here a couple of times and it's the best salon I've been to. She does amazing eyebrows and facials, and gives skin care tips which are very helpful!","Kanwaljit S."),
 ("It was very calming and peaceful. Pedicure and manicure were really done well. Facial was very relaxing and the results were really good.","Swas S."),
 ("She is very kind, nice and a professional person. I really love her treatment ❤️","Kiran K."),
 ("I visited this place for the first time and like the environment, and the way of work is very good. Great work!","Amandeep K."),
]
FAQ = [
 ("What should I wear or bring?","Just yourself. You stay covered with linens throughout, and only the area being worked on is uncovered."),
 ("Can I add an enhancement?","Yes. Aromatherapy, hot stone, foot therapy or scalp therapy can be added to any 60 or 90 minute massage."),
 ("Do you offer a consultation for permanent makeup?","Yes, permanent makeup starts with a free consultation so we can plan shape and colour together."),
 ("Can I get a receipt for my insurance?","Yes, a receipt is available after every massage, and we can tell you about direct billing for your plan."),
 ("How do I cancel or reschedule?","Text us as early as you can and we will find you a new time."),
]
NAV = [("index.html","Home"),("massage.html","Massage"),("beauty.html","Beauty & PMU"),("index.html#therapist","About"),("contact.html","Visit")]
e = H.escape

LD = {"@context":"https://schema.org","@type":"HealthAndBeautyBusiness","name":"Rishya Beauty Lounge","alternateName":"Looks Beauty Salon","url":"https://looksbeautysalon.ca/","telephone":TEL,"email":EMAIL,"image":"https://looksbeautysalon.ca/assets/img/logo.png","priceRange":"$$","address":{"@type":"PostalAddress","streetAddress":"58 Saddlecreek Crescent NE","addressLocality":"Calgary","addressRegion":"AB","postalCode":"T3J 4R9","addressCountry":"CA"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"11:00","closes":"17:00"}],"areaServed":["Calgary","Airdrie","Balzac","Chestermere"],"sameAs":[IG]}

def head(title, desc, current, extra_head=""):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==current else ""}>{t}</a>' for h,t in NAV)
    dnav = "".join(f'<a href="{h}"><span>0{i+1}</span>{t}</a>' for i,(h,t) in enumerate(NAV))
    return f'''<!doctype html>
<html lang="en-CA" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#26082A">
<link rel="icon" href="assets/img/favicon.png">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="assets/img/v3-hero-room.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500;600&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={V}">
<link rel="stylesheet" href="assets/chat.css?v={V}">
<script>document.documentElement.classList.remove("no-js")</script>
<script type="application/ld+json">{json.dumps(LD)}</script>
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">By appointment only <span class="hide-sm">· Massage · Permanent makeup · Esthetics</span> · Text <a href="{WA}" target="_blank" rel="noopener">{PHONE}</a></div>
<header class="hdr">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Rishya Beauty Lounge home"><img src="assets/img/logo.png" alt="" width="50" height="50"><span><b>Rishya</b><small>Beauty Lounge</small></span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <a class="btn btn-plum" href="{WA}" target="_blank" rel="noopener">Book now</a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">{ICON["menu"]}</button>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer-top"><img src="assets/img/logo.png" alt="Rishya Beauty Lounge"><button class="drawer-x" aria-label="Close menu">&times;</button></div>
  <nav aria-label="Mobile">{dnav}</nav>
  <div class="actions"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Text to book</a><a class="btn btn-ghost" href="tel:{TEL}">{ICON["phone"]} Call</a></div>
</div>
<main id="main">
'''

def hero_bg(src, msrc=None, alt="", eager=True):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    if msrc:
        return f'<div class="hero-bg"><picture><source media="(max-width:700px)" srcset="assets/img/{msrc}"><img src="assets/img/{src}" alt="{e(alt)}" {load}></picture></div>'
    return f'<div class="hero-bg"><img src="assets/img/{src}" alt="{e(alt)}" {load}></div>'

def foot():
    return f'''</main>
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div style="display:grid;gap:18px;align-content:start">
        <a class="brand" href="index.html"><img src="assets/img/logo.png" alt="" width="50" height="50"><span><b>Rishya</b><small>Beauty Lounge</small></span></a>
        <p>A calm, private studio in NE Calgary for massage therapy, permanent makeup and esthetics. Every appointment is one-on-one.</p>
      </div>
      <div><h4>Explore</h4><ul><li><a href="massage.html">Massage menu</a></li><li><a href="beauty.html">Beauty &amp; PMU</a></li><li><a href="index.html#therapist">About</a></li><li><a href="contact.html">Visit &amp; book</a></li></ul></div>
      <div><h4>Hours</h4><ul><li>Mon–Fri · 9:00–18:00</li><li>Sat · 11:00–17:00</li><li>Sun · Closed</li><li>By appointment only</li></ul></div>
      <div><h4>Contact</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp us</a></li><li><a href="{IG}" target="_blank" rel="noopener">@looksbeautysalon.ca</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{MAPS}" target="_blank" rel="noopener">58 Saddlecreek Cres NE</a></li></ul></div>
    </div>
    <div class="big" aria-hidden="true">Relax · Rejuvenate · Heal</div>
    <div class="ftr-base"><span>© 2026 Rishya Beauty Lounge · Calgary, Alberta</span><span>Serving Saddle Ridge, NE Calgary, Airdrie, Balzac &amp; Chestermere</span></div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ICON["wa"]}<span>Chat with us</span></a>
<script src="assets/kb.js?v=1" defer></script>
<script src="assets/chat.js?v=3" defer></script>
<script src="assets/site.js?v={V}" defer></script>
</body>
</html>
'''

def kicker(t): return f'<span class="kicker">{t}</span>'

def mlist(items, numbered=True, dark=False, with_thumbs=True):
    out = []
    for i,(name,prices,desc,img,tag) in enumerate(items):
        pr = "".join(f'<span>{d}<b>{p}</b></span>' for d,p in prices)
        th = f'<img class="mthumb" src="assets/img/{img}" alt="" loading="lazy">' if with_thumbs else ""
        out.append(f'''<li class="mitem" data-img="assets/img/{img}" data-cap="{e(name)}"><span class="num">{i+1:02d}</span><div class="row"><h3>{e(name)}</h3><div class="prices">{pr}</div></div><p>{e(desc)}</p>{th}<a class="book" href="{wa("Hi! I'd like to book a " + name + ".")}" target="_blank" rel="noopener">Book this →</a></li>''')
    return '<ul class="mlist">' + "".join(out) + '</ul>'

def menu_block(items, first_img):
    imgs = []
    seen = []
    for it in items:
        if it[3] not in seen: seen.append(it[3])
    for j,src in enumerate(seen):
        imgs.append(f'<img src="assets/img/{src}" alt="" loading="lazy" class="{"on" if j==0 else ""}" data-src="assets/img/{src}">')
    return f'''<div class="menu-wrap">
  <div class="menu-visual" aria-hidden="true"><div class="frame">{"".join(imgs)}<span class="cap">{e(items[0][0])}</span></div></div>
  <div>{mlist(items)}</div>
</div>'''

def reviews_block():
    sl = "".join(f'<div class="rv-slide{" on" if i==0 else ""}"><blockquote>“{e(q)}”</blockquote><cite>{e(n)} · Google review</cite></div>' for i,(q,n) in enumerate(REVIEWS))
    dots = "".join(f'<button aria-label="Review {i+1}"{" class=\"on\"" if i==0 else ""}></button>' for i in range(len(REVIEWS)))
    return f'''<section class="reviews" aria-label="Client reviews">
  <div class="wrap"><div class="rv rv-in">
    <span class="script">Loved by our clients</span>
    <div class="rv-stars" aria-label="5 stars">★★★★★</div>
    <div class="rv-slides">{sl}</div>
    <div class="rv-dots">{dots}</div>
    <a class="link" href="{REVIEWS_URL}" target="_blank" rel="noopener">Read all 30 Google reviews {ICON["arrow"]}</a>
  </div></div>
</section>'''

def visit_block():
    return f'''<section id="visit">
  <div class="wrap">
    <div class="sec-head split rv-in"><div style="display:grid;gap:16px">{kicker("Visit the lounge")}<h2>Find us in <em>NE Calgary</em></h2></div><p class="lead">A quiet, private studio in Saddle Ridge, easy to reach from Airdrie, Balzac and Chestermere. Text us and we will send you directions.</p></div>
    <div class="visit-grid rv-in">
      <div class="visit-info">
        <div class="info-row"><span class="ic">{ICON["pin"]}</span><div><h4>Address</h4><a href="{MAPS}" target="_blank" rel="noopener">{ADDR}</a></div></div>
        <div class="info-row"><span class="ic">{ICON["clock"]}</span><div style="width:100%"><h4>Hours</h4><table class="hours"><tr><td>Monday – Friday</td><td>9:00 – 18:00</td></tr><tr><td>Saturday</td><td>11:00 – 17:00</td></tr><tr><td>Sunday</td><td>Closed</td></tr></table></div></div>
        <div class="info-row"><span class="ic">{ICON["phone"]}</span><div><h4>Call, text or WhatsApp</h4><a href="tel:{TEL}">{PHONE}</a></div></div>
        <div class="actions"><a class="btn btn-plum" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Text to book</a><a class="btn btn-line" href="tel:{TEL}">Call {PHONE}</a></div>
      </div>
      <div class="map"><iframe title="Map to Rishya Beauty Lounge" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </div>
  </div>
</section>'''

def cta_block(title='Your hour of <em>calm</em> is waiting', sub=f"By appointment only · Text to book {PHONE}", img="v3-ritual.jpg"):
    return f'''<section class="cta">
  {hero_bg(img, eager=False)}
  <div class="wrap rv-in">
    <span class="script">Relax · Rejuvenate · Heal</span>
    <h2>{title}</h2>
    <p>{sub}</p>
    <div class="actions" style="justify-content:center"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Text to book</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
</section>'''

def faq_block():
    items = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in FAQ)
    return f'''<section class="cream" style="background:var(--peach-100)">
  <div class="wrap">
    <div class="sec-head rv-in">{kicker("Good to know")}<h2>Questions <em>before you book</em></h2></div>
    <div class="faq rv-in">{items}</div>
  </div>
</section>'''

def marquee(words):
    s = "".join(f"<span>{w}</span>" for w in words)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{s}{s}</div></div>'

def bento():
    big = f'''<a class="tile t-big" href="beauty.html#brows"><img src="assets/img/micro.jpg" alt="Microblading brows" loading="lazy"><span class="arrow">{ICON["arrow"]}</span><div class="t-body"><small>Permanent makeup</small><h3>Brows, made for your face</h3><p>Microblading, hybrid, powder and nano brows, mapped to your features and colour-matched to your skin. Free consultation.</p><div class="tags"><span>Microblading</span><span>Hybrid</span><span>Powder</span><span>Nano</span></div></div></a>'''
    tiles = []
    for i,(cat,name,desc,tags,img) in enumerate(BEAUTY):
        cls = "tile t-wide" if i>=4 else "tile"
        tiles.append(f'<a class="{cls}" href="beauty.html"><img src="assets/img/{img}" alt="{e(name)}" loading="lazy"><span class="arrow">{ICON["arrow"]}</span><div class="t-body"><small>{cat}</small><h3>{e(name)}</h3></div></a>')
    # last wide tile = mani pedi + waxing
    return f'<div class="bento rv-in">{big}{"".join(tiles)}</div>'

def therapist_block():
    return f'''<section class="dark meet" id="therapist">
  <div class="wrap meet-grid">
    <div class="arch rv-in"><img src="assets/img/therapist-portrait.jpg" alt="Your therapist at Rishya Beauty Lounge" loading="lazy"><div class="badge"><b>30</b>Google reviews</div></div>
    <div class="meet-copy rv-in">
      {kicker("Meet your therapist")}
      <h2>The hands <em>behind Rishya</em></h2>
      <p class="quote">Whether it is a deep tissue massage or a set of brows, I take time to listen first and tailor every treatment to you.</p>
      <p class="lead">Rishya Beauty Lounge is a calm, private studio in NE Calgary where every appointment is one-on-one, from pain relief and a quiet hour to yourself to brows and lips you can wake up with.</p>
      <ul class="checks"><li>{ICON["check"]}Registered Massage Therapist, receipts for your insurance</li><li>{ICON["check"]}Permanent makeup, brows, lashes and esthetics</li><li>{ICON["check"]}One client at a time, in a private room</li></ul>
      <div class="actions"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Book with me</a></div>
    </div>
  </div>
</section>'''

def steps_block():
    return f'''<section>
  <div class="wrap">
    <div class="sec-head rv-in">{kicker("How booking works")}<h2>Three easy steps <em>to unwind</em></h2></div>
    <div class="steps rv-in">
      <div class="step">{ICON["chat"]}<h3>Text us</h3><p>Send a WhatsApp or text to {PHONE} with the treatment you have in mind, or just how you feel.</p></div>
      <div class="step">{ICON["cal"]}<h3>Pick a time</h3><p>We reply with open slots that suit you, weekdays 9 to 6 and Saturdays 11 to 5.</p></div>
      <div class="step">{ICON["leaf"]}<h3>Relax</h3><p>Arrive, breathe out and enjoy a one-on-one session in a calm, private room.</p></div>
    </div>
  </div>
</section>'''

# ---------- pages ----------
def page_index():
    b = head("Rishya Beauty Lounge | Massage Therapy & Permanent Makeup in NE Calgary",
             "Massage therapy, permanent makeup brows and lips, facials and waxing in a calm, private NE Calgary studio. By appointment only. Text to book 778-392-7296.", "index.html")
    b += f'''<section class="hero">
  {hero_bg("v3-hero-room.jpg","v3-hero-room-m.jpg","Candlelit private massage room at Rishya Beauty Lounge")}
  <div class="wrap">
    <div class="hero-copy">
      <span class="kicker rise">Massage · Permanent makeup · Esthetics</span>
      <h1 class="rise d1">Relax, <em>rejuvenate</em> &amp; heal</h1>
      <p class="lead rise d2">A calm, private studio in NE Calgary for therapeutic massage, permanent makeup and beauty treatments. One client at a time.</p>
      <div class="actions rise d3"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Text to book</a><a class="btn btn-ghost" href="massage.html">View massage menu</a></div>
    </div>
    <div class="hero-stats rise d4"><div><b>RMT</b><span>Registered therapist</span></div><div><b>10+</b><span>Massage treatments</span></div><div><b>5★</b><span>30 Google reviews</span></div></div>
  </div>
</section>
{marquee(["Deep tissue","Hot stone","Lymphatic drainage","Prenatal","TMJ","Cupping","Microblading","Lip blushing","Facials","Waxing"])}
<section>
  <div class="wrap intro-grid">
    <div class="collage rv-in"><img class="c-main" src="assets/img/m-room.jpg" alt="Treatment room with plum linens and candles" loading="lazy"><img class="c-small" src="assets/img/m-aroma.jpg" alt="Aromatherapy oils and warm candles" loading="lazy"><div class="seal"><div><b>1:1</b>Private<br>sessions</div></div></div>
    <div class="intro-copy rv-in">
      {kicker("Welcome to Rishya")}
      <h2>Massage &amp; beauty, <em>under one roof</em></h2>
      <p class="lead">Book a therapeutic massage, refresh your skin, or wake up with perfect brows. Every appointment is private, unhurried and tailored to how you feel today.</p>
      <div class="pillars"><div><b>Professional</b><span>Registered massage therapy with receipts</span></div><div><b>Personalized</b><span>We listen first, then tailor the session</span></div><div><b>Results driven</b><span>Pain relief and natural-looking beauty</span></div><div><b>Private</b><span>A quiet room, one client at a time</span></div></div>
      <div class="actions" style="margin-top:8px"><a class="link" href="#therapist">Meet your therapist {ICON["arrow"]}</a></div>
    </div>
  </div>
</section>
<section class="dark" id="massage">
  <div class="wrap">
    <div class="sec-head split rv-in"><div style="display:grid;gap:16px">{kicker("Massage & stretch lab")}<h2>The massage <em>menu</em></h2></div><p class="lead">Client favourites, from firm deep tissue to gentle lymphatic work. Add aromatherapy, hot stone, foot or scalp therapy to any session.</p></div>
    {menu_block(MASSAGES[:6], MASSAGES[0][3])}
    <div class="actions" style="margin-top:40px"><a class="btn btn-gold" href="massage.html">See the full menu &amp; enhancements</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head split rv-in"><div style="display:grid;gap:16px">{kicker("Beauty & PMU studio")}<h2>Wake up <em>beautiful</em></h2></div><p class="lead">Soft, natural results with a free consultation for every permanent makeup service. Plus facials, lashes, waxing and nails.</p></div>
    {bento()}
    <div class="actions" style="margin-top:36px"><a class="link" href="beauty.html">Explore all beauty services {ICON["arrow"]}</a></div>
  </div>
</section>
{therapist_block()}
{steps_block()}
{reviews_block()}
{cta_block()}
{visit_block()}
'''
    return b + foot()

def page_massage():
    b = head("Massage Therapy Menu & Prices | Rishya Beauty Lounge, NE Calgary",
             "Deep tissue, therapeutic, hot stone, lymphatic, prenatal, TMJ and facial massage in NE Calgary, from $100. RMT receipts. Text to book 778-392-7296.", "massage.html")
    cards = []
    for name,prices,desc,img,tag in MASSAGES:
        pr = "".join(f'<span>{d}<b>{p}</b></span>' for d,p in prices)
        t = f'<span class="tag">{tag}</span>' if tag else ""
        cards.append(f'<article class="card rv-in"><div class="img"><img src="assets/img/{img}" alt="{e(name)}" loading="lazy">{t}</div><div class="body"><h3>{e(name)}</h3><p>{e(desc)}</p></div><div class="foot"><div class="prices">{pr}</div><a class="link" href="{wa("Hi! I would like to book a " + name + ".")}" target="_blank" rel="noopener">Book {ICON["arrow"]}</a></div></article>')
    enh = "".join(f'<div><img src="assets/img/{img}" alt="" loading="lazy"><b>{n}</b><span>{p}</span></div>' for n,p,img in ENH)
    b += f'''<section class="phero">
  {hero_bg("m-hotstone.jpg", alt="Hot stone massage")}
  <div class="wrap"><div class="hero-copy" style="max-width:640px;display:grid">
    <span class="crumbs rise"><a href="index.html">Home</a> / Massage</span>
    <h1 class="rise d1">Massage <em>therapy</em></h1>
    <p class="lead rise d2">Registered massage therapy in a quiet, private room. Every session is tailored to how you feel today.</p>
    <div class="actions rise d3"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Book a massage</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div></div>
</section>
{marquee(["Good energy","Good health","Better you","Relax","Rejuvenate","Heal"])}
<section>
  <div class="wrap">
    <div class="sec-head split rv-in"><div style="display:grid;gap:16px">{kicker("Services & pricing")}<h2>Choose your <em>treatment</em></h2></div><p class="lead">Not sure which one to choose? Text us how you feel and we will suggest the right fit.</p></div>
    <div class="cards">{"".join(cards)}</div>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <div class="sec-head rv-in">{kicker("Add to any 60 or 90 min massage")}<h2>Massage <em>enhancements</em></h2></div>
    <div class="enh rv-in">{enh}</div>
    <div class="badges rv-in">
      <div>{ICON["receipt"]}<p><b>Receipts</b><span>Available for your insurance records</span></p></div>
      <div>{ICON["card"]}<p><b>Direct billing</b><span>Ask us about your plan</span></p></div>
      <div>{ICON["shield"]}<p><b>RMT</b><span>Registered Massage Therapist</span></p></div>
    </div>
  </div>
</section>
{steps_block()}
{faq_block()}
{cta_block(title='Book your <em>massage</em> today')}
{visit_block()}
'''
    return b + foot()

def page_beauty():
    b = head("Permanent Makeup, Brows & Esthetics | Rishya Beauty Lounge, NE Calgary",
             "Microblading, hybrid, powder and nano brows, lip blushing, lash enhancement, facials, waxing and nails in NE Calgary. Free PMU consultation.", "beauty.html")
    brows = "".join(f'<div class="brow rv-in"><div class="img"><img src="assets/img/{img}" alt="{e(n)}" loading="lazy"></div><h3>{e(n)}</h3><p>{e(d)}</p><a class="link" href="{wa("Hi! I would like a free consultation for " + n + ".")}" target="_blank" rel="noopener">Book consult {ICON["arrow"]}</a></div>' for n,d,img in BROWS)
    cards = []
    for cat,name,desc,tags,img in BEAUTY:
        tg = "".join(f"<span>{t}</span>" for t in tags)
        cards.append(f'<article class="card rv-in"><div class="img"><img src="assets/img/{img}" alt="{e(name)}" loading="lazy"><span class="tag">{cat}</span></div><div class="body"><h3>{e(name)}</h3><p>{e(desc)}</p></div><div class="foot"><span style="font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)">{" · ".join(tags)}</span><a class="link" href="{wa("Hi! I would like to book " + name + ".")}" target="_blank" rel="noopener">Book {ICON["arrow"]}</a></div></article>')
    b += f'''<section class="phero">
  {hero_bg("ai-hybrid-brows.jpg", alt="Soft hybrid brows")}
  <div class="wrap"><div class="hero-copy" style="max-width:640px;display:grid">
    <span class="crumbs rise"><a href="index.html">Home</a> / Beauty &amp; PMU</span>
    <h1 class="rise d1">Beauty &amp; <em>PMU studio</em></h1>
    <p class="lead rise d2">Brows, lips, lashes, facials, waxing and nails, with a free consultation for every permanent makeup service.</p>
    <div class="actions rise d3"><a class="btn btn-gold" href="{wa("Hi! I would like to book a free permanent makeup consultation.")}" target="_blank" rel="noopener">{ICON["wa"]} Free consultation</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div></div>
</section>
{marquee(["Microblading","Hybrid brows","Powder brows","Nano brows","Lip blushing","Lash line","Facials","Waxing"])}
<section id="brows">
  <div class="wrap">
    <div class="sec-head split rv-in"><div style="display:grid;gap:16px">{kicker("Signature brows")}<h2>Brows, made <em>for your face</em></h2></div><p class="lead">Every brow is mapped to your features and colour-matched to your skin tone. You approve the shape before we begin.</p></div>
    <div class="brows">{brows}</div>
  </div>
</section>
<section style="background:var(--peach-100)">
  <div class="wrap">
    <div class="sec-head rv-in">{kicker("Feel your best")}<h2>Face, lashes, <em>hands &amp; body</em></h2></div>
    <div class="cards">{"".join(cards)}</div>
  </div>
</section>
{therapist_block()}
{reviews_block()}
{cta_block(title='Wake up <em>beautiful</em>', sub="Free consultation for every permanent makeup service", img="ai-nano-brows.jpg")}
{visit_block()}
'''
    return b + foot()

def page_contact():
    b = head("Visit & Book | Rishya Beauty Lounge, Saddlecreek Cres NE Calgary",
             "Book massage, permanent makeup and esthetics at 58 Saddlecreek Crescent NE, Calgary. By appointment only. Text or WhatsApp 778-392-7296.", "contact.html")
    b += f'''<section class="phero" style="min-height:min(60vh,520px)">
  {hero_bg("m-room.jpg", alt="Private treatment room")}
  <div class="wrap"><div class="hero-copy" style="max-width:640px;display:grid">
    <span class="crumbs rise"><a href="index.html">Home</a> / Visit</span>
    <h1 class="rise d1">Book <em>your visit</em></h1>
    <p class="lead rise d2">We are by appointment only. The quickest way to book is a text or WhatsApp message.</p>
    <div class="actions rise d3"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]} Text to book</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div></div>
</section>
{visit_block()}
{steps_block()}
{faq_block()}
'''
    return b + foot()

def page_404():
    b = head("Page not found | Rishya Beauty Lounge", "The page you're looking for doesn't exist or has moved.", "")
    b = b.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">')
    b += f'''<section class="dark err">
  <div class="wrap">
    <div class="code gold-text">404</div>
    <h1 style="font-size:clamp(2rem,5vw,3.2rem)">This room is <em>empty</em></h1>
    <p class="lead" style="text-align:center">The page you're looking for doesn't exist or has moved. Let's get you back somewhere relaxing.</p>
    <div class="actions" style="justify-content:center"><a class="btn btn-gold" href="index.html">Back home</a><a class="btn btn-ghost" href="massage.html">Massage menu</a></div>
  </div>
</section>
'''
    return b + foot()

if __name__ == "__main__":
    pages = {"index.html":page_index(),"massage.html":page_massage(),"beauty.html":page_beauty(),"contact.html":page_contact(),"404.html":page_404()}
    for f,c in pages.items():
        with open(os.path.join(ROOT,f),"w",encoding="utf-8") as fh: fh.write(c)
        print("wrote",f,len(c))
