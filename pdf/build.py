"""Genera salida/guia.html (A4, identidad Notas Lima HUD + Dot Grid en hojas blancas)."""
import os, unicodedata
from lib import *
import charts as C
from charts import leyenda

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "../teoria/imagenes/"

# Caja de lectura de las hojas interiores (pt)
CX, CY, CW, CH = 64, 70, 467, 712


def aq(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").upper()


CSS = """
@font-face{font-family:Aquire;src:url(../pdf/fonts/AquireLight-YzE0o.otf);font-weight:300}
@font-face{font-family:Aquire;src:url(../pdf/fonts/Aquire-BW0ox.otf);font-weight:400}
@font-face{font-family:Aquire;src:url(../pdf/fonts/AquireBold-8Ma60.otf);font-weight:700}
@font-face{font-family:Bricolage;src:url(../pdf/fonts/bricolage-grotesque-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:Bricolage;src:url(../pdf/fonts/bricolage-grotesque-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:Bricolage;src:url(../pdf/fonts/bricolage-grotesque-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:Bricolage;src:url(../pdf/fonts/bricolage-grotesque-latin-800-normal.woff2);font-weight:800}
@font-face{font-family:JBMono;src:url(../pdf/fonts/jetbrains-mono-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:JBMono;src:url(../pdf/fonts/jetbrains-mono-latin-700-normal.woff2);font-weight:700}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#777}
body{font-family:Bricolage,"DejaVu Sans",sans-serif;color:#000;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{position:relative;width:595.28pt;height:841.89pt;overflow:hidden;break-after:page;margin:0 auto 12pt}
@media print{.pg{margin:0}html,body{background:none}}
.pg>svg.bg{position:absolute;left:0;top:0;width:595.28pt;height:841.89pt}
.ab{position:absolute}
.mono{font-family:JBMono,monospace;font-weight:700;font-size:6.6pt;letter-spacing:.08em;text-transform:uppercase}
.hud-r{position:absolute;height:.6pt;opacity:.35}
.barras{display:inline-flex;gap:3pt}.barras i{display:block;width:5.5pt;height:10pt;background:currentColor;transform:skewX(-30deg);border-radius:1pt}.barras i:last-child{width:9pt}
.cbar{display:inline-flex;gap:1.1pt;height:10pt}.cbar i{display:block;background:currentColor}
/* lectura */
.ct{position:absolute;left:64pt;top:70pt;width:467pt;height:712pt;font-size:9.6pt;line-height:1.55}
.ct p{margin:0 0 7pt}
.ct ul,.ct ol{margin:0 0 7pt;padding-left:13pt}.ct li{margin:0 0 3pt}
h1.t{font:700 17pt/1.05 Aquire,sans-serif;letter-spacing:.02em;margin:0 0 7pt}
.regla{width:92pt;height:2.4pt;background:#000;margin:0 0 15pt}
h2{font:700 11.2pt/1.25 Bricolage,sans-serif;margin:12pt 0 5pt}
h2:first-child{margin-top:0}
h2,h3{break-after:avoid-column;break-after:avoid}
h3{font:700 9.8pt/1.3 Bricolage,sans-serif;margin:9pt 0 3pt}
.lead{font:600 11.5pt/1.4 Bricolage,sans-serif;margin:0 0 12pt;max-width:440pt}
.c2{column-count:2;column-gap:23pt}
.c2>*{break-inside:avoid}
.sp{height:10pt}.sp2{height:18pt}
.et{font:700 6pt JBMono,monospace;letter-spacing:.05em;border:.6pt solid #000;border-radius:99px;padding:0 3pt;white-space:nowrap;vertical-align:1pt}
code{font:400 8pt JBMono,monospace;background:#eee;padding:0 2pt;border-radius:2pt}
pre{font:400 7.4pt/1.45 JBMono,monospace;background:#f3f3f3;border-left:3pt solid #000;padding:7pt 9pt;margin:4pt 0 10pt;white-space:pre-wrap;break-inside:avoid}
/* tablas */
table.tb{border-collapse:collapse;width:100%;font-size:8pt;line-height:1.36;margin:2pt 0 12pt;break-inside:avoid}
.tb th{text-align:left;font-weight:700;padding:3.5pt 5pt;border-top:1.5pt solid #000;border-bottom:1.5pt solid #000;vertical-align:bottom}
.tb td{padding:3.5pt 5pt;vertical-align:top;border-bottom:.6pt solid #aaa}
.tb.sm{font-size:7.5pt}
/* notas y bocadillos */
.nota{display:flex;gap:8pt;align-items:flex-start;margin:6pt 0 11pt;padding-left:8pt;border-left:1.6pt solid #000;break-inside:avoid}
.nota.resumen{border-left-width:3pt;padding-left:11pt;gap:11pt}
.nota .nm{flex:0 0 24pt}.nota.resumen .nm{flex-basis:32pt}
.nota p{margin:0;font-size:9.4pt;line-height:1.5}
.masc{display:block;width:100%;height:auto}
.boca{display:flex;gap:9pt;align-items:flex-start;margin:6pt 0 12pt;break-inside:avoid}
.boca .bm{flex:0 0 28pt}
.globo{position:relative;margin:2pt 0 0;padding:6pt 9pt;border-radius:9pt;background:#dfff04;color:#000;font:600 8.8pt/1.42 Bricolage,sans-serif;border:.6pt solid #000}
.globo::before{content:"";position:absolute;left:-6.5pt;top:8pt;border:4.5pt solid transparent;border-right:6.5pt solid #000;border-left:0}
.globo::after{content:"";position:absolute;left:-5.4pt;top:8.6pt;border:3.9pt solid transparent;border-right:5.6pt solid #dfff04;border-left:0}
.boca.inv .globo{background:#000;color:#dfff04}.boca.inv .globo::after{border-right-color:#000}
/* figuras */
.fig{margin:4pt 0 12pt;break-inside:avoid}
.fig svg.ch{display:block}
.pie{font-size:7.3pt;line-height:1.38;color:#333;margin:5pt 0 0}
.pie b{color:#000}
.ley{display:flex;flex-wrap:wrap;gap:4pt 12pt;font-size:7pt;color:#333;margin:4pt 0 0}
.ley i{display:inline-block;width:8pt;height:8pt;border-radius:1.5pt;margin-right:4pt;vertical-align:-1pt}
.cor{position:relative;padding:6pt}
.cor::before,.cor::after{content:"";position:absolute;width:14pt;height:14pt;border:2pt solid #000}
.cor::before{left:0;top:0;border-right:0;border-bottom:0}.cor::after{right:0;bottom:0;border-left:0;border-top:0}
.foto img{display:block;width:100%;object-fit:cover}
.fotos{display:grid;gap:10pt}
/* tablero */
.mets{display:grid;grid-template-columns:repeat(3,1fr);gap:10pt;margin:0 0 14pt}
.met{border-radius:12pt;padding:10pt 11pt;display:flex;flex-direction:column;gap:3pt}
.met small{font:700 6.4pt JBMono,monospace;letter-spacing:.08em;text-transform:uppercase}
.met strong{font:700 24pt/1 Aquire,sans-serif}
.met em{font:400 7.3pt/1.3 Bricolage,sans-serif;font-style:normal;opacity:.85}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12pt 23pt}
.g2>*{min-width:0}
.kick{font:700 6.6pt JBMono,monospace;letter-spacing:.08em;text-transform:uppercase;margin:0 0 4pt;color:#333}
/* aperturas, verdes, portada */
.chips{display:flex;gap:6pt;flex-wrap:wrap}
.chips span{height:20pt;padding:0 10pt;border-radius:99px;display:inline-grid;place-items:center;font:700 6.8pt JBMono,monospace;letter-spacing:.06em;border:1.4pt solid currentColor}
.pc-chip{display:flex;align-items:center;gap:8pt;font:700 8pt JBMono,monospace;letter-spacing:.1em;border:1.6pt solid #000;border-radius:99px;padding:4pt 12pt 4pt 6pt}
.pc-frase{border-left:7pt solid #000;padding:2pt 0 2pt 18pt;font:800 29pt/1.12 Bricolage,sans-serif;letter-spacing:-.01em}
.pc-ev strong{display:block;font:700 40pt/1 Aquire,sans-serif;color:#dfff04;margin:0 0 9pt}
.pc-ev p{margin:0;color:#fff;font-size:9pt;line-height:1.45}
.pc-col small{display:block;font:700 6.6pt JBMono,monospace;letter-spacing:.08em;color:#dfff04;margin:0 0 3pt}
.pc-col p{margin:0 0 12pt;color:#fff;font-size:9.4pt;line-height:1.5}
.titulo{font-family:Aquire,sans-serif;font-weight:700;line-height:.95;margin:0}
.sub{font-family:Bricolage,sans-serif;font-weight:600;line-height:1.22;margin:0}
.idx{font-size:9pt;line-height:1.42}
.idx .n1{display:flex;align-items:baseline;gap:6pt;font-weight:700;font-size:10pt;margin:7pt 0 1pt}
.idx .n2{display:flex;align-items:baseline;gap:6pt;padding-left:22pt}
.idx .g{flex:1;border-bottom:1pt dotted #777;transform:translateY(-3pt)}
.idx .num{font:700 7pt JBMono,monospace;width:16pt}
"""

PAGINAS = []
INDICE = []  # (nivel, texto, pagina)
CAP = {"n": 0, "nombre": ""}


def hud(color, cap, num):
    return (f'<div class="ab mono" style="left:64pt;top:26pt;color:{color}">SP-01 · {cap}</div>'
            f'<div class="ab" style="left:420pt;top:23.5pt">{barras_hud(color)}</div>'
            f'<div class="ab mono" style="right:64.28pt;top:26pt;color:{color};text-align:right">P.{num:02d}</div>'
            f'<div class="hud-r" style="left:64pt;top:44pt;width:467pt;background:{color}"></div>'
            f'<div class="ab" style="left:64pt;top:803pt">{codigo_barras(color)}</div>'
            f'<div class="ab mono" style="right:64.28pt;top:805pt;color:{color};text-align:right">GUÍA DE IA · VOL 01</div>')


def capstr():
    return f"CAP {CAP['n']:02d} · {CAP['nombre']}" if CAP["n"] else "INICIO"


def hoja(cuerpo, entrada=None, sub=None):
    """Hoja normal de lectura sobre papel con Dot Grid en el margen."""
    num = len(PAGINAS) + 1
    if entrada:
        INDICE.append((2, entrada, num))
    libre = [(CX - 14, CY - 14, CW + 28, CH + 22), (CX - 10, 16, CW + 20, 34), (CX - 10, 795, CW + 20, 28)]
    bg = f'<svg class="bg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>{puntos(libre)}</svg>'
    PAGINAS.append(f'<section class="pg" style="background:#fff">{bg}{hud("#000", capstr(), num)}<div class="ct">{cuerpo}</div></section>')


def titulo(t):
    return f'<h1 class="t">{aq(t)}</h1><div class="regla"></div>'


HF = [(50, 12, 495, 42), (50, 788, 495, 36)]


def apertura(numero, nombre, titulo_lineas, sub, chips, seed):
    """Hoja negra de apertura de capítulo."""
    CAP["n"] = numero
    CAP["nombre"] = aq(nombre)
    num = len(PAGINAS) + 1
    INDICE.append((1, f"{numero:02d} · {nombre}", num))
    g = glifos(GN, seed, manchas=[(480, 300, 260, 330), (90, 770, 150)], excl=[(56, 430, 440, 300), (56, 100, 330, 220)] + HF, polvo=0.04)
    ch = "".join(f'<span{" style=\"background:#dfff04;color:#000;border-color:#dfff04\"" if i == len(chips) - 1 else ""}>{c}</span>' for i, c in enumerate(chips))
    PAGINAS.append(f'<section class="pg" style="background:{NEGRO}"><svg class="bg" viewBox="0 0 {W} {H}">{g}</svg>{hud("#fff", capstr(), num)}'
                   f'<div class="ab titulo" style="left:62pt;top:118pt;font-size:178pt;line-height:.8;color:{LIMA}">{numero:02d}</div>'
                   f'<h2 class="ab titulo" style="left:64pt;top:446pt;font-size:36pt;color:#fff;margin:0">{"<br>".join(aq(x) for x in titulo_lineas)}</h2>'
                   f'<p class="ab sub" style="left:65pt;top:{458 + 40*len(titulo_lineas)}pt;width:360pt;font-size:13pt;color:#cfd2d6">{sub}</p>'
                   f'<div class="ab chips" style="left:65pt;top:{530 + 40*len(titulo_lineas)}pt;color:#fff;width:440pt">{ch}</div></section>')


def verde(n_, frase, cifra, cifra_nota, porque, hacer, seed, boca=None):
    """Hoja lima de punto clave. Se distingue del divisor: sin número gigante; la frase manda,
    con una barra negra a la izquierda, y debajo una caja negra de evidencia (cifra, por qué, qué hacer)."""
    num = len(PAGINAS) + 1
    g = glifos(GL, seed, manchas=[(560, 790, 230, 160), (600, 90, 120, 90)], excl=[(44, 54, 507, 580)] + HF, polvo=0.015)
    y0 = 304
    forma = forma_lima([(56, y0), (232, y0), (232, y0 + 40), (539, y0 + 40), (539, y0 + 236), (56, y0 + 236)], 44)
    diana = ('<svg width="22pt" height="22pt" viewBox="0 0 40 40"><circle cx="20" cy="20" r="11" fill="none" stroke="#000" stroke-width="3"/>'
             '<circle cx="20" cy="20" r="3.5" fill="#000"/><path d="M20 0V9M20 31V40M0 20H9M31 20H40" stroke="#000" stroke-width="3"/></svg>')
    b = ""
    if boca:
        b = f'<div class="ab" style="left:64pt;top:574pt;width:440pt">{bocadillo(boca, invertido=True, expresion="guino", forma="gota")}</div>'
    PAGINAS.append(
        f'<section class="pg" style="background:{LIMA}"><svg class="bg" viewBox="0 0 {W} {H}">{g}<path d="{forma}" fill="{NEGRO}"/></svg>'
        f'{hud("#000", capstr() + " · PUNTO CLAVE", num)}'
        f'<div class="ab pc-chip" style="left:64pt;top:74pt">{diana}<span>PUNTO CLAVE · {n_}</span></div>'
        f'<div class="ab pc-frase" style="left:64pt;top:126pt;width:467pt">{frase}</div>'
        f'<div class="ab mono" style="left:84pt;top:{y0 + 15}pt;color:{LIMA};font-size:7pt">LA EVIDENCIA</div>'
        f'<div class="ab pc-ev" style="left:84pt;top:{y0 + 62}pt;width:150pt"><strong>{cifra}</strong><p>{cifra_nota}</p></div>'
        f'<div class="ab pc-col" style="left:268pt;top:{y0 + 62}pt;width:244pt"><small>POR QUÉ</small><p>{porque}</p>'
        f'<small>QUÉ HACER</small><p>{hacer}</p></div>{b}</section>')


def fig(svg, pie=None, ley=None):
    return f'<div class="fig">{svg}{ley or ""}{f"<p class=pie>{pie}</p>" if pie else ""}</div>'


def foto(src, alto, pie):
    return f'<div class="fig"><div class="cor foto"><img src="{IMG}{src}" style="height:{alto}pt"></div><p class="pie">{pie}</p></div>'


def met(et, val, nota_, estilo):
    est = {"l": f"background:{LIMA};color:#000;border:.6pt solid #000", "n": f"background:{NEGRO};color:#fff", "g": "background:#f1f2f4;color:#000"}[estilo]
    return f'<div class="met" style="{est}"><small>{et}</small><strong>{val}</strong><em>{nota_}</em></div>'



CSS += """
.aprende{display:flex;gap:14pt;align-items:flex-start;background:#0b0d12;color:#fff;border-radius:12pt;padding:11pt 14pt;margin:0 0 15pt;break-inside:avoid}
.aprende .k{font:700 6.6pt JBMono,monospace;letter-spacing:.08em;color:#dfff04;flex:0 0 70pt;padding-top:2pt}
.aprende ul{list-style:none;margin:0;padding:0;font-size:9pt;line-height:1.48}
.aprende li{padding-left:13pt;position:relative;margin:0 0 2pt}
.aprende li::before{content:"";position:absolute;left:0;top:4.4pt;width:5pt;height:5pt;border:1.3pt solid #dfff04;border-radius:50%}
.paso{display:grid;grid-template-columns:20pt 1fr;gap:0 8pt;margin:0 0 10pt;break-inside:avoid}
.paso .nn{font:700 14pt/1 Aquire,sans-serif;padding-top:1pt}
.paso h3{margin:0 0 2pt}.paso p{margin:0}
.exp{border:1pt solid #000;border-radius:12pt;padding:9pt 11pt;break-inside:avoid;display:flex;flex-direction:column;gap:4pt;background:#fff}
.exp .top{display:flex;justify-content:space-between;align-items:center;gap:8pt}
.exp .q{font:700 6.2pt JBMono,monospace;letter-spacing:.07em;text-transform:uppercase;color:#333}
.exp h3{margin:0;font-size:10.2pt}
.exp dl{display:grid;grid-template-columns:52pt 1fr;gap:3pt 6pt;margin:2pt 0 0;font-size:8.4pt;line-height:1.4}
.exp dt{font:700 6pt/1.9 JBMono,monospace;letter-spacing:.06em;text-transform:uppercase;color:#333}
.exp dd{margin:0}
.ver{font:700 6.3pt JBMono,monospace;letter-spacing:.06em;border-radius:99px;padding:3pt 8pt;white-space:nowrap;border:1.2pt solid #000}
.ver.si{background:#dfff04}.ver.no{background:#000;color:#dfff04;border-color:#000}.ver.medio{background:#fff}
.cambio{display:grid;grid-template-columns:1fr 24pt 1fr;align-items:stretch;margin:4pt 0 14pt;break-inside:avoid}
.cambio>div{border-radius:12pt;padding:9pt 11pt;font-size:8.9pt;line-height:1.45}
.cambio .antes{background:#f1f2f4}.cambio .despues{background:#dfff04;border:.8pt solid #000}
.cambio small{display:block;font:700 6.3pt JBMono,monospace;letter-spacing:.08em;margin:0 0 3pt}
.cambio .fl{display:grid;place-items:center;font:700 15pt Bricolage,sans-serif}
.turno{border-top:2.4pt solid #000;padding-top:8pt;margin-top:6pt;break-inside:avoid}
.turno .k{font:700 6.6pt JBMono,monospace;letter-spacing:.08em;margin:0 0 5pt}
.turno ul{list-style:none;margin:0;padding:0;columns:2;column-gap:23pt;font-size:8.9pt;line-height:1.45}
.turno li{padding-left:15pt;position:relative;margin:0 0 4pt;break-inside:avoid}
.turno li::before{content:"";position:absolute;left:0;top:2.5pt;width:8pt;height:8pt;border:1.2pt solid #000;border-radius:1.5pt}
.graf{margin:0 0 13pt;break-inside:avoid}
.c2+.graf,.c2+.fig,.c2+.exp,.c2+.cambio{margin-top:8pt}
.graf .gt{font:700 6.6pt JBMono,monospace;letter-spacing:.08em;text-transform:uppercase;margin:0 0 5pt}
.graf svg.ch{display:block}
.graf dl{display:grid;grid-template-columns:54pt 1fr;gap:3pt 6pt;margin:6pt 0 0;padding-top:5pt;border-top:.6pt solid #000;font-size:8.2pt;line-height:1.4}
.graf dt{font:700 5.9pt/1.95 JBMono,monospace;letter-spacing:.06em;text-transform:uppercase;color:#333}
.graf dd{margin:0}
.graf dd.en{font-weight:600}
"""


def aprende(items):
    return '<div class="aprende"><div class="k">AL TERMINAR<br>SABRÁS</div><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"


def paso(nn, t, p):
    return f'<div class="paso"><span class="nn">{nn}</span><div><h3>{t}</h3><p>{p}</p></div></div>'


def exp(pregunta, titulo_, veredicto, filas):
    cls = {"FUNCIONÓ": "si", "NO FUNCIONÓ": "no", "A MEDIAS": "medio"}[veredicto]
    dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in filas)
    return (f'<div class="exp"><div class="top"><span class="q">{pregunta}</span><span class="ver {cls}">{veredicto}</span></div>'
            f'<h3>{titulo_}</h3><dl>{dl}</dl></div>')


