"""Piezas de la identidad Notas Lima HUD para el PDF (unidades: pt; hoja A4 595 x 842)."""
import math, html

W, H = 595.28, 841.89
NEGRO, LIMA, PAPEL, TINTA = "#0b0d12", "#dfff04", "#ffffff", "#000000"
GP, GN, GL = "#cfd2d6", "#2c3138", "#b7d100"
GRIS, GRIS2, SUAVE = "#8a929c", "#c9cdd2", "#333333"
PUNTO = "#bdbdbd"


def n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def esc(s):
    return html.escape(s, quote=False)


def azar(seed):
    s = [seed]

    def r():
        s[0] = (s[0] * 16807) % 2147483647
        return (s[0] - 1) / 2147483646
    return r


# ---------- forma con esquinas interiores ----------
def forma_lima(pts, r=44):
    k = len(pts)
    d = ""
    for i in range(k):
        a, p, b = pts[(i - 1) % k], pts[i], pts[(i + 1) % k]
        l1 = math.hypot(p[0] - a[0], p[1] - a[1])
        l2 = math.hypot(b[0] - p[0], b[1] - p[1])
        d1 = ((p[0] - a[0]) / l1, (p[1] - a[1]) / l1)
        d2 = ((b[0] - p[0]) / l2, (b[1] - p[1]) / l2)
        rr = min(r, l1 / 2, l2 / 2)
        giro = 1 if d1[0] * d2[1] - d1[1] * d2[0] > 0 else 0
        d += ("L" if i else "M") + f"{n(p[0]-d1[0]*rr)},{n(p[1]-d1[1]*rr)}"
        d += f"A{n(rr)},{n(rr)} 0 0 {giro} {n(p[0]+d2[0]*rr)},{n(p[1]+d2[1]*rr)}"
    return d + "Z"


# ---------- fondo de glifos ----------
def _glifo(t, c):
    if t == "anillo":
        return f'<circle r="4.2" fill="none" stroke="{c}" stroke-width="1.3"/><circle r="1.5" fill="{c}"/>'
    if t == "equis":
        return f'<path d="M-3.6-3.6L3.6 3.6M3.6-3.6L-3.6 3.6" stroke="{c}" stroke-width="1.9" stroke-linecap="round"/>'
    if t == "cuadro":
        return f'<rect x="-3.8" y="-3.8" width="7.6" height="7.6" rx="1.3" fill="none" stroke="{c}" stroke-width="1.4"/>'
    if t == "cuadro-punto":
        return _glifo("cuadro", c) + f'<rect x="-1.3" y="-1.3" width="2.6" height="2.6" fill="{c}"/>'
    if t == "trebol":
        return "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="{c}"/>' for x, y in ((-2, -2), (2, -2), (-2, 2), (2, 2)))
    if t == "mas":
        return f'<path d="M-2.8 0H2.8M0-2.8V2.8" stroke="{c}" stroke-width="1.1"/>'
    if t == "barra":
        return f'<path d="M-2.4 2.4L2.4-2.4" stroke="{c}" stroke-width="1"/>'
    return f'<circle r="1" fill="{c}"/>'


def glifos(c, seed=7, manchas=(), excl=(), polvo=0.02, paso=15, w=W, h=H, x0=0, y0=0):
    r = azar(seed)
    fuertes = ["anillo", "anillo", "cuadro", "cuadro-punto", "equis", "trebol"]
    out = []
    y = paso / 2 + y0
    while y < h:
        x = paso / 2 + x0
        while x < w:
            if not any(e[0] - 6 < x < e[0] + e[2] + 6 and e[1] - 6 < y < e[1] + e[3] + 6 for e in excl):
                f = 0
                for m in manchas:
                    ry = m[3] if len(m) > 3 else m[2]
                    f = max(f, 1 - math.hypot((x - m[0]) / m[2], (y - m[1]) / ry))
                f += (r() - 0.5) * 0.35
                if f > 0.5:
                    t = fuertes[int(r() * len(fuertes))]
                elif f > 0.3:
                    t = "mas" if r() < 0.5 else "barra"
                elif f > 0.1:
                    t = "punto"
                else:
                    t = "punto" if r() < polvo else None
                if t:
                    out.append(f'<g transform="translate({n(x)} {n(y)})">{_glifo(t, c)}</g>')
            x += paso
        y += paso
    return "".join(out)


