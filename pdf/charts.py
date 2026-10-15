"""Gráficos en SVG para hoja de papel (1 unidad = 1 pt). Serie destacada en lima con borde negro; el resto negro o gris."""
import math
from lib import n, LIMA, NEGRO, GRIS, GRIS2, PAPEL

TX = "#000"
MU = "#4a4f57"
AX = "#d5d8dc"
OSC = "#1c2028"


def f(v):
    return str(v).replace(".", ",")


def T(x, y, s, a="middle", cls="", sz=7.5, w=400, fill=None):
    fl = fill or (MU if cls == "mu" else TX)
    return f'<text x="{n(x)}" y="{n(y)}" text-anchor="{a}" font-size="{sz}" font-weight="{w}" fill="{fl}">{s}</text>'


def svg(w, h, body):
    return f'<svg class="ch" width="{n(w)}pt" height="{n(h)}pt" viewBox="0 0 {n(w)} {n(h)}" role="img">{body}</svg>'


def bar(x, y, w, h, hi=False, hatch=False, gris=False):
    if hatch:
        return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="3" fill="url(#rayado)" stroke="#000" stroke-width=".6"/>'
    if hi:
        return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="3" fill="{LIMA}" stroke="#000" stroke-width=".6"/>'
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="3" fill="{GRIS2 if gris else NEGRO}"/>'