def cambio(antes, despues):
    return (f'<div class="cambio"><div class="antes"><small>ANTES</small>{antes}</div><div class="fl">→</div>'
            f'<div class="despues"><small>DESPUÉS</small>{despues}</div></div>')


def turno(items):
    return '<div class="turno"><p class="k">TU TURNO · QUÉ PUEDES HACER</p><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"


def graf(t, svg, muestra, ensena, ley=None):
    """Gráfico con título y las dos lecturas: qué muestra y qué nos enseñó."""
    return (f'<div class="graf"><p class="gt">{t}</p>{svg}{ley or ""}<dl><dt>Qué muestra</dt><dd>{muestra}</dd>'
            f'<dt>Qué enseñó</dt><dd class="en">{ensena}</dd></dl></div>')


E = lambda s: f'<span class="et">{s}</span>'

# =====================================================================================
# PORTADA · estilo Hoja negra · apertura
# =====================================================================================
def portada():
    g = glifos(GN, 33, manchas=[(500, 250, 230, 300), (110, 790, 150)], excl=[(56, 420, 470, 320), (56, 90, 300, 260), (50, 30, 495, 24), (50, 780, 495, 40)], polvo=0.04)
    PAGINAS.append(
        f'<section class="pg" style="background:{NEGRO}"><svg class="bg" viewBox="0 0 {W} {H}">{g}</svg>'
        f'<div class="ab mono" style="left:64pt;top:42pt;color:#fff">TEORÍA · VOLUMEN 01</div>'
        f'<div class="ab mono" style="right:64.28pt;top:42pt;color:{LIMA};text-align:right">SP-01</div>'
        f'<div class="ab titulo" style="left:58pt;top:104pt;font-size:210pt;line-height:.8;color:{LIMA}">IA</div>'
        f'<h1 class="ab titulo" style="left:64pt;top:440pt;font-size:50pt;color:#fff">GUIA DE IA</h1>'
        f'<p class="ab sub" style="left:65pt;top:506pt;width:380pt;font-size:19pt;color:#cfd2d6">Cómo hacer que un modelo distinga animales</p>'
        f'<p class="ab" style="left:65pt;top:578pt;width:360pt;font-size:10pt;line-height:1.5;color:#cfd2d6">Especie, etapa, sexo y salud desde una foto, con contexto. '
        f'Teoría, rutas y lecciones medidas, con un caso conductor: los trips <i>Frankliniella</i>.</p>'
        f'<div class="ab chips" style="left:65pt;top:668pt;color:#fff"><span>ESPECIE</span><span>ETAPA</span><span>SEXO</span><span style="background:{LIMA};color:#000;border-color:{LIMA}">CONTEXTO</span></div>'
        f'<div class="ab" style="left:64pt;top:790pt">{codigo_barras("#fff", 9)}</div>'
        f'<div class="ab" style="left:452pt;top:788pt">{barras_hud(LIMA)}</div></section>')