# ---------- cuadrícula de puntos (Dot Grid) para hojas blancas ----------
def puntos(libre):
    """Puntos de 6 mm en toda la hoja salvo en los rectángulos `libre` (x, y, w, h)."""
    paso = 17.01
    out = []
    y = paso / 2
    while y < H:
        x = paso / 2
        while x < W:
            if not any(e[0] - 3 < x < e[0] + e[2] + 3 and e[1] - 3 < y < e[1] + e[3] + 3 for e in libre):
                out.append(f'<circle cx="{n(x)}" cy="{n(y)}" r="0.85"/>')
            x += paso
        y += paso
    return f'<g fill="{PUNTO}">' + "".join(out) + "</g>"


# ---------- mascota ----------
FORMAS = {
    "circulo": ('<circle cx="50" cy="52" r="40"/>', 52, 30),
    "gota": ('<path d="M50 8 C58 22 84 40 84 62 C84 80 69 93 50 93 C31 93 16 80 16 62 C16 40 42 22 50 8 Z"/>', 63, 26),
    "nube": ('<circle cx="30" cy="60" r="20"/><circle cx="52" cy="44" r="25"/><circle cx="73" cy="58" r="21"/><rect x="14" y="58" width="78" height="28" rx="14"/>', 60, 28),
    "cubo": ('<rect x="16" y="20" width="68" height="66" rx="13" transform="rotate(-4 50 53)"/>', 54, 28),
    "triangulo": ('<path d="M50 12 Q57 12 63 24 L89 72 Q96 88 80 90 L20 90 Q4 88 11 72 L37 24 Q43 12 50 12 Z"/>', 68, 23),
    "flor": ('<circle cx="50" cy="52" r="28"/><circle cx="50" cy="24" r="16"/><circle cx="76" cy="40" r="16"/><circle cx="76" cy="66" r="16"/><circle cx="50" cy="80" r="16"/><circle cx="24" cy="66" r="16"/><circle cx="24" cy="40" r="16"/>', 52, 26),
}
_P = {"t": "p", "w": 8, "h": 20}


def _o(izq, der=None, mirada=None):
    return {"izq": izq, "der": der or izq, "mirada": mirada or (0, 0)}


EXPRESIONES = {
    "reposo": _o(_P),
    "feliz": _o({"t": "a", "w": 5}),
    "celebra": _o({"t": "a", "w": 5.5, "g": -12}, {"t": "a", "w": 5.5, "g": 12}, (0, -0.25)),
    "alerta": _o({"t": "p", "w": 9, "h": 27}),
    "sorpresa": _o({"t": "p", "w": 15, "h": 17}),
    "duda": _o({"t": "p", "w": 8, "h": 22, "dy": -2}, {"t": "p", "w": 8, "h": 13, "dy": 3}),
    "guino": _o({"t": "l"}, _P),
    "pensando": _o({"t": "p", "w": 8, "h": 17}, None, (0.55, -0.6)),
    "leyendo": _o({"t": "p", "w": 8, "h": 12}, None, (0, 0.7)),
    "serio": _o({"t": "p", "w": 8, "h": 18, "g": -14}, {"t": "p", "w": 8, "h": 18, "g": 14}),
}
_cuenta = [0]