DEFS = ('<svg width="0" height="0" style="position:absolute"><defs>'
        '<pattern id="rayado" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        f'<rect width="5" height="5" fill="#fff"/><rect width="2.2" height="5" fill="{LIMA}"/></pattern></defs></svg>')


def vbars(items, vmax, w=226, h=150, unit="%", ticks=(0, 0.5, 1), dec=None):
    PL, PR, PT, PB = 30, 6, 16, 30
    iw, ih = w - PL - PR, h - PT - PB
    gap = iw / len(items)
    bw = gap * 0.56
    s = ""
    for t in ticks:
        y = PT + ih - ih * t
        s += f'<line x1="{PL}" x2="{n(w-PR)}" y1="{n(y)}" y2="{n(y)}" stroke="{AX}" stroke-width=".6"/>' + T(PL - 4, y + 2.5, f(round(vmax * t, 2)), "end", "mu", 6.5)
    for i, it in enumerate(items):
        x = PL + gap * i + (gap - bw) / 2
        bh = ih * it["v"] / vmax
        y = PT + ih - bh
        s += bar(x, y, bw, bh, it.get("hi"), it.get("hatch"), it.get("gris"))
        top = y
        if it.get("err"):
            e = ih * it["err"] / vmax
            cx = x + bw / 2
            s += f'<path d="M{n(cx)} {n(y-e)}V{n(y+e)}M{n(cx-4)} {n(y-e)}H{n(cx+4)}M{n(cx-4)} {n(y+e)}H{n(cx+4)}" stroke="#000" stroke-width=".8" fill="none"/>'
            top = y - e
        lab = it.get("t", f(it["v"]) + unit)
        s += T(x + bw / 2, top - 4, lab, "middle", "", 7.5, 700)
        s += T(x + bw / 2, h - PB + 11, it["l"], "middle", "mu", 6.8)
        if it.get("l2"):
            s += T(x + bw / 2, h - PB + 20, it["l2"], "middle", "mu", 6.8)
    return svg(w, h, s)


def hbars(items, vmax, w=226, lw=118, rh=17):
    h = len(items) * rh + 6
    s = ""
    for i, it in enumerate(items):
        y = 4 + i * rh
        bw = (w - lw - 22) * it["v"] / vmax
        s += T(lw - 5, y + 9, it["l"], "end", "", 6.8)
        s += bar(lw, y + 1, bw, 10, it.get("hi"))
        s += T(lw + bw + 4, y + 9, f(it["v"]), "start", "", 7, 700)
    return svg(w, h, s)


def linea(pts, xr, yr, xl, yl, w=226, h=160, yticks=4, labels=True):
    PL, PR, PT, PB = 30, 10, 18, 32
    iw, ih = w - PL - PR, h - PT - PB
    X = lambda v: PL + iw * (v - xr[0]) / (xr[1] - xr[0])
    Y = lambda v: PT + ih - ih * (v - yr[0]) / (yr[1] - yr[0])
    s = ""
    for k in range(yticks + 1):
        v = yr[0] + (yr[1] - yr[0]) * k / yticks
        s += f'<line x1="{PL}" x2="{n(w-PR)}" y1="{n(Y(v))}" y2="{n(Y(v))}" stroke="{AX}" stroke-width=".6"/>' + T(PL - 4, Y(v) + 2.5, f(round(v)), "end", "mu", 6.5)
    s += f'<path d="{"".join(("L" if i else "M") + n(X(p[0])) + " " + n(Y(p[1])) for i, p in enumerate(pts))}" stroke="#000" stroke-width="1.4" fill="none"/>'
    for p in pts:
        s += f'<circle cx="{n(X(p[0]))}" cy="{n(Y(p[1]))}" r="3.2" fill="{LIMA}" stroke="#000" stroke-width=".8"/>'
        if labels:
            s += T(X(p[0]), Y(p[1]) - 6, f(p[1]), "middle", "", 6.8, 700)
        s += T(X(p[0]), h - PB + 10, p[2] if len(p) > 2 else f(p[0]), "middle", "mu", 6.5)
    s += T(PL + iw / 2, h - 6, xl, "middle", "mu", 6.5) + T(2, 8, yl, "start", "mu", 6.5)
    return svg(w, h, s)


def agrupadas(grupos, series, vmax, w=226, h=150):
    """grupos: [(etiqueta, [v1, v2])]; series: [(nombre, estilo)] estilo 'n' negro, 'l' lima."""
    PL, PR, PT, PB = 30, 6, 16, 26
    iw, ih = w - PL - PR, h - PT - PB
    gw = iw / len(grupos)
    s = ""
    for t in (0, 0.5, 1):
        y = PT + ih - ih * t
        s += f'<line x1="{PL}" x2="{n(w-PR)}" y1="{n(y)}" y2="{n(y)}" stroke="{AX}" stroke-width=".6"/>' + T(PL - 4, y + 2.5, f(round(vmax * t)), "end", "mu", 6.5)
    k = len(series)
    bw = gw * 0.7 / k
    for i, (lab, vals) in enumerate(grupos):
        for j, v in enumerate(vals):
            x = PL + gw * i + gw * 0.15 + j * bw
            bh = ih * v / vmax
            y = PT + ih - bh
            s += bar(x + 1, y, bw - 2, bh, series[j][1] == "l", gris=series[j][1] == "g")
            s += T(x + bw / 2, y - 3, f(v), "middle", "", 6.8, 700)
        s += T(PL + gw * i + gw / 2, h - PB + 11, lab, "middle", "mu", 7)
    return svg(w, h, s)


def leyenda(items):
    out = ""
    for nombre, estilo in items:
        if estilo == "l":
            c = f"background:{LIMA};border:.6pt solid #000"
        elif estilo == "g":
            c = f"background:{GRIS2}"
        elif estilo == "h":
            c = f"background:repeating-linear-gradient(45deg,{LIMA} 0 2pt,#fff 2pt 4pt);border:.6pt solid #000"
        else:
            c = f"background:{NEGRO}"
        out += f'<span><i style="{c}"></i>{nombre}</span>'
    return f'<div class="ley">{out}</div>'


# ---------- diagramas ----------
def ciclo_trips(w=483):
    h = 150
    st = [("HUEVO", 3.07, "dentro del tejido", 0), ("LARVA I", 1.78, "en la planta", 1), ("LARVA II", 2.38, "en la planta", 1),
          ("PREPUPA", 1.00, "suelo", 0), ("PUPA", 2.04, "suelo u hojarasca", 0)]
    tot = sum(a[1] for a in st)
    sc = (w - 70) / tot
    x = 0
    s = T(0, 9, "DURACIÓN POR ESTADIO A 27 °C (DÍAS) · UF/IFAS, REPOLLO", "start", "mu", 6.5, 700)
    for a in st:
        bw = a[1] * sc
        fill = LIMA if a[3] else NEGRO
        col = "#000" if a[3] else "#fff"
        s += f'<rect x="{n(x)}" y="16" width="{n(bw-3)}" height="38" rx="5" fill="{fill}" stroke="#000" stroke-width=".6"/>'
        s += T(x + (bw - 3) / 2, 31, a[0], "middle", "", 7, 700, col) + T(x + (bw - 3) / 2, 44, f(a[1]) + " d", "middle", "", 7, 400, col)
        s += T(x + (bw - 3) / 2, 66, a[2], "middle", "mu", 6.5)
        x += bw
    s += f'<rect x="{n(x)}" y="16" width="64" height="38" rx="5" fill="#fff" stroke="#000" stroke-width=".8" stroke-dasharray="3 2"/>'
    s += T(x + 32, 31, "ADULTO", "middle", "", 7, 700) + T(x + 32, 44, "&lt;2 mm", "middle", "", 7) + T(x + 32, 66, "flores y hojas", "middle", "mu", 6.5)
    s += f'<path d="M0 78H{n(x-3)}M0 74V82M{n(x-3)} 74V82" stroke="#000" stroke-width=".8" fill="none"/>'
    s += T((x - 3) / 2, 92, "huevo → adulto: 10,2 días (cifra de la fuente)", "middle", "", 7)
    s += T(0, 116, "CICLO HUEVO → HUEVO POR TEMPERATURA (DÍAS) · EPPO", "start", "mu", 6.5, 700)
    tb = [("15 °C", 44.1), ("20 °C", 22.4), ("25 °C", 18.2), ("30 °C", 15)]
    for i, (t, v) in enumerate(tb):
        xx = i * (w / 4)
        s += T(xx, 134, t, "start", "", 7, 700) + T(xx + 34, 134, f(v) + " d", "start", "", 7)
        s += bar(xx, 139, (w / 4 - 16) * v / 44.1, 6, i == 3)
    return svg(w, h, s)


def matriz_eta_sexo(w=483):
    h = 210
    et = ["HUEVO", "LARVA I", "LARVA II", "PREPUPA", "PUPA", "ADULTO"]
    sx = ["INDIFERENCIADO", "MACHO", "HEMBRA"]
    x0, y0, cw, ch = 58, 20, 78, 28
    s = ""
    for j, a in enumerate(sx):
        s += T(x0 + j * cw + (cw - 5) / 2, y0 - 7, a, "middle", "mu", 6.3, 700)
    for i, e in enumerate(et):
        s += T(x0 - 6, y0 + i * ch + 16, e, "end", "", 6.8, 700)
        for j in range(3):
            ad = i == 5
            ok = (j > 0) if ad else (j == 0)
            x, y = x0 + j * cw, y0 + i * ch
            esc_ = i in (0, 3, 4)
            if ok and esc_:
                s += f'<rect x="{x}" y="{y}" width="{cw-5}" height="{ch-5}" rx="5" fill="#fff" stroke="#000" stroke-width=".8" stroke-dasharray="3 2"/>' + T(x + (cw - 5) / 2, y + 14, "pocas fotos", "middle", "", 6.5)
            elif ok:
                s += f'<rect x="{x}" y="{y}" width="{cw-5}" height="{ch-5}" rx="5" fill="{LIMA}" stroke="#000" stroke-width=".6"/>' + T(x + (cw - 5) / 2, y + 14, "centroide propio" if ad else "etapa sin sexo", "middle", "", 6.5)
            else:
                s += f'<rect x="{x}" y="{y}" width="{cw-5}" height="{ch-5}" rx="5" fill="#f1f2f4"/>'
    px = 312
    s += T(px, y0 - 7, "UN VECTOR → CABEZAS POR PREGUNTA", "start", "mu", 6.3, 700)
    s += f'<rect x="{px}" y="{y0}" width="150" height="30" rx="6" fill="{NEGRO}"/>' + T(px + 75, y0 + 18, "VECTOR DEL ENCODER (CONGELADO)", "middle", "", 6.5, 700, "#fff")
    for i, c in enumerate(["TAXÓN", "ETAPA", "SEXO"]):
        x = px + i * 52
        s += f'<path d="M{px+75} {y0+30}L{x+23} {y0+64}" stroke="#000" stroke-width=".6"/>'
        s += f'<rect x="{x}" y="{y0+64}" width="46" height="24" rx="6" fill="{LIMA}" stroke="#000" stroke-width=".6"/>' + T(x + 23, y0 + 79, c, "middle", "", 6.8, 700)
    s += T(px, y0 + 112, "Salud y calidad: cabezas aparte.", "start", "mu", 6.8)
    s += T(px, y0 + 124, "Con menos de 3 individuos en una celda", "start", "mu", 6.8)
    s += T(px, y0 + 136, "se presta el centroide global.", "start", "mu", 6.8)
    s += T(x0, h - 4, "Borde discontinuo: celdas con pocas fotos esperables (huevo, prepupa y pupa están ocultos). Esquema, no resultados.", "start", "mu", 6.5)
    return svg(w, h, s)


def arbol(w=226):
    h = 252
    r = ["REINO", "FILO", "CLASE", "ORDEN", "FAMILIA", "GÉNERO", "ESPECIE"]
    a = ["Animalia", "Chordata", "Amphibia", "Anura", "Bufonidae", "Rhinella", "R. marina"]
    p = ["Plantae", "Tracheophyta", "Liliopsida", "Poales", "Poaceae", "Zea", "Zea mays"]
    s = ""
    for i, e in enumerate(r):
        y = 4 + i * 33
        s += T(44, y + 15, e, "end", "mu", 6.3, 700)
        hi = i == 6
        s += f'<rect x="50" y="{y}" width="82" height="24" rx="5" fill="{LIMA if hi else NEGRO}" stroke="#000" stroke-width=".6"/>' + T(91, y + 15, a[i], "middle", "", 7, 700 if hi else 400, "#000" if hi else "#fff")
        s += f'<rect x="140" y="{y}" width="82" height="24" rx="5" fill="#fff" stroke="#000" stroke-width=".6"/>' + T(181, y + 15, p[i], "middle", "", 7)
        if i < 6:
            s += f'<path d="M91 {y+24}V{y+33}M181 {y+24}V{y+33}" stroke="#000" stroke-width=".6"/>'
    s += T(91, h - 4, "RANA", "middle", "mu", 6.3, 700) + T(181, h - 4, "PLANTA", "middle", "mu", 6.3, 700)
    return svg(w, h, s)


def pipeline(w=483):
    h = 128
    p = [("ALCANCE", "especies, región, móvil o web"), ("DATOS", "fuente y licencia por foto"), ("DIVISIÓN", "por individuo, no al azar"),
         ("LÍNEA BASE", "congelado + vecino cercano"), ("EVALUAR", "top-1, top-5, F1, matriz"), ("EXPORTAR", "ONNX, FP16, latencia"),
         ("CAMPO", "fotos nuevas, no solo test"), ("INTERFAZ", "3 mejores y aviso")]
    bw = (w - 3 * 10) / 4
    s = ""
    for i, (t, d) in enumerate(p):
        x = (i % 4) * (bw + 10)
        y = 0 if i < 4 else 68
        hi = i == 3
        s += f'<rect x="{n(x)}" y="{y}" width="{n(bw)}" height="56" rx="8" fill="{LIMA if hi else "#fff"}" stroke="#000" stroke-width=".7"/>'
        s += T(x + 9, y + 20, f"{i+1} · {t}", "start", "", 7.5, 700) + T(x + 9, y + 38, d, "start", "", 6.8)
        if i % 4 < 3:
            s += f'<path d="M{n(x+bw)} {y+28}h10" stroke="#000" stroke-width=".7"/>'
    s += f'<path d="M{n(3*(bw+10)+bw/2)} 56V68" stroke="#000" stroke-width=".7"/>'
    s += f'<path d="M{n(3*(bw+10)+bw/2)} 62H{n(bw/2)}V68" stroke="#000" stroke-width=".7" fill="none" stroke-dasharray="2 2"/>'
    return svg(w, h, s)


def escalera(w=483):
    st = [("1–10 fotos por clase", "Embeddings congelados + centroide o kNN; zero-shot como línea base", "BioCLIP 1: 1 foto 50,3 · 5 fotos 68,8"),
          ("10–70 fotos", "Lo anterior + aumentación moderada, solo en train y al vuelo", "Matiz ≤ ±10°"),
          ("Clases desbalanceadas", "Oversampling con aumentación en las repeticiones; pesos de raíz cuadrada", "Anura: < 70 individuos"),
          ("Faltan variantes difíciles", "CutMix, RandomErasing, copy-paste", "No mezclar especies del mismo género"),
          ("Faltan fotos de verdad", "Fuentes públicas y fotos propias; fusionar etapas (prepupa-pupa)", "Las etapas no vienen etiquetadas"),
          ("Último recurso", "Imágenes sintéticas (difusión), nunca en val ni test", "Evidencia débil")]
    rh = 40
    h = len(st) * rh
    s = ""
    for i, a in enumerate(st):
        x = i * 16
        y = i * rh
        hi = i == 0
        s += f'<rect x="{x}" y="{y}" width="{n(w-x)}" height="{rh-6}" rx="7" fill="{LIMA if hi else "#fff"}" stroke="#000" stroke-width=".7"/>'
        s += T(x + 10, y + 14, f"{i+1} · {a[0]}", "start", "", 7.5, 700) + T(x + 10, y + 26, a[1], "start", "", 6.8)
        s += T(w - 9, y + 14, a[2], "end", "mu" if not hi else "", 6.5)
    return svg(w, h, s)


def prior(w=226):
    h = 150
    PL, PR, PT, PB = 30, 8, 14, 24
    iw, ih = w - PL - PR, h - PT - PB
    Y = lambda v: PT + ih - ih * v / 1.6
    X = lambda u: PL + iw * u
    s = ""
    for v in (0.5, 1, 1.5):
        s += f'<line x1="{PL}" x2="{n(w-PR)}" y1="{n(Y(v))}" y2="{n(Y(v))}" stroke="{AX}" stroke-width=".6" {"" if v == 1 else "stroke-dasharray=\"3 3\""}/>' + T(PL - 4, Y(v) + 2.5, f(v), "end", "mu", 6.5)

    def c(sig, amp):
        return "".join(("L" if i else "M") + n(X(i / 100)) + " " + n(Y(0.5 + amp * math.exp(-((i / 100 - 0.5) ** 2) / (2 * sig * sig))))
                       for i in range(101))
    s += f'<path d="{c(.28,.5)}" stroke="{GRIS}" stroke-width="2" fill="none"/>'
    s += f'<path d="{c(.07,1)}" stroke="#000" stroke-width="3.2" fill="none"/><path d="{c(.07,1)}" stroke="{LIMA}" stroke-width="1.8" fill="none"/>'
    s += T(X(.56), PT + 4, "endémica", "start", "", 6.8, 700) + T(X(.98), Y(.66), "amplia", "end", "mu", 6.8, 700)
    s += T(PL + iw / 2, h - 6, "distancia al centro de sus observaciones →", "middle", "mu", 6.5)
    s += T(2, 8, "multiplicador", "start", "mu", 6.5)
    return svg(w, h, s)


def gosner_bbch(w=483):
    h = 150
    u = w / 46
    s = T(0, 8, "GOSNER (1960): 46 ESTADIOS DE ANURO", "start", "mu", 6.5, 700)
    gs = [(1, 25, "EMBRIONARIA", "", 0), (26, 30, "26–30", "esbozo", 1), (31, 37, "31–37", "dedos", 1), (38, 40, "38–40", "tubérc.", 1), (41, 41, "41", "", 0), (42, 46, "42–46", "metam.", 0)]
    for a, b, t1, t2, hi in gs:
        x = (a - 1) * u
        bw = (b - a + 1) * u - 2
        s += f'<rect x="{n(x)}" y="14" width="{n(bw)}" height="32" rx="4" fill="{LIMA if hi else NEGRO}" stroke="#000" stroke-width=".6"/>'
        col = "#000" if hi else "#fff"
        s += T(x + bw / 2, 28, t1, "middle", "", 6.8, 700, col) + T(x + bw / 2, 39, t2, "middle", "", 6.3, 400, col)
    s += T(0, 56, "1", "start", "mu", 6.5) + T(24.5 * u, 56, "25: empieza a alimentarse", "middle", "mu", 6.5) + T(w, 56, "46", "end", "mu", 6.5)
    s += T(0, 84, "BBCH (MEIER 2001): 10 ESTADIOS PRINCIPALES DE PLANTA", "start", "mu", 6.5, 700)
    bb = ["Germinac.", "Hojas", "Brotes lat.", "Elongac.", "Cosechable", "Inflor.", "Floración", "Fruto", "Maduración", "Senescen."]
    bw = w / 10
    for i, t in enumerate(bb):
        x = i * bw
        hi = i == 6
        s += f'<rect x="{n(x)}" y="90" width="{n(bw-3)}" height="34" rx="4" fill="{LIMA if hi else "#fff"}" stroke="#000" stroke-width=".6"/>'
        s += T(x + (bw - 3) / 2, 104, str(i), "middle", "", 7.5, 700) + T(x + (bw - 3) / 2, 117, t, "middle", "", 6.2)
    s += T(0, 142, "Primer dígito = estadio principal; segundo = secundario (base: código de cereales de Zadoks).", "start", "mu", 6.5)
    return svg(w, h, s)


def individuos(w=483):
    """Ilustración: mismo número de fotos, distinta variedad de individuos."""
    h = 176
    r = __import__("lib").azar(11)
    s = ""
    panes = [(0, "A · 1 INDIVIDUO × 20 FOTOS", 1), (w / 2 + 8, "B · 10 INDIVIDUOS × 2 FOTOS", 10)]
    pw = w / 2 - 8
    for x0, tit, k in panes:
        s += T(x0, 8, tit, "start", "", 7, 700)
        s += f'<rect x="{n(x0)}" y="14" width="{n(pw)}" height="128" rx="6" fill="#fff" stroke="#000" stroke-width=".6"/>'
        # nube real de la especie (elipse)
        cx, cy = x0 + pw / 2, 78
        s += f'<ellipse cx="{n(cx)}" cy="{cy}" rx="{n(pw*0.38)}" ry="44" fill="#f1f2f4" stroke="{GRIS}" stroke-width=".6" stroke-dasharray="3 2"/>'
        pts = []
        if k == 1:
            ox, oy = cx + pw * 0.22, cy - 22
            for _ in range(20):
                pts.append((ox + (r() - .5) * 18, oy + (r() - .5) * 14))
        else:
            for i in range(10):
                a = 2 * math.pi * i / 10 + r() * .4
                rr = .45 + r() * .45
                bx, by = cx + math.cos(a) * pw * .34 * rr, cy + math.sin(a) * 40 * rr
                for _ in range(2):
                    pts.append((bx + (r() - .5) * 8, by + (r() - .5) * 6))
        for px, py in pts:
            s += f'<circle cx="{n(px)}" cy="{n(py)}" r="2.2" fill="#000"/>'
        mx = sum(p[0] for p in pts) / len(pts)
        my = sum(p[1] for p in pts) / len(pts)
        s += f'<path d="M{n(mx-5)} {n(my-5)}L{n(mx+5)} {n(my+5)}M{n(mx+5)} {n(my-5)}L{n(mx-5)} {n(my+5)}" stroke="#000" stroke-width="3.4"/>'
        s += f'<path d="M{n(mx-5)} {n(my-5)}L{n(mx+5)} {n(my+5)}M{n(mx+5)} {n(my-5)}L{n(mx-5)} {n(my+5)}" stroke="{LIMA}" stroke-width="1.8"/>'
        s += f'<circle cx="{n(cx)}" cy="{cy}" r="3" fill="none" stroke="#000" stroke-width="1"/>'
        txt = ("El centroide (✕) cae lejos del centro real de la especie (○):" if k == 1 else "El centroide (✕) cae cerca del centro real (○):")
        txt2 = ("aprende ese animal, su fondo y su luz." if k == 1 else "aprende la especie, no un individuo.")
        s += T(x0, 156, txt, "start", "", 6.8) + T(x0, 167, txt2, "start", "mu", 6.8)
    return svg(w, h, s)


def curvas_ajuste(w=483):
    h = 190
    PL, PR, PT, PB = 30, 10, 26, 30
    iw, ih = w - PL - PR, h - PT - PB
    X = lambda e: PL + iw * e / 30
    Y = lambda v: PT + ih - ih * v / 1.0
    s = ""
    # zonas
    zonas = [(0, 6, "SUBAJUSTE", "#f1f2f4"), (6, 12, "PUNTO JUSTO", LIMA), (12, 30, "SOBREAJUSTE", "#f1f2f4")]
    for a, b, t, c in zonas:
        s += f'<rect x="{n(X(a))}" y="{PT}" width="{n(X(b)-X(a))}" height="{ih}" fill="{c}" {"" if c != LIMA else "fill-opacity=\".55\""}/>'
        s += T((X(a) + X(b)) / 2, PT - 8, t, "middle", "", 7, 700)
    for k in range(3):
        v = k / 2
        s += f'<line x1="{PL}" x2="{n(w-PR)}" y1="{n(Y(v))}" y2="{n(Y(v))}" stroke="{AX}" stroke-width=".6"/>'
    tr = [(e, 0.92 * math.exp(-e / 5.5) + 0.01) for e in range(0, 31)]
    va = [(e, 0.38 + 0.6 * math.exp(-e / 3.6) + 0.0016 * max(0, e - 10) ** 1.6) for e in range(0, 31)]
    s += f'<path d="{"".join(("L" if i else "M") + n(X(e)) + " " + n(Y(v)) for i, (e, v) in enumerate(tr))}" stroke="#000" stroke-width="1.6" fill="none"/>'
    s += f'<path d="{"".join(("L" if i else "M") + n(X(e)) + " " + n(Y(min(v, .99))) for i, (e, v) in enumerate(va))}" stroke="#000" stroke-width="1.6" fill="none" stroke-dasharray="5 3"/>'
    s += f'<line x1="{n(X(10))}" x2="{n(X(10))}" y1="{PT}" y2="{PT+ih}" stroke="#000" stroke-width="1"/>'
    s += T(X(10) + 4, Y(.93), "parada temprana", "start", "", 6.8, 700)
    s += T(X(29), Y(.07), "entrenamiento", "end", "", 6.8) + T(X(29), Y(.9), "validación", "end", "", 6.8)
    s += T(PL + iw / 2, h - 8, "épocas de entrenamiento →", "middle", "mu", 6.5) + T(2, PT + 4, "error", "start", "mu", 6.5)
    return svg(w, h, s)


def stack_diagrama(w=483):
    h = 156
    s = ""
    # local
    s += T(0, 9, "TODO LOCAL (KOTLIN, REACT NATIVE O FLUTTER)", "start", "", 7, 700)
    cajas = [("CÁMARA", "foto + GPS + fecha"), ("PREPROCESO", "224 px, misma media"), ("ENCODER ONNX", "BioCLIP 1 FP16"), ("CENTROIDES", "paquete SQLite"), ("TOP-3", "y nivel alcanzado")]
    bw = (w - 4 * 12) / 5
    for i, (t, d) in enumerate(cajas):
        x = i * (bw + 12)
        hi = i == 2
        s += f'<rect x="{n(x)}" y="16" width="{n(bw)}" height="42" rx="7" fill="{LIMA if hi else "#fff"}" stroke="#000" stroke-width=".7"/>'
        s += T(x + bw / 2, 33, t, "middle", "", 7, 700) + T(x + bw / 2, 46, d, "middle", "", 6.5)
        if i < 4:
            s += f'<path d="M{n(x+bw)} 37h12" stroke="#000" stroke-width=".7"/><path d="M{n(x+bw+12)} 37l-4 -2.5v5z" fill="#000"/>'
    s += T(0, 84, "MÓVIL COMO HERRAMIENTA DE ENTRADA + SERVIDOR", "start", "", 7, 700)
    s += f'<rect x="0" y="92" width="{n(bw*1.4)}" height="52" rx="7" fill="#fff" stroke="#000" stroke-width=".7"/>'
    s += T(bw * .7, 112, "APP (CUALQUIER STACK)", "middle", "", 7, 700) + T(bw * .7, 126, "captura foto y contexto", "middle", "", 6.5)
    xs = bw * 1.4 + 70
    s += f'<path d="M{n(bw*1.4)} 112H{n(xs)}" stroke="#000" stroke-width=".7"/><path d="M{n(xs)} 112l-4 -2.5v5z" fill="#000"/>'
    s += T((bw * 1.4 + xs) / 2, 106, "HTTPS", "middle", "mu", 6.3, 700)
    s += f'<path d="M{n(xs)} 128H{n(bw*1.4)}" stroke="#000" stroke-width=".7" stroke-dasharray="3 2"/><path d="M{n(bw*1.4)} 128l4 -2.5v5z" fill="#000"/>'
    s += T((bw * 1.4 + xs) / 2, 140, "top-3 + nivel", "middle", "mu", 6.3)
    s += f'<rect x="{n(xs)}" y="92" width="{n(w-xs)}" height="52" rx="7" fill="{NEGRO}"/>'
    s += T(xs + (w - xs) / 2, 112, "API EN MÁQUINA CON GPU", "middle", "", 7, 700, "#fff")
    s += T(xs + (w - xs) / 2, 126, "BioCLIP 2.5 cargado una vez · caché HF · vectores precalculados", "middle", "", 6.5, 400, LIMA)
    return svg(w, h, s)


def scraping(w=483):
    h = 74
    p = [("TAXONES", "y sinónimos"), ("API", "pausa y reintento"), ("METADATOS", "obs, licencia, GPS"), ("FILTRO", "licencia, precisión"),
         ("DESCARGA", "cola y reanudar"), ("DEDUP", "hash + observación"), ("DIVIDIR", "por individuo"), ("VERSIÓN", "fecha y conteos")]
    bw = (w - 7 * 6) / 8
    s = ""
    for i, (t, d) in enumerate(p):
        x = i * (bw + 6)
        hi = i in (5, 6)
        s += f'<rect x="{n(x)}" y="4" width="{n(bw)}" height="50" rx="7" fill="{LIMA if hi else "#fff"}" stroke="#000" stroke-width=".7"/>'
        s += T(x + bw / 2, 22, f"{i+1}", "middle", "", 8, 700) + T(x + bw / 2, 34, t, "middle", "", 6.3, 700) + T(x + bw / 2, 45, d, "middle", "", 5.6)
    s += T(0, 70, "Lima: los dos pasos que más evaluaciones han arruinado si se saltan (fotos repetidas y división al azar).", "start", "mu", 6.5)
    return svg(w, h, s)