portada()
PAGINAS.append("@@INDICE@@")

# =====================================================================================
# CAP 01 · FUNDAMENTOS
# =====================================================================================
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "contenido.py"), encoding="utf-8").read())


# =====================================================================================
# ÍNDICE (se rellena al final con los números reales)
# =====================================================================================
def indice_html():
    out = ""
    for nivel, texto, pag in INDICE:
        if nivel == 1:
            out += f'<div class="n1"><span>{texto}</span><span class="g"></span><span>{pag:02d}</span></div>'
        else:
            out += f'<div class="n2"><span>{texto}</span><span class="g"></span><span>{pag:02d}</span></div>'
    libre = [(CX - 14, CY - 14, CW + 28, CH + 22), (CX - 10, 16, CW + 20, 34), (CX - 10, 795, CW + 20, 28)]
    bg = f'<svg class="bg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>{puntos(libre)}</svg>'
    return (f'<section class="pg" style="background:#fff">{bg}{hud("#000", "ÍNDICE", 2)}<div class="ct">{titulo("Índice")}'
            f'<div class="idx">{out}</div></div></section>')


paginas = [indice_html() if p == "@@INDICE@@" else p for p in PAGINAS]
doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Guía de IA</title><style>{CSS}</style></head><body>'
       + C.DEFS + "".join(paginas) + "</body></html>")
os.makedirs(os.path.join(RAIZ, "salida"), exist_ok=True)
with open(os.path.join(RAIZ, "salida", "guia.html"), "w", encoding="utf-8") as fh:
    fh.write(doc)
print(len(paginas), "páginas")
