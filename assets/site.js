/* Rishya v3: header state, mobile drawer, scroll reveal, massage menu preview, review slider. */
(() => {
  const hdr = document.querySelector('.hdr');
  const onScroll = () => hdr && hdr.classList.toggle('scrolled', scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  const drawer = document.getElementById('drawer'), btn = document.querySelector('.menu-btn');
  const setDrawer = open => {
    drawer.classList.toggle('open', open); drawer.setAttribute('aria-hidden', !open);
    btn.setAttribute('aria-expanded', open); document.body.classList.toggle('locked', open);
  };
  btn && btn.addEventListener('click', () => setDrawer(true));
  drawer && drawer.querySelector('.drawer-x').addEventListener('click', () => setDrawer(false));
  drawer && drawer.querySelectorAll('nav a').forEach(a => a.addEventListener('click', () => setDrawer(false)));
  addEventListener('keydown', e => { if (e.key === 'Escape' && drawer.classList.contains('open')) setDrawer(false); });

  const els = document.querySelectorAll('.rv-in');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add('seen'); io.unobserve(x.target); } }), { rootMargin: '0px 0px -8% 0px' });
    els.forEach(el => io.observe(el));
  } else els.forEach(el => el.classList.add('seen'));

  document.querySelectorAll('.menu-wrap').forEach(w => {
    const imgs = w.querySelectorAll('.menu-visual img'), cap = w.querySelector('.menu-visual .cap');
    w.querySelectorAll('.mitem').forEach(it => it.addEventListener('mouseenter', () => {
      imgs.forEach(i => i.classList.toggle('on', i.dataset.src === it.dataset.img));
      if (cap) cap.textContent = it.dataset.cap;
    }));
  });

  document.querySelectorAll('.rv').forEach(rv => {
    const s = rv.querySelectorAll('.rv-slide'), d = rv.querySelectorAll('.rv-dots button');
    let i = 0, t;
    const go = n => { i = (n + s.length) % s.length; s.forEach((x, k) => x.classList.toggle('on', k === i)); d.forEach((x, k) => x.classList.toggle('on', k === i)); };
    const auto = () => { clearInterval(t); if (!matchMedia('(prefers-reduced-motion: reduce)').matches) t = setInterval(() => go(i + 1), 6500); };
    d.forEach((b, k) => b.addEventListener('click', () => { go(k); auto(); }));
    auto();
  });
})();
