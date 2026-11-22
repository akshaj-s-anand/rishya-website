/* Rishya "Ask us" chat widget.
   Live mode: set window.RISHYA_CHAT_ENDPOINT = "api/ask.php" (POST {message, history} -> {reply}).
   Demo mode (no endpoint): answers simple questions from assets/kb.json. */
(function () {
  const ENDPOINT = window.RISHYA_CHAT_ENDPOINT || null;
  const WA = document.querySelector('.wa-float')?.href || '#';
  let KB = null, history = [], busy = false;
  /* Chat is remembered in this browser for 30 days after the last message. */
  const STORE = 'rishya-chat-v1', TTL = 30 * 24 * 3600 * 1000;
  const load = () => { try { const d = JSON.parse(localStorage.getItem(STORE) || 'null'); if (d && Date.now() - d.t < TTL) return d; localStorage.removeItem(STORE); } catch (e) {} return null; };
  const save = () => { try { localStorage.setItem(STORE, JSON.stringify({ t: Date.now(), msgs: [...log.children].filter(m => !m.classList.contains('typing')).map(m => ({ w: m.classList.contains('me') ? 'me' : 'bot', h: m.innerHTML })), history: history.slice(-16) })); } catch (e) {} };
  const sess = (k, v) => { try { return v === undefined ? sessionStorage.getItem(k) : sessionStorage.setItem(k, v); } catch (e) { return null; } };

  const el = (t, c, h) => { const e = document.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; };
  const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  const btn = el('button', 'chat-fab', '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12Z"/><path d="M8.5 10.5h7M8.5 13.5h4.5"/></svg><span>Ask us</span>');
  btn.setAttribute('aria-label', 'Ask us a question'); btn.setAttribute('aria-expanded', 'false');

  const panel = el('section', 'chat-panel');
  panel.setAttribute('aria-label', 'Ask Rishya'); panel.hidden = true;
  panel.innerHTML = `
    <header class="chat-head">
      <img src="assets/img/logo.png" alt="" width="40" height="40">
      <div><b>Ask Rishya</b><small>Usually answers instantly</small></div>
      <button class="chat-new" aria-label="Start a new chat" title="New chat"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg></button>
      <button class="chat-x" aria-label="Close chat">×</button>
    </header>
    <div class="chat-log" role="log" aria-live="polite"></div>
    <div class="chat-chips"></div>
    <form class="chat-form">
      <input type="text" maxlength="400" placeholder="Type your question…" aria-label="Your question" autocomplete="off">
      <button type="submit" aria-label="Send"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7Z"/></svg></button>
    </form>
    <p class="chat-note">Answers come from our website. For bookings, <a href="${WA}" target="_blank" rel="noopener">chat on WhatsApp</a>.</p>`;
  document.body.append(btn, panel);

  const log = panel.querySelector('.chat-log'), form = panel.querySelector('form'), input = form.querySelector('input'), chips = panel.querySelector('.chat-chips');
  const add = (who, html) => { const m = el('div', 'msg ' + who, html); log.append(m); log.scrollTop = log.scrollHeight; return m; };
  const CHIPS = ['Massage prices', 'Opening hours', 'Where are you?', 'Permanent makeup', 'Which massage for back pain?'];
  CHIPS.forEach(c => { const b = el('button', 'chip', c); b.type = 'button'; b.onclick = () => ask(c); chips.append(b); });
  const GREET = "Hi! 👋 I can answer questions about our massages, beauty services, prices and hours. What would you like to know?";
  const saved = load();
  if (saved && saved.msgs && saved.msgs.length) {
    saved.msgs.forEach(m => add(m.w, m.h)); history = saved.history || [];
    if (saved.msgs.some(m => m.w === 'me')) chips.hidden = true;
  }

  function open(v) {
    panel.hidden = !v; btn.setAttribute('aria-expanded', v); document.body.classList.toggle('chat-open', v); sess('rishya-chat-open', v ? '1' : '');
    if (v) { if (!log.children.length) { add('bot', GREET); save(); } log.scrollTop = log.scrollHeight; if (!matchMedia('(max-width:600px)').matches) setTimeout(() => input.focus(), 50); }
  }
  panel.querySelector('.chat-new').onclick = () => { log.innerHTML = ''; history = []; chips.hidden = false; try { localStorage.removeItem(STORE); } catch (e) {} add('bot', GREET); save(); input.focus(); };
  /* keep the chat open when moving between pages */
  if (sess('rishya-chat-open') === '1') open(true);
  btn.onclick = () => open(panel.hidden);
  panel.querySelector('.chat-x').onclick = () => open(false);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !panel.hidden) open(false); });
  form.onsubmit = e => { e.preventDefault(); const q = input.value.trim(); if (q) ask(q); };

  async function ask(q) {
    if (busy) return; busy = true; input.value = ''; chips.hidden = true;
    add('me', esc(q));
    const t = add('bot typing', '<i></i><i></i><i></i>');
    let reply;
    try {
      if (ENDPOINT) {
        const r = await fetch(ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ message: q, history: history.slice(-8) }) });
        if (!r.ok) throw new Error(r.status);
        reply = esc((await r.json()).reply || '').replace(/\n/g, '<br>');
      } else {
        await new Promise(r => setTimeout(r, 650));
        reply = await demo(q);
      }
    } catch (e) {
      reply = `Sorry, I couldn't answer that just now. Please <a href="${WA}" target="_blank" rel="noopener">message us on WhatsApp</a>.`;
    }
    t.className = 'msg bot'; t.innerHTML = reply; log.scrollTop = log.scrollHeight;
    history.push({ role: 'user', text: q }, { role: 'assistant', text: t.textContent });
    save();
    busy = false;
  }

  /* ---------- demo answers from kb.json ---------- */
  async function demo(q) {
    if (!KB) KB = window.RISHYA_KB || { massages: [], beauty: [], enhancements: [] };
    const s = q.toLowerCase(), has = (...w) => w.some(x => s.includes(x));
    const waLink = `<a href="${WA}" target="_blank" rel="noopener">book on WhatsApp</a>`;
    const m = (KB.massages || []).find(x => x.keys.some(k => s.includes(k)));
    if (m) return `<b>${m.name}</b>: ${m.prices.join(' · ')}.<br>${m.desc} Would you like to ${waLink}?`;
    const b = (KB.beauty || []).find(x => x.keys.some(k => s.includes(k)));
    if (b) return `<b>${b.name}</b>: ${b.desc} ${b.note || ''} Pricing is shared on request, just ${waLink}.`;
    if (has('hour', 'open', 'close', 'time', 'sunday', 'saturday', 'today')) return `We're open ${KB.hours}. Visits are by appointment only, so please ${waLink} first.`;
    if (has('where', 'address', 'location', 'locat', 'park', 'direction', 'find you')) return `We're at ${KB.address}, serving NE Calgary, Airdrie, Balzac and Chestermere. <a href="contact.html">See the map</a>.`;
    if (has('book', 'appointment', 'availability', 'available', 'slot')) return `The quickest way is to ${waLink}, or call ${KB.phone}. We'll reply with open times.`;
    if (has('back pain', 'pain', 'sore', 'tight', 'stiff', 'knot', 'neck', 'shoulder')) return `For tight or sore muscles, clients often choose <b>Relaxation Deep Tissue</b> (60 min $110 / 90 min $160) or our <b>Therapeutic Massage</b> (90 min $170, includes cupping, trigger points and hot stone). For neck and shoulders there's also <b>Head, Neck, Shoulder & Foot</b> (60 min $100). This isn't medical advice, so tell us how you feel when you ${waLink}.`;
    if (has('price', 'cost', 'how much', 'rate', 'menu', '$')) return 'Our massages start at $100:<br>' + KB.massages.map(x => `• ${x.name}: ${x.prices.join(' / ')}`).join('<br>') + `<br><a href="massage.html">See the full menu</a>.`;
    if (has('add-on', 'addon', 'enhanc', 'extra', 'aroma', 'scalp')) return 'Enhancements for any 60 or 90 min massage: ' + KB.enhancements.join(' · ') + '.';
    if (has('pmu', 'permanent', 'makeup', 'make up', 'beauty', 'esthetic')) return `We offer permanent makeup (microblading, hybrid, powder and nano brows, lip blushing, eyelash enhancement) plus facials, lashes, waxing, manicures and pedicures. Every permanent makeup service starts with a free consultation. <a href="beauty.html">See beauty services</a>.`;
    if (has('massage', 'massages', 'types')) return 'We offer: ' + KB.massages.map(x => x.name).join(', ') + `. <a href="massage.html">See prices</a>.`;
    if (has('cancel', 'reschedul')) return `Please text us as early as you can and we'll find you a new time.`;
    if (has('insurance', 'billing', 'receipt', 'covered', 'rmt')) return `Please ask us directly about receipts and billing for your plan, just ${waLink}.`;
    if (has('hi', 'hello', 'hey')) return 'Hello! Ask me about massage, permanent makeup, prices, hours or location.';
    return `I'm not sure about that one. Please <a href="${WA}" target="_blank" rel="noopener">message us on WhatsApp</a> and we'll answer personally.`;
  }
})();