def _ojo(e, lado, cy, rad, yaw, pitch, relleno):
    a = yaw + lado * 0.42
    x = 50 + rad * math.sin(a) * math.cos(pitch * 0.6)
    y = cy + e.get("dy", 0) + rad * 0.7 * math.sin(pitch)
    sx = max(0.3, math.cos(a))
    sy = max(0.55, math.cos(pitch)) * (0.85 + 0.15 * math.cos(a))
    giro = e.get("g", 0) + 28 * math.sin(a) * math.sin(pitch)
    w, h = e.get("w", 8), e.get("h", 20)
    if e["t"] == "a":
        f = f'<path d="M{-w} 4 Q0 {-(w+3)} {w} 4" fill="none" stroke-width="5" stroke-linecap="round" stroke="{relleno}"/>'
    elif e["t"] == "l":
        f = f'<rect x="-9" y="-3" width="18" height="6" rx="3" fill="{relleno}"/>'
    else:
        f = f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="{w/2}" fill="{relleno}"/>'
    return f'<g transform="translate({n(x)} {n(y)}) rotate({n(giro)}) scale({n(sx)} {n(sy)})">{f}</g>'


def mascota(forma="circulo", expresion="reposo", mirada=None, tinta=TINTA, papel=PAPEL):
    d, cy, rad = FORMAS[forma]
    ex = EXPRESIONES[expresion]
    m = mirada or ex["mirada"]
    yaw, pitch = max(-1, min(1, m[0])) * 0.7, max(-1, min(1, m[1])) * 0.55
    _cuenta[0] += 1
    cid = f"m{_cuenta[0]}"
    return (f'<svg class="masc" viewBox="0 0 100 100" aria-hidden="true"><clipPath id="{cid}">{d}</clipPath>'
            f'<g fill="{tinta}">{d}</g><g clip-path="url(#{cid})">'
            + _ojo(ex["izq"], -1, cy, rad, yaw, pitch, papel) + _ojo(ex["der"], 1, cy, rad, yaw, pitch, papel) + "</g></svg>")


NOTAS = [("Resumen", "feliz"), ("Recuerda", "reposo"), ("Para recordar", "celebra"), ("Ojo", "alerta"),
         ("Cuidado", "sorpresa"), ("Truco", "guino"), ("Ejemplo", "pensando"), ("Dato", "reposo"), ("¿Sab", "duda"),
         ("Práctica", "leyendo"), ("Error", "serio")]
_formas_rot = list(FORMAS)
_nota_i = [0]


def expresion_de(et):
    for k, v in NOTAS:
        if et.startswith(k):
            return v
    return "reposo"


def nota(etiqueta, cuerpo, resumen=False):
    forma = _formas_rot[_nota_i[0] % len(_formas_rot)]
    _nota_i[0] += 1
    return (f'<aside class="nota{" resumen" if resumen else ""}"><div class="nm">'
            + mascota(forma, expresion_de(etiqueta), (0.55, 0.1))
            + f'</div><p><b>{etiqueta}</b> {cuerpo}</p></aside>')


def bocadillo(cuerpo, invertido=False, expresion="feliz", forma="circulo"):
    t, p = (TINTA, PAPEL)
    return (f'<aside class="boca{" inv" if invertido else ""}"><div class="bm">'
            + mascota(forma, expresion, (0.55, -0.1), t, p) + f'</div><p class="globo">{cuerpo}</p></aside>')


def tabla(filas, anchos=None, cls=""):
    cab = filas[0]
    col = ""
    if anchos:
        col = "<colgroup>" + "".join(f'<col style="width:{a}%">' for a in anchos) + "</colgroup>"
    h = "<tr>" + "".join(f"<th>{c}</th>" for c in cab) + "</tr>"
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas[1:])
    return f'<table class="tb {cls}">{col}<thead>{h}</thead><tbody>{b}</tbody></table>'


def barras_hud(color):
    return (f'<span class="barras" style="color:{color}"><i></i><i></i><i></i><i></i></span>')


def codigo_barras(color, seed=3):
    r = azar(seed)
    s = "".join(f'<i style="width:{0.9 + int(r()*3)*0.9:.1f}pt"></i>' for _ in range(26))
    return f'<span class="cbar" style="color:{color}">{s}</span>'
