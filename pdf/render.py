"""Renderiza salida/guia.html a salida/guia.pdf y revisa desbordes y textos superpuestos."""
import json, os, sys
from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMBRE = sys.argv[2] if len(sys.argv) > 2 else "guia"
HTML = "file://" + os.path.join(RAIZ, "salida", NOMBRE + ".html")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PREV = sys.argv[1] if len(sys.argv) > 1 else None

CHECK = r"""
() => {
  const res = [];
  const pgs = [...document.querySelectorAll('section.pg')];
  const inter = (a, b, t) => a.left < b.right - t && b.left < a.right - t && a.top < b.bottom - t && b.top < a.bottom - t;
  const bgs = pgs.map(p => p.style.background || '');
  for (let i = 1; i < pgs.length; i++) if (!bgs[i].includes('255, 255, 255') && !bgs[i-1].includes('255, 255, 255') && i > 1) res.push(`P${i}-P${i+1}: dos hojas de color seguidas`);
  pgs.forEach((pg, i) => {
    const P = pg.getBoundingClientRect();
    const n = i + 1;
    const ct = pg.querySelector('.ct');
    if (ct) {
      if (ct.scrollHeight > ct.clientHeight + 1) res.push(`P${n}: desborde vertical ${ct.scrollHeight - ct.clientHeight}px`);
      if (ct.scrollWidth > ct.clientWidth + 1) res.push(`P${n}: desborde horizontal ${ct.scrollWidth - ct.clientWidth}px`);
      const C = ct.getBoundingClientRect();
      ct.querySelectorAll('*').forEach(e => {
        const r = e.getBoundingClientRect();
        if (r.width && (r.right > C.right + 1 || r.bottom > C.bottom + 1)) res.push(`P${n}: ${e.tagName}.${e.className.baseVal ?? e.className} fuera de la caja (${Math.round(r.right - C.right)},${Math.round(r.bottom - C.bottom)})`);
      });
      // columnas: un elemento cortado entre columnas
      ct.querySelectorAll('.c2').forEach(c => { if (c.scrollWidth > c.clientWidth + 1) res.push(`P${n}: columnas desbordadas`); });
      // espacio libre al final
      const kids = [...ct.children]; if (kids.length) { const last = kids[kids.length-1].getBoundingClientRect(); res.push(`#LIBRE P${n}: ${Math.round(C.bottom - last.bottom)}px`); }
    }
    // textos absolutos que se pisan
    const abs = [...pg.querySelectorAll(':scope > .ab')].filter(e => e.textContent.trim());
    for (let a = 0; a < abs.length; a++) {
      const ra = abs[a].getBoundingClientRect();
      if (ra.right > P.right + 1 || ra.bottom > P.bottom + 1 || ra.left < P.left - 1) res.push(`P${n}: ${abs[a].textContent.slice(0,20)} sale de la hoja`);
      for (let b = a + 1; b < abs.length; b++) {
        const rb = abs[b].getBoundingClientRect();
        if (inter(ra, rb, 1)) res.push(`P${n}: se pisan «${abs[a].textContent.trim().slice(0,18)}» y «${abs[b].textContent.trim().slice(0,18)}»`);
      }
    }
    // textos de los gráficos
    pg.querySelectorAll('svg.ch').forEach((s, k) => {
      const S = s.getBoundingClientRect();
      const ts = [...s.querySelectorAll('text')].map(t => [t, t.getBoundingClientRect()]);
      ts.forEach(([t, r]) => { if (r.left < S.left - 1 || r.right > S.right + 1 || r.top < S.top - 1 || r.bottom > S.bottom + 1) res.push(`P${n} graf${k}: «${t.textContent}» sale del gráfico`); });
      for (let a = 0; a < ts.length; a++) for (let b = a + 1; b < ts.length; b++)
        if (inter(ts[a][1], ts[b][1], 0.5)) res.push(`P${n} graf${k}: se pisan «${ts[a][0].textContent}» y «${ts[b][0].textContent}»`);
    });
    // texto de celdas que no cabe (palabras largas)
    pg.querySelectorAll('td,th').forEach(td => { if (td.scrollWidth > td.clientWidth + 1) res.push(`P${n}: celda desbordada «${td.textContent.slice(0,25)}»`); });
  });
  return res;
}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 900, "height": 1200})
    pg.goto(HTML)
    pg.wait_for_load_state("networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    fuentes = pg.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
    print("fuentes:", sorted(set(fuentes)))
    res = pg.evaluate(CHECK)
    libres = [r for r in res if r.startswith("#LIBRE")]
    errores = [r for r in res if not r.startswith("#LIBRE")]
    print("\n".join(errores) if errores else "SIN PROBLEMAS")
    print(" ".join(l.replace("#LIBRE ", "") for l in libres))
    pg.pdf(path=os.path.join(RAIZ, "salida", NOMBRE + ".pdf"), prefer_css_page_size=True, print_background=True)
    if PREV:
        os.makedirs(PREV, exist_ok=True)
        pg.emulate_media(media="print")
        n = pg.evaluate("document.querySelectorAll('section.pg').length")
        for i in range(n):
            el = pg.locator("section.pg").nth(i)
            el.screenshot(path=os.path.join(PREV, f"p{i+1:02d}.png"))
    b.close()
