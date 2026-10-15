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
.titulo{font-family:Aquire,sans-serif;font-weight:700;line-height:.95;margin:0}
.sub{font-family:Bricolage,sans-serif;font-weight:600;line-height:1.22;margin:0}
.idx{font-size:9.4pt;line-height:1.5}
.idx .n1{display:flex;align-items:baseline;gap:6pt;font-weight:700;font-size:10.4pt;margin:10pt 0 2pt}
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


def verde(cifra, frase, detalle, seed, boca=None):
    """Hoja lima de punto clave: cifra gigante, una frase y el detalle en una forma negra."""
    num = len(PAGINAS) + 1
    g = glifos(GL, seed, manchas=[(590, 760, 200, 180), (0, 160, 110)], excl=[(44, 60, 507, 640)] + HF, polvo=0.02)
    forma = forma_lima([(56, 470), (380, 470), (380, 424), (539, 424), (539, 650), (56, 650)], 44)
    b = ""
    if boca:
        b = f'<div class="ab" style="left:64pt;top:712pt;width:440pt">{bocadillo(boca, invertido=True, expresion="guino", forma="gota")}</div>'
    PAGINAS.append(f'<section class="pg" style="background:{LIMA}"><svg class="bg" viewBox="0 0 {W} {H}">{g}<path d="{forma}" fill="{NEGRO}"/></svg>{hud("#000", capstr() + " · PUNTO CLAVE", num)}'
                   f'<div class="ab titulo" style="left:60pt;top:96pt;font-size:120pt;line-height:.8">{cifra}</div>'
                   f'<div class="ab mono" style="left:64pt;top:212pt;font-size:8pt">PUNTO CLAVE</div>'
                   f'<p class="ab sub" style="left:64pt;top:232pt;width:450pt;font-size:23pt;line-height:1.16">{frase}</p>'
                   f'<div class="ab" style="left:92pt;top:500pt;width:420pt;color:#fff;font-size:10.6pt;line-height:1.55">{detalle}</div>{b}</section>')


def fig(svg, pie=None, ley=None):
    return f'<div class="fig">{svg}{ley or ""}{f"<p class=pie>{pie}</p>" if pie else ""}</div>'


def foto(src, alto, pie):
    return f'<div class="fig"><div class="cor foto"><img src="{IMG}{src}" style="height:{alto}pt"></div><p class="pie">{pie}</p></div>'


def met(et, val, nota_, estilo):
    est = {"l": f"background:{LIMA};color:#000;border:.6pt solid #000", "n": f"background:{NEGRO};color:#fff", "g": "background:#f1f2f4;color:#000"}[estilo]
    return f'<div class="met" style="{est}"><small>{et}</small><strong>{val}</strong><em>{nota_}</em></div>'


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
apertura(1, "Fundamentos", ["Que se le puede", "preguntar a una foto"],
         "Especie, etapa, sexo, edad y salud: cada pregunta tiene su propia fiabilidad.", ["TAXÓN", "ETAPA", "SEXO", "RANGO"], 81)

hoja(titulo("Cómo leer esta guía") +
     '<p class="lead">Esta guía no diseña tu modelo: te da los conceptos, las opciones y lo que pasó cuando alguien las probó de verdad.</p>'
     '<div class="c2">'
     '<p>Está escrita para estudiantes que van a construir un modelo que reconozca un organismo en una foto. El caso conductor son los trips del género <i>Frankliniella</i>: el objetivo es saber <b>en qué etapa de vida</b> está el insecto y recomendar el manejo adecuado.</p>'
     '<p>Casi todas las cifras medidas vienen de <b>Anura</b>, un proyecto que identifica ranas de Colombia con BioCLIP en el móvil. Sus aciertos y sus errores valen para cualquier otro grupo de animales o plantas.</p>'
     '<h2>Las etiquetas de cada dato</h2>'
     f'<p>{E("FUENTE")} leído en un paper o una ficha. {E("PROYECTO")} medido o decidido en Anura. {E("CALC")} calculado a partir de otras cifras. {E("INF")} inferencia o recomendación propia, sin fuente. {E("SIMULACIÓN")} supuesto, nunca resultado.</p>'
     '<p>Un número sin sus condiciones (cuántas especies, qué división, qué versión) no sirve para decidir. Por eso las cifras van con su contexto.</p>'
     '<h2>Qué cubre y qué no</h2>'
     '<p><b>Sólido:</b> identificar la especie de un animal en foto y, si no se puede, el género o la familia. <b>Parcial:</b> etapa, sexo, plantas y salud. <b>No desde una foto:</b> la edad en años y el diagnóstico de una enfermedad.</p>'
     '</div><div class="sp"></div>' +
     nota("Resumen.", "Mide antes de construir, devuelve solo el nivel que la evidencia sostiene y reporta cada cifra con sus condiciones.", True) +
     '<div class="sp"></div><h2>El recorrido</h2>' +
     tabla([["Capítulo", "Qué resuelve"],
            ["01 · Fundamentos", "Qué preguntar a una foto, qué rango taxonómico elegir y por qué una especie no es una sola apariencia"],
            ["02 · El modelo", "BioCLIP 1, 2 y 2.5, dónde conseguirlo, cómo configurarlo, la ruta de método y la decisión entre congelar o ajustar"],
            ["03 · Los datos", "De dónde sacar imágenes y cómo scrapear, individuos frente a fotos, sobreajuste, etiquetado y pocas imágenes"],
            ["04 · Caso real", "Resultados y errores medidos en Anura"],
            ["05 · Contexto", "Lugar, hospedero y época; especies casi idénticas; etapa, sexo, edad y enfermedad"],
            ["06 · Frankliniella", "Ciclo de vida, identificación por contexto y de la etapa al manejo"],
            ["07 · Despliegue", "Stack (Kotlin, React Native, Flutter o servidor), FP16, multi-pregunta y límites"]], [26, 74]),
     "Cómo leer esta guía")

hoja(titulo("Qué se puede preguntar a una foto") +
     '<p class="lead">Una foto responde cinco familias de preguntas, cada una con una fiabilidad distinta.</p>' +
     tabla([["Pregunta", "Qué evidencia visual usa", "Fiabilidad típica"],
            ["Especie, género, familia", "Forma, color, patrón", "Alta si hay datos; baja en especies gemelas"],
            ["Etapa de vida", "Cambios de forma (larva → adulto), fenología", "Media; depende del grupo"],
            ["Sexo", "Dimorfismo: tamaño, color, estructuras", "Solo si la especie lo tiene y se ve"],
            ["Edad", "Casi nada fiable en foto", "Baja: se usan clases de edad (cría, joven, adulto)"],
            ["Salud", "Lesiones visibles", "Pistas inespecíficas; no es diagnóstico"]], [24, 42, 34]) +
     '<div class="sp"></div><div class="c2">'
     '<h2>La regla</h2>'
     '<p>La respuesta debe tener el nivel que la evidencia sostiene, igual que con la taxonomía. Ejemplos: «adulto, sexo no determinable» o «signos compatibles con una enfermedad de la piel; requiere confirmación».</p>'
     '<p>Un sistema que siempre da especie, etapa y sexo, aunque la foto no lo permita, es peor que uno que a veces dice «no sé».</p>'
     '<h2>Cuando la foto no basta</h2>'
     '<ol><li>Pedir otra foto: otro ángulo, más cerca, con escala.</li><li>Pedir otro órgano: hoja, flor, fruto; el vientre de la rana.</li>'
     '<li>Cambiar de pregunta: de «qué plaga» a «estado de la rama o de la planta».</li><li>Añadir contexto: lugar, altitud, fecha, cultivo, hospedero.</li>'
     '<li>Bajar de rango (especie → género → familia) o decir «no determinable».</li></ol>'
     '</div>' +
     bocadillo("La edad en años casi nunca sale de una foto: en anuros se cuentan líneas de crecimiento en un hueso del dedo.", expresion="pensando"),
     "Qué se puede preguntar a una foto")

verde("01", "Devuelve solo el nivel que la evidencia sostiene.",
      "<p>«Familia Hylidae, género probable <i>Boana</i>, especie no determinable» vale más que un nombre de especie equivocado.</p>"
      "<p>En Anura, 27 de 28 especies con pocos datos quedaron cubiertas a nivel de género o familia. El rescate vino de la taxonomía, no de inflar los datos.</p>",
      71)

hoja(titulo("Elegir el rango taxonómico") +
     '<p class="lead">El grupo que quieres evaluar debe separarse fácilmente de sus vecinos. Elige un rango cuyo límite sea visible y estable.</p>'
     '<div class="g2"><div>'
     '<p>Ejemplo: los anuros se separan del resto de anfibios porque <b>no tienen cola</b> (<i>Anura</i> significa «sin cola»). Lo fácil, rana frente a no-rana, se resuelve con un umbral. Lo difícil, especie frente a especie del mismo género, necesita datos y contexto.</p>'
     f'<p>Medido en Anura {E("PROYECTO")}: «no es una rana» se separa casi a la perfección (AUROC 0,987–0,992). Una rana frente a otra rana, no (AUROC 0,665 en la subregión del Sinú).</p>'
     '<p>Los falsos positivos de «no-rana» fueron los vecinos más parecidos: reptiles (23 %) y salamandras (15 %).</p>'
     '<h2>El rasgo depende de la etapa</h2>'
     '<p>Los renacuajos <b>sí</b> tienen cola: «sin cola» solo vale para el adulto. Por eso etapa y rango no se resuelven por separado.</p>'
     '<h2>Para un grupo nuevo</h2>'
     '<p>Escribe la lista de rasgos que lo separan de sus vecinos más parecidos y comprueba que se ven en foto. En trips, el orden Thysanoptera se reconoce por las alas con flecos y un tamaño menor de 2 mm; la especie no se reconoce en foto.</p>'
     '</div><div>' +
     fig(C.arbol(222), "<b>Siete rangos</b>, de lo general a lo particular. BioCLIP aprende con la cadena completa en el texto, pero no devuelve los siete rangos por sí solo: en Anura, género y familia salen de supercentroides.") +
     '</div></div>',
     "Elegir el rango taxonómico")

hoja(titulo("Una especie no es una sola apariencia") +
     '<p class="lead">Un individuo tiene un rango taxonómico, pero también una etapa y un sexo, y los tres cambian lo que se ve.</p>' +
     fig(C.matriz_eta_sexo(467), "<b>Especie × etapa × sexo</b> aplicado a un trips. Una sola etiqueta «especie» mezcla apariencias muy distintas: un único centroide queda en el medio y no representa a ninguna. Cada celda es una subclase con su propio prototipo.") +
     '<div class="c2">'
     f'<p>BioCLIP 2 reporta que la variación dentro de una especie (etapas, sexos) se conserva en el espacio de vectores, separada de la variación entre especies {E("FUENTE")}. Los autores aclaran que esa separación no está probada formalmente.</p>'
     '<h3>Tres maneras de modelarlo</h3>'
     '<ol><li>Una etiqueta compuesta «especie-etapa» como clase.</li><li>Un vector común y <b>cabezas separadas</b> por pregunta.</li><li>Prototipos por celda, con préstamo del global si hay menos de 3 individuos.</li></ol>'
     '<p>Elige según cuántas fotos haya por celda. Divide los datos por individuo y por sitio, y comprueba que cada etapa aparece en train, validación y test.</p>'
     '</div>' +
     tabla([["Campo", "Valores", "Si no se puede saber"],
            ["Taxón", "Familia, género o especie (el más fino confirmado)", "<code>no_determinable</code> + rango alcanzado"],
            ["Etapa", "Las del grupo: huevo, larva I, larva II, prepupa, pupa, adulto; BBCH en plantas", "<code>no_determinable</code>"],
            ["Sexo", "Macho, hembra, indiferenciado", "<code>no_determinable</code>"],
            ["Salud, calidad", "Sano o síntoma; nítida, borrosa, escala visible", "<code>no_determinable</code>"],
            ["Individuo, sitio, fecha, observador", "Identificadores", "—"]], [22, 50, 28], "sm"),
     "Una especie no es una sola apariencia")

hoja(titulo("Taxonomía y cómo identifican los expertos") +
     '<div class="c2">'
     '<p class="lead" style="font-size:10.6pt">Los expertos combinan varias evidencias. Una foto es solo una de ellas.</p>'
     '<h3>Morfología y claves</h3><p>Claves dicotómicas (dos opciones por paso hasta el nombre) y caracteres diagnósticos.</p>'
     f'<h3>ADN</h3><p>Código de barras: en animales, el gen COI (648 pares de bases); en plantas, rbcL + matK, a veces ITS2; en hongos, ITS {E("FUENTE")}.</p>'
     '<h3>Sonido</h3><p>Cantos de ranas y aves (Xeno-canto, Merlin).</p>'
     f'<h3>Ciencia ciudadana</h3><p>En iNaturalist, el «grado de investigación» exige que más de 2/3 de los identificadores coincidan a nivel de especie {E("FUENTE")}.</p>'
     '<h3>El nombre cambia</h3><p>Las sinonimias rompen datasets. En Anura, <i>D. labialis</i> = <i>D. molitor</i> contaminó una evaluación. <i>R. horribilis</i> se separó de <i>R. marina</i> en 2016 y <i>R. bella</i> se describió en 2024.</p>'
     '<h3>Cuándo la foto no basta</h3><p>Especies crípticas, partes que no se ven (vientre translúcido) y estadios distintos. Mostrar género o familia es mejor que adivinar.</p>'
     '</div><div class="sp"></div>' +
     tabla([["Grupo", "Ruta habitual", "Pista de apoyo"],
            ["Anfibios (anuros)", "Foto de cuerpo entero + vientre; canto", "Altitud, región, hora"],
            ["Reptiles", "Escamas, color, papada", "Región, microhábitat"],
            ["Aves", "Foto + canto", "Fecha y lugar (eBird)"],
            ["Mamíferos", "Cámaras trampa; detector primero", "Sitio"],
            ["Insectos", "Foto + estadio (huevo, larva, pupa, adulto)", "Planta hospedera"],
            ["Plantas", "Hoja, flor, fruto (varios órganos)", "Región, altitud"],
            ["Hongos", "Cuerpo fructífero; ADN", "Sustrato"]], [22, 46, 32]) +
     f'<p style="font-size:8.6pt;color:#333">AmphibiaWeb lista 9.081 anfibios y 8.011 anuros, en 57 familias y 504 géneros (7 ago 2026) {E("FUENTE")}.</p>',
     "Taxonomía y cómo identifican los expertos")

# =====================================================================================
# CAP 02 · EL MODELO
# =====================================================================================
apertura(2, "El modelo", ["BioCLIP y la", "ruta de metodo"],
         "Qué es, cuál elegir, dónde conseguirlo y cuándo no hay que entrenarlo.", ["BIOCLIP", "ONNX", "RUTA", "CONGELADO"], 91)

hoja(titulo("BioCLIP: qué es y cómo funciona") +
     '<div class="g2"><div>'
     f'<p><b>BioCLIP</b> es un modelo de visión y lenguaje para el árbol de la vida, de Imageomics (Ohio State; CVPR 2024; licencia MIT) {E("FUENTE")}. Es contrastivo, como CLIP: acerca el vector de una foto al vector del texto que la describe.</p>'
     '<h3>La idea clave</h3>'
     '<p>Cada foto se empareja con un texto que puede ser el nombre común, el científico o la <b>cadena taxonómica completa</b> (reino → especie). En una ablación en Rare Species: texto mixto 30,9; taxonómico + común 30,4; solo científico 22,3.</p>'
     '<p>Por eso los vectores de especies del mismo género quedan cerca, y el modelo funciona con especies raras o no vistas.</p>'
     '</div><div>' +
     fig(C.vbars([{"l": "BIOCLIP 1", "l2": "512-d", "v": 37.6, "t": "37,6"}, {"l": "BIOCLIP 2", "l2": "768-d", "v": 55.6, "t": "55,6"}, {"l": "BIOCLIP 2.5", "l2": "1024-d", "v": 61.3, "hi": 1, "t": "61,3"}], 100, 222, 150),
         "<b>Zero-shot, media de 10 tareas</b> (protocolo de las fichas de BioCLIP 2 y 2.5) " + E("FUENTE") + ". Son benchmarks, no tus especies.") +
     '</div></div>' +
     tabla([["", "BioCLIP 1", "BioCLIP 2", "BioCLIP 2.5 Huge"],
            ["Torre de imagen", "ViT-B/16", "ViT-L/14", "ViT-H/14"],
            ["Embedding", "512", "768", "1024"],
            ["Datos", "TreeOfLife-10M (~10,4 M imágenes, 454 mil taxones)", "TreeOfLife-200M (214 M imágenes, 952 mil taxones)", "TreeOfLife-200M ampliado (~19 M más)"],
            ["Parámetros (modelo completo)", "~150 M", "~428 M", "~986 M"],
            ["Tamaño FP16 " + E("CALC"), "0,30 GB", "0,86 GB", "1,97 GB"],
            ["Cómputo, torre de imagen", "35 GFLOPs", "162 GFLOPs", "335 GFLOPs"],
            ["Publicación", "CVPR 2024", "NeurIPS 2025", "Ficha en Hugging Face (2026)"]], [25, 25, 25, 25], "sm") +
     bocadillo("La mejora de 2.5 no se debe solo a los 1024 dimensiones: el modelo es ~6,6 veces más grande y vio ~20 veces más datos.", expresion="guino", forma="nube"),
     "BioCLIP: qué es y cómo funciona")

hoja(titulo("Conseguir BioCLIP y configurarlo") +
     '<p class="lead">Los tres modelos están en Hugging Face. Se cargan con OpenCLIP o con pybioclip, según lo que necesites.</p>'
     '<div class="c2">'
     '<h3>Dónde está</h3>'
     '<ul><li><code>imageomics/bioclip</code>: v1, ViT-B/16, MIT.</li><li><code>imageomics/bioclip-2</code>: ViT-L/14.</li><li><code>imageomics/bioclip-2.5-vith14</code>: ViT-H/14, MIT.</li></ul>'
     '<h3>Opción 1: OpenCLIP</h3>'
     '<p>Da el modelo, su preprocesado exacto y el tokenizador. Es la base para embeddings, centroides y exportación a ONNX.</p>'
     '<h3>Opción 2: pybioclip</h3>'
     '<p>Clasificadores listos: <code>TreeOfLifeClassifier</code> predice por rango (de reino a especie) y <code>CustomLabelsClassifier</code> usa tus propias etiquetas. Incluye la orden <code>bioclip predict</code>. Comprueba qué versiones de BioCLIP admite la versión que instales.</p>'
     '</div>'
     '<pre>pip install open_clip_torch pybioclip\n\nimport open_clip, torch\nfrom PIL import Image\nm, _, prep = open_clip.create_model_and_transforms("hf-hub:imageomics/bioclip")\nm.eval()\nwith torch.no_grad():\n    v = m.encode_image(prep(Image.open("foto.jpg")).unsqueeze(0))\nv = v / v.norm(dim=-1, keepdim=True)   # vector L2 para centroides o kNN</pre>' +
     tabla([["Necesidad", "Configuración"],
            ["Probar en una tarde", "<code>bioclip predict</code> o <code>CustomLabelsClassifier</code> con tus nombres: línea base zero-shot"],
            ["Tus especies con pocas fotos", "Embeddings congelados + un centroide por especie, etapa o sexo; kNN para comparar"],
            ["Móvil sin conexión", "Solo la torre de imagen de BioCLIP 1 en ONNX (opset 18, batch 1, FP16: 165,6 MB) + centroides en SQLite " + E("PROYECTO")],
            ["Servidor con GPU", "BioCLIP 2.5 (~2 GB en FP16) cargado una vez: <code>HF_HOME</code> fijo, <code>HF_HUB_OFFLINE=1</code>, proceso caliente, textos precalculados"],
            ["Compromiso", "BioCLIP 2 (ViT-L/14)"],
            ["Siempre", "Mismo preprocesado (224×224, media y desviación de OpenCLIP) y un <b>contrato de embedding</b>: hash del encoder + dimensión + preprocesado + normalización"]], [26, 74], "sm") +
     nota("Ojo:", "cambiar de versión de BioCLIP obliga a recalcular todos los vectores. Los vectores de dos versiones no son comparables."),
     "Conseguir BioCLIP y configurarlo")

hoja(titulo("Otras opciones y con qué compararlo") +
     tabla([["Modelo", "Qué es", "Cuándo usarlo", "Límite"],
            ["CLIP / OpenCLIP", "Visión y lenguaje general", "Base de comparación", "21,9 y 20,4 de media frente a 39,4 de BioCLIP 1 (protocolo del paper)"],
            ["SigLIP", "Visión y lenguaje general", "Comparación", "39,5 de media en el protocolo de las fichas (BioCLIP 1: 37,6)"],
            ["DINO / DINOv2", "Visión autosupervisada", "Vectores visuales sin texto", "El paper de BioCLIP solo compara con DINO v1"],
            ["BioTrove (BT-CLIP)", "CLIP biológico, 40 M de imágenes de entrenamiento", "Alternativa a BioCLIP", "Sin comparación directa encontrada"],
            ["SpeciesNet (Google)", "Más de 2.000 etiquetas, usa MegaDetector", "Cámaras trampa", "Cerrado a su catálogo"],
            ["MegaDetector", "Detecta animal, persona y vehículo", "Filtrar fotos vacías o localizar el animal", "No da especie"],
            ["Pl@ntNet", "Plantas; 1 a 5 fotos por consulta, cada una con su órgano", "Plantas", "Modelo propietario"],
            ["Merlin", "Foto y sonido con lugar y fecha de eBird, sin conexión", "Referencia de diseño de paquetes regionales", "Cerrado"]], [18, 28, 24, 30], "sm") +
     '<div class="sp"></div><div class="c2">'
     '<h2>Cuándo usar cada BioCLIP</h2>'
     '<p><b>Móvil sin internet:</b> BioCLIP 1, solo la torre de imagen en ONNX FP16. <b>Servidor con GPU:</b> BioCLIP 2.5, mayor precisión zero-shot. <b>Compromiso:</b> BioCLIP 2.</p>'
     '<p>En cualquier caso, <b>mide primero con tus fotos</b>: los benchmarks no son tus especies.</p>'
     '<h2>Las debilidades</h2>'
     '<p>BioCLIP 1 saca 6,1 en Plankton y apenas mejora a CLIP en PlantDoc (28,4 frente a 26,1). En enfermedades de plantas, un modelo de biodiversidad no sustituye a uno de enfermedades.</p>'
     '</div>',
     "Otras opciones")

hoja(titulo("Ruta de método, paso 0 a 5") +
     '<p class="lead">Con el mismo stack, la ruta depende de la pregunta y de cuántas fotos tengas.</p>' +
     fig(C.pipeline(467), "<b>Pipeline de referencia.</b> Resaltado: la línea base sin entrenar, que se mide antes de construir nada.") +
     '<div class="c2">'
     '<h3>Paso 0 · Define la pregunta</h3><p>Qué se distingue (especie, etapa, estado), cuántas clases, dónde corre (móvil, web, servidor) y qué error es peor: confundir dos clases parecidas o no reconocer nada.</p>'
     '<h3>Paso 1 · Mira los datos</h3>' +
     tabla([["Si tienes", "Empieza por"], ["&lt; 50 fotos por clase", "Embeddings + vecino más cercano"], ["50 a 500", "Capa lineal sobre el encoder congelado"],
            ["&gt; 500 y equilibrio", "Ajuste fino (con cuidado, ver 2.6)"], ["Clases que cambian", "Búsqueda por similitud"], ["Sin etiquetas", "Clustering y etiquetado asistido"]], [45, 55], "sm") +
     '<h3>Paso 2 · Escalera de métodos</h3><ol><li>Línea base sin entrenar (coseno).</li><li>Clasificador lineal sobre embeddings.</li><li>Ajuste de la última capa.</li><li>Ajuste fino completo.</li><li>Detección + clasificación.</li><li>Ensamble o modelo grande en servidor.</li></ol>'
     '<p>Sube un peldaño solo si el actual no alcanza la métrica y el coste lo justifica.</p>'
     '<h3>Paso 3 · Evalúa siempre igual</h3><p>Top-1, top-5, F1 por clase y matriz de confusión; división por individuo; prueba de campo; un umbral para decir «no sé».</p>'
     '<h3>Pasos 4 y 5</h3><p>No prometas un número antes de medirlo. Despliega según el dispositivo (capítulo 07).</p>'
     '</div>',
     "Ruta de método")

hoja(titulo("Fine-tuning o congelado") +
     '<p class="lead">Ajustar todos los pesos no es un error, pero es un riesgo. Con pocas fotos por especie, gana el encoder congelado.</p>'
     '<div class="g2"><div>' +
     fig(C.agrupadas([("FT", [85.1, 59.3]), ("LP", [82.9, 66.2]), ("LP-FT", [85.7, 68.9])], [("ID", "n"), ("OOD", "l")], 100, 222, 150),
         "<b>Kumar et al. 2022</b> " + E("FUENTE") + ": medias de 3 ejecuciones. FT = ajuste completo; LP = solo capa lineal; LP-FT = primero lineal, luego todo.",
         leyenda([("Dentro de distribución (6 conjuntos)", "n"), ("Fuera de distribución (10)", "l")])) +
     '</div><div>' +
     fig(C.vbars([{"l": "SIN ENTRENAR", "v": 70.4, "hi": 1}, {"l": "AJUSTE FINO", "v": 69.2}, {"l": "+ ALBUMENT.", "v": 19.7, "gris": 1}], 100, 222, 150),
         "<b>Anura, 28 especies</b> " + E("PROYECTO") + ": el ajuste no mejoró el top-1 y memorizó. Con una aumentación mal normalizada cayó a 19,7 %.") +
     '</div></div><div class="c2">'
     '<h3>Por qué pasa</h3><p>Al entrenar una cabeza nueva al azar, las capas bajas se mueven y distorsionan las características que el modelo ya traía. Con ~2.200 imágenes y 28,7 M parámetros descongelados, la pérdida de entrenamiento bajó de 0,92 a 0,01: memorización.</p>'
     '<h3>Por qué congelado</h3><p>Añadir una especie o una etapa nueva es calcular un vector, sin reentrenar. Los paquetes regionales y las versiones dependen de que el encoder no cambie. Es barato, determinista y no necesita GPU para mantenerlo.</p>'
     '<h3>Si aun así hace falta ajustar</h3><p>Primero capa lineal; luego LP-FT con tasa de aprendizaje baja o WiSE-FT (promediar pesos). Valida en sitios nuevos, recalcula todos los vectores y versiona.</p>'
     '</div>',
     "Fine-tuning o congelado")

verde("02", "Usa BioCLIP congelado por defecto y ajusta solo si demuestras que hace falta.",
      "<p>La medición propia dice que el ajuste no mejora el top-1 y memoriza. La literatura lo respalda: el ajuste completo rinde peor fuera de distribución.</p>"
      "<p>Regla de la ruta: ajuste fino completo solo con más de 500 imágenes por clase y buen equilibrio.</p>", 77)

# =====================================================================================
# CAP 03 · LOS DATOS
# =====================================================================================
apertura(3, "Los datos", ["Los datos pesan", "mas que el modelo"],
         "Dónde conseguir fotos, cuántos individuos hacen falta y cómo no engañarte al medir.", ["SCRAPING", "INDIVIDUOS", "ETIQUETAS", "DIVISIÓN"], 63)

hoja(titulo("De dónde sacar imágenes de cualquier animal") +
     '<p class="lead">Casi todo empieza en iNaturalist y GBIF. Lo que decide la calidad es guardar los metadatos de cada foto y no mezclar fuentes duplicadas.</p>' +
     tabla([["Fuente", "Qué da", "Cómo se accede", "Cuidado"],
            ["iNaturalist", "Fotos con observación, lugar, fecha, autor, licencia y grado de investigación", "API v1 (<code>/v1/observations</code>: <code>taxon_name</code>, <code>quality_grade=research</code>, <code>photos=true</code>, <code>photo_license</code>, hasta 200 por página); cliente <code>pyinaturalist</code>; volcado abierto en AWS (<code>inaturalist-open-data</code>)", "Cuotas de peticiones y de descarga; en insectos las etiquetas son las menos fiables"],
            ["GBIF", "Registros de muchas colecciones, incluido iNaturalist", "API <code>occurrence/search</code> con <code>mediaType=StillImage</code>; descargas grandes con cuenta y DOI citable; <code>pygbif</code>", "Duplica registros de iNaturalist"],
            ["Wikimedia Commons", "Fotos curadas con autor y licencia", "API de MediaWiki por categoría (<code>imageinfo</code> con URL y metadatos)", "Pocas fotos por especie"],
            ["Conjuntos armados", "iNat2021 (10.000 especies), TreeOfLife-10M, BIOSCAN-5M (insectos), IP102 (plagas), Pl@ntNet-300K, PlantVillage", "Hugging Face o la página del conjunto", "Licencia de cada uno; el test de laboratorio engaña"],
            ["Xeno-canto", "Cantos", "API v3 con clave", "La API v2 se retiró"],
            ["Fotos propias", "Etapas raras (huevo, pupa) y tu región", "Protocolo de captura con escala", "Cara, pero la más útil"]], [14, 27, 37, 22], "sm") +
     '<div class="c2">'
     '<h3>Antes de descargar</h3>'
     '<p>Haz la lista de taxones con sus <b>sinónimos</b>: un nombre viejo esconde fotos y un sinónimo mezcla especies.</p>'
     '<p>Elige licencias que puedas usar: CC0 y CC BY; CC BY-NC solo si el uso no es comercial. Cita siempre al autor.</p>'
     '<h3>Lo que tarda</h3>'
     f'<p>En Anura {E("PROYECTO")}: GBIF ≈7 s por especie; iNaturalist 5–10 min por especie (40 individuos nuevos, 3 fotos por individuo).</p>'
     '</div>' +
     bocadillo("En iNaturalist la URL de la foto cambia de tamaño reemplazando <b>square</b> por <b>medium</b>, <b>large</b> u <b>original</b>.", expresion="guino", forma="gota"),
     "De dónde sacar imágenes")

hoja(titulo("Cómo scrapear sin romper nada") +
     '<p class="lead">Ocho pasos. Los dos resaltados son los que más evaluaciones han arruinado cuando se saltan.</p>' +
     fig(C.scraping(467)) +
     '<div class="c2">'
     '<h3>1 · Taxones y sinónimos</h3><p>Usa el backbone de GBIF o el catálogo del grupo.</p>'
     '<h3>2 · Siempre por API</h3><p>Nunca leas el HTML de la web. Una especie a la vez, con un <code>User-Agent</code> que te identifique, una pausa entre peticiones y reintentos con espera creciente. La documentación de iNaturalist pide alrededor de una petición por segundo y menos de 10.000 al día; comprueba las cuotas actuales.</p>'
     '<h3>3 · Metadatos antes que fotos</h3><p><code>obs_id</code>, <code>photo_id</code>, URL, licencia, autor, coordenadas y su precisión, fecha y grado de calidad.</p>'
     '<h3>4 · Filtra</h3><p>Licencias, coordenadas imprecisas (Anura descartó registros con hasta 7.270 km de error), animales cautivos y fotos de manejo.</p>'
     '<h3>5 · Descarga</h3><p>Con cola, límite de velocidad y reanudación (<code>img2dataset</code> o un script propio). Comprueba que cada archivo abre.</p>'
     '<h3>6 · Deduplica</h3><p>Por hash exacto, por hash perceptual (pHash) <b>y por observación</b> entre fuentes.</p>'
     '<h3>7 · Divide por individuo</h3><p>Antes de aumentar, y congela el test.</p>'
     '<h3>8 · Versiona</h3><p>Fecha, consulta exacta y conteos por especie y etapa.</p>'
     '</div>'
     '<pre>import requests, time\nURL = "https://api.inaturalist.org/v1/observations"\nq = {"taxon_name": "Frankliniella", "quality_grade": "research", "photos": "true",\n     "photo_license": "cc0,cc-by,cc-by-nc", "per_page": 200, "page": 1}\nr = requests.get(URL, params=q, headers={"User-Agent": "guia-ia/1.0 (correo@ejemplo)"}).json()\nfor o in r["results"]:\n    for f in o["photos"]:\n        print(o["id"], f["id"], f["license_code"], f["url"].replace("square", "medium"))\ntime.sleep(1)   # una petición por segundo</pre>' +
     nota("Cuidado.", "Las coordenadas de especies amenazadas vienen ofuscadas, y así deben quedar en tu base."),
     "Cómo scrapear")

hoja(titulo("Individuos frente a fotos") +
     '<p class="lead">Lo que estabiliza un centroide es la variación <b>entre individuos</b>, no el número de fotos del mismo animal.</p>' +
     fig(C.individuos(467), "<b>Ilustración.</b> Las dos muestras tienen 20 fotos. Con un solo individuo, el modelo aprende ese animal, su fondo y su luz; con diez, aprende la especie.") +
     '<div class="g2"><div>' +
     tabla([["Nivel", "Fotos", "Individuos"], ["Mínimo viable", "10–15", "3–5"], ["Recomendado", "30–50", "8–12"], ["Robusto", "80–100+", "15+"],
            ["Piso de un paquete (v5)", "≥ 80", "≥ 10"], ["Identificación entrenada", "—", "≥ 70"]], [50, 25, 25], "sm") +
     f'<p class="pie">Reglas de Anura por clase {E("PROYECTO")}.</p></div><div>'
     f'<p>Con 38 individuos o más, añadir fotos ya no ayudó: la correlación entre el acierto y el número de individuos fue −0,05 (56 especies) {E("PROYECTO")}.</p>'
     '<p>Lo que más explica el error es lo cerca que está la especie vecina (correlación −0,62).</p>'
     '<p>Para etapa y sexo vale lo mismo, celda por celda: muchos individuos distintos en cada etapa.</p>'
     '</div></div>' +
     nota("Para recordar.", "100 fotos de un individuo enseñan un individuo. 20 individuos × 5 fotos enseñan la especie. Pide variedad: animales, sitios, luces y fondos distintos."),
     "Individuos frente a fotos")

hoja(titulo("Sobreajuste y subajuste") +
     '<p class="lead">El modelo puede quedarse corto (subajuste) o aprenderse de memoria las fotos de entrenamiento (sobreajuste). La curva de validación lo delata.</p>' +
     fig(C.curvas_ajuste(467), "<b>Ilustración.</b> El error de entrenamiento (línea continua) siempre baja; el de validación (discontinua) baja, toca fondo y sube. El mejor modelo es el de la parada temprana.") +
     tabla([["", "Señal", "Ejemplo", "Remedio"],
            ["<b>Subajuste</b>", "Error alto en entrenamiento y en validación", "Zero-shot con nombres que el modelo no conoce; una cabeza demasiado simple", "Centroides o capa lineal sobre embeddings; más épocas; LP-FT si hay muchos datos"],
            ["<b>Punto justo</b>", "Validación en su mejor valor", "Anura, fase 4: pico de validación 72,7 % en la época 10", "Parada temprana: guarda ese punto"],
            ["<b>Sobreajuste</b>", "Entrenamiento baja; validación sube o se estanca", "Anura: pérdida 0,92 → 0,01; test 69,2 % frente a 70,4 % sin entrenar", "Congelar el encoder, más individuos, aumentación moderada, regularización, menos épocas"]], [14, 24, 31, 31], "sm") +
     '<div class="c2">'
     '<h3>La trampa que lo esconde</h3><p>Dividir al azar en vez de por individuo o sitio. Las fotos del mismo animal en train y test inflan la métrica: en la Fase 13 de Anura, el 100 % de las imágenes de prueba ya estaban en el entrenamiento.</p>'
     '<h3>Cómo evitar los dos</h3><ul><li>Divide por individuo y por sitio.</li><li>Mide la línea base sin entrenar.</li><li>Mira train y validación juntas.</li><li>Prefiere más individuos a más fotos.</li><li>Prueba la aumentación sola antes de entrenar.</li></ul>'
     '</div>',
     "Sobreajuste y subajuste")

hoja(titulo("Etiquetar bien") +
     '<p class="lead">Una etiqueta mala no se arregla con más datos: el modelo la aprende.</p>'
     '<div class="c2">'
     f'<p>Al menos un 3,3 % de errores de etiqueta de media en 10 conjuntos de prueba, y al menos un 6 % en la validación de ImageNet (Northcutt et al. 2021) {E("FUENTE")}. La herramienta <i>confident learning</i> (cleanlab) estima las etiquetas sospechosas.</p>'
     '<p>En iNaturalist, una estimación informal de su personal (2019) daba ~85 % de grado de investigación correcto: 91 % en aves y 65 % en insectos. En insectos las etiquetas públicas son las menos fiables.</p>'
     f'<h3>Errores reales de Anura {E("PROYECTO")}</h3>'
     '<ul><li>Siete correcciones de nomenclatura y carpetas con errores de tipeo.</li><li><i>D. labialis</i> = <i>D. molitor</i>: el 79,1 % era la misma observación.</li><li>El <code>individual_id</code> era el de la observación, no un animal verificado.</li><li>La búsqueda de negativos difíciles elige una y otra vez el error cuando hay etiquetas sucias.</li></ul>'
     '</div><h2>Protocolo mínimo</h2>' +
     tabla([["#", "Paso"], ["1", "Guía de anotación escrita con ejemplos de cada valor y de cada <code>no_determinable</code>"],
            ["2", "Ante la duda entre marcar algo y <code>no_determinable</code>, gana <code>no_determinable</code>; ante desacuerdo en una escala, el valor más conservador"],
            ["3", "Dos anotadores sobre una muestra y medir el acuerdo (kappa de Cohen)"], ["4", "Un experto para la especie (en trips, microscopio)"],
            ["5", "Versionar la taxonomía y guardar sinónimos"], ["6", "Detectar duplicados por hash y por observación"],
            ["7", "Revisar los casos de mayor pérdida antes de reentrenar"], ["8", "Congelar el test antes de mirar resultados"]], [6, 94], "sm"),
     "Etiquetar bien")

hoja(titulo("Pocas imágenes: aumentación y alternativas") +
     '<p class="lead">Si faltan fotos, baja peldaño a peldaño, de lo más barato a lo más costoso.</p>' +
     fig(C.escalera(467), "<b>Escalera si no hay suficientes imágenes.</b> Las cifras del primer peldaño son de BioCLIP 1 (media de 10 tareas), no de trips.") +
     '<div class="c2">'
     f'<h3>Aumentación usada en Anura {E("PROYECTO")}</h3>'
     '<p><b>Moderada</b> (individuos reales): recorte 0,6–1,0; volteos; rotación ±20°; brillo y contraste 0,25; saturación 0,15; matiz 0,05; borrado aleatorio p=0,2. <b>Agresiva</b> solo en las repeticiones de especies con menos de 70 individuos.</p>'
     '<p>Validación y test sin aumentación. La aumentación va <b>solo en train y al vuelo</b>, nunca antes de dividir.</p>'
     '<h3>Qué no romper</h3>'
     '<ul><li><b>Color diagnóstico:</b> matiz ≤ ±10 a 15°.</li><li><b>Tamaño y proporción:</b> si la etapa se distingue por tamaño, evita zoom fuerte o deja una escala en la foto.</li><li><b>Rotación y volteo:</b> válidos para insectos vistos desde arriba.</li><li><b>Fondo:</b> varía hoja, trampa y mano para que no aprenda el fondo.</li></ul>'
     '<h3>Pesos de clase</h3><p>Usa la raíz cuadrada de la frecuencia inversa: multiplicar ×6 el gradiente de una clase de 11 individuos fuerza a memorizar.</p>'
     '</div>',
     "Pocas imágenes")

# =====================================================================================
# CAP 04 · CASO REAL
# =====================================================================================
apertura(4, "Caso real", ["Anuros de", "Colombia"],
         "56 especies, 5.818 fotos y 3.240 individuos: lo que se midió y lo que falló.", ["TOP-1", "TOP-3", "RECHAZO", "ERRORES"], 53)

hoja(titulo("Tablero: identificación") +
     '<div class="mets">' + met("Top-1 · 56 especies", "62,9%", "test v5, 864 fotos, centroides", "l") + met("Top-3", "86,1%", "mostrar tres candidatas: +23 pp", "n") +
     met("Dataset v5", "56", "especies · 5.818 fotos · 3.240 individuos", "g") + '</div>'
     '<div class="g2"><div><p class="kick">Acierto con 56 especies</p>' +
     fig(C.vbars([{"l": "TOP-1", "v": 62.85, "hi": 1, "err": 3.2, "t": "62,85%"}, {"l": "TOP-3", "v": 86.11, "t": "86,11%"}, {"l": "TOP-5", "v": 91.09, "t": "91,09%"}], 100, 222, 150),
         E("CALC") + " Barra de error: intervalo del 95 % (±3,2 pp).") +
     '</div><div><p class="kick">Más especies, menos acierto</p>' +
     fig(C.linea([(5, 87.3), (18, 78.2), (26, 76.0), (31, 68.6), (56, 64.4)], (0, 60), (60, 100), "especies en el modelo", "% entre aceptadas", 222, 150),
         E("PROYECTO") + " Validación por lotes; no es un experimento controlado, pero la tendencia es real.") +
     '</div><div><p class="kick">Paquete regional frente a global · Sinú</p>' +
     fig(C.vbars([{"l": "GLOBALES", "v": 73.83, "hi": 1, "err": 3.9, "t": "73,83%"}, {"l": "REGIONALES", "v": 70.99, "err": 4.0, "t": "70,99%"}], 100, 222, 150),
         "33 especies, 493 fotos. Los intervalos se solapan: el centroide regional no mejora.") +
     '</div><div><p class="kick">Quitar el fondo empeora</p>' +
     fig(C.vbars([{"l": "COMPLETA", "v": 60.7, "hi": 1}, {"l": "RECORTE", "v": 50.7}, {"l": "FONDO NEGRO", "v": 44.7}], 100, 222, 150),
         "150 imágenes pareadas con BioCLIP. Reentrenar sobre recortes no se probó.") +
     '</div></div>',
     "Tablero: identificación")

hoja(titulo("Tablero: rechazo y especies gemelas") +
     '<div class="g2"><div><p class="kick">Rechazar ranas ajenas · Sinú</p>' +
     fig(C.linea([(78.5, 61.3, "78,5"), (81.5, 68.2, "81,5"), (86.4, 75.1, "86,4"), (95.3, 91.6, "95,3"), (98.8, 97.6, "98,8")], (75, 100), (40, 100), "% de conocidas aceptadas (KAR)", "% de ajenas que se cuelan", 222, 160),
         "Aceptar más conocidas deja pasar más ajenas: de 90 a 95 % de KAR, el FAR sube ~16 puntos.") +
     '</div><div><p class="kick">AUROC del rechazo · 0,5 = azar</p>' +
     fig(C.vbars([{"l": "SABANAS", "l2": "MAHAL.", "v": .576, "t": "0,576"}, {"l": "SABANAS", "l2": "COSENO", "v": .826, "hi": 1, "t": "0,826"}, {"l": "SINÚ", "l2": "MAHAL.", "v": .578, "t": "0,578"}, {"l": "SINÚ", "l2": "COSENO", "v": .665, "hi": 1, "t": "0,665"}], 1, 222, 160, ""),
         "Coseno + Weibull separa mejor que Mahalanobis, pero en el Sinú sigue débil.") +
     '</div></div><p class="kick">Errores entre especies parecidas (top-1 equivocado, test)</p>' +
     fig(C.hbars([{"l": "D. bogerti → D. microcephalus", "v": 8, "hi": 1}, {"l": "R. marina → R. horribilis", "v": 7, "hi": 1}, {"l": "H. tatayoi → E. prosoblepon", "v": 5},
                  {"l": "D. columbianus → D. bogerti", "v": 5}, {"l": "C. metriosistus → C. raniformis", "v": 5}, {"l": "O. taurinus → T. macrotis", "v": 4},
                  {"l": "N. grandisonae → E. prosoblepon", "v": 4}, {"l": "R. humboldti → R. beebei", "v": 4}], 9, 467, 150),
         "Casi siempre del mismo género. Cuanto más cerca está la especie vecina, peor el acierto (−0,62).") +
     '<div class="c2"><p>«No es una rana» se rechaza bien: solo el 4,6 % de las fotos de otra cosa se cuela (AUROC 0,989). Lo que se cuela son reptiles y salamandras.</p>'
     '<p>El rechazo de <b>ranas ajenas</b> sigue sin resolverse: FAR de 61 a 92 %. El cuello de botella son pares casi idénticos en el espacio de vectores.</p></div>',
     "Tablero: rechazo")

hoja(titulo("Errores y lecciones") +
     '<p class="lead">Quince lecciones de un proyecto real. Casi todas valen para cualquier grupo.</p>' +
     tabla([["#", "Lección", "Evidencia"],
            ["1", "Mide una línea base sin entrenar antes de construir nada", "70,4 % sin entrenar frente a 69,2 % con ajuste"],
            ["2", "Quitar el fondo no ayudó", "60,7 → 50,7 → 44,7 %"],
            ["3", "El contexto geográfico es la mayor ganancia y el mayor riesgo", "+15 a +25 pp; volteó una identificación correcta"],
            ["4", "Filtrar por región mejora la precisión", "kNN regional +11,8 pp"],
            ["5", "Los ViT no se cuantizan a INT8 sin reentrenar", "Cinco intentos: 0,2–51 %"],
            ["6", "La destilación a un modelo pequeño falló", "57,7 → 24,3 %"],
            ["7", "Mahalanobis con covarianza compartida degradó el rechazo", "AUROC 0,69 → 0,59"],
            ["8", "El rechazo de desconocidos no está resuelto", "FAR 52–94 %"],
            ["9", "Una evaluación se contamina sin querer", "Fase 13: 100 % del test en train"],
            ["10", "Un score perfecto suele ser una trampa", "AUROC 1,0 ajustado sobre los mismos datos"],
            ["11", "Separa «no es una rana» de «rana que no conozco»", "La primera se separa limpio; la segunda no"],
            ["12", "La exportación a ONNX falla en silencio", "Un archivo de 1,2 MB sin error"],
            ["13", "Las especies raras se salvan con el nivel taxonómico", "27 de 28 cubiertas por género o familia"],
            ["14", "La documentación se desincroniza", "«BioCLIP 2.5 no existe» era falso"],
            ["15", "Reporta siempre con condiciones", "Especies, división, n y versión"]], [5, 55, 40], "sm") +
     bocadillo("Una decisión costó días: esperar a la segmentación antes de entrenar. El experimento que lo descartaba duraba 7 minutos de GPU.", expresion="serio", forma="cubo"),
     "Errores y lecciones")

hoja(titulo("Lo que falló: fondo, destilación y cuantización") +
     '<div class="c2">'
     '<h2>Quitar el fondo</h2>'
     '<p>Se esperaba que recortar la rana quitara el atajo del sustrato. Pasó lo contrario: completa 60,7 %, recorte 50,7 %, fondo negro 44,7 %.</p>'
     '<p>Causa probable: cambio de dominio. BioCLIP nunca vio fondos artificiales, y la rana ocupaba solo el 6–18 % del encuadre, así que el recorte reescalado quedaba borroso. Los modelos sí aprovechan el fondo: fondos adversariales rompen hasta el 87,5 % de los aciertos (Xiao et al.).</p>'
     '<p><b>Lo que quedó:</b> la segmentación explica después; no decide.</p>'
     '<h2>Destilación</h2>'
     '<p>Un modelo pequeño (alumno) aprende a imitar a uno grande (maestro). De BioCLIP a MobileNetV3: 57,7 → 24,3 % (−33,4 pp). El alumno tenía que aprender «qué es una rana» y «cuál rana» a la vez. Sí se transfirió la coherencia taxonómica.</p>'
     '<p>Ejemplo seguro de destilación: los modelos <i>DeepSeek-R1-Distill</i>, ajustados con ~800 mil muestras generadas por R1.</p>'
     '<h2>De FP32 a FP16</h2>'
     '<p>Torre de imagen exportada con <code>torch.onnx.export</code>, opset 18, batch 1 y FP16: 165,6 MB, predicciones idénticas (64 imágenes) y coseno 0,999999. Sin ganancia de velocidad en CPU, pero la mitad de tamaño.</p>'
     '<h2>Por qué no INT8</h2>'
     '<p>Los ViT tienen valores atípicos en las activaciones tras LayerNorm y softmax que una escala entera no representa (PTQ4ViT, RepQ-ViT). Cinco intentos dieron entre 0,2 y 51 %.</p>'
     '</div>',
     "Lo que falló")

# =====================================================================================
# CAP 05 · CONTEXTO
# =====================================================================================
apertura(5, "Contexto", ["Cuando la imagen", "ya no alcanza"],
         "Lugar, altitud, fecha, hospedero y época reordenan candidatas. Nunca deciden solos.", ["LUGAR", "HOSPEDERO", "ÉPOCA", "ACOTADO"], 41)

hoja(titulo("El contexto dinámico") +
     '<p class="lead">El prior geográfico y los demás datos de contexto deben ser dinámicos: hay especies endémicas y otras presentes en todas partes.</p>'
     '<div class="g2"><div>'
     f'<p>Mac Aodha et al. 2019 {E("FUENTE")}: P(clase | imagen, lugar) ∝ P(clase | imagen) · P(clase | lugar). En iNat2018 el top-1 pasa de 60,2 a <b>72,7</b>; en un conjunto sin estructura geográfica no ayuda.</p>'
     '<p>SINR (Cole et al. 2023) aprende un mapa por especie: con 10 ejemplos por especie ya supera a una cuadrícula con todos los datos.</p>'
     '<p>Ningún método publicado trata endémicas y amplias con un parámetro explícito. Lo de abajo es una propuesta apoyada en Anura.</p>'
     '</div><div>' +
     fig(C.prior(222), "<b>Ilustración.</b> La anchura sale de la dispersión real de cada especie. El multiplicador queda entre 0,5 y 1,5.",
         leyenda([("Endémica", "l"), ("Amplia", "g")])) +
     '</div></div>' +
     tabla([["#", "Regla del diseño dinámico"],
            ["1", "Escala por especie calculada de los datos (dispersión de distancias y altitud), nunca fija"],
            ["2", "Perfiles de peso editables: generalista 80/10/10, microendémica 30/60/10, par críptico 35/35/30, de quebrada 50/20/30"],
            ["3", "Suavizado hacia lo uniforme cuando hay pocas observaciones"],
            ["4", "Prior acotado: nunca elimina una especie; la oficial sale del voto visual"],
            ["5", "«No observado» no es «ausente»: tres estados, no un sí o no"],
            ["6", "Recalcular en cada versión; cada peso con tres valores: calculado, manual y efectivo"],
            ["7", "Vigilar sesgos: más registros cerca de ciudades, coordenadas imprecisas, especies invasoras"],
            ["8", "Evaluar sin la especie real como entrada y comprobar que no voltea aciertos visuales"]], [6, 94], "sm") +
     nota("Ojo:", "en Anura un prior sin acotar volteó una <i>D. bogerti</i> bien identificada a <i>D. truncatus</i>. Desde entonces el prior solo reordena."),
     "El contexto dinámico")

hoja(titulo("Especies casi idénticas") +
     '<p class="lead">Muchas especies de anuros se ven casi iguales aunque sean distintas. El par que más se confunde en Anura es este.</p>'
     '<div class="g2">' +
     foto("dimorfismo/rhinella_marina_hembra.jpg", 150, "<b><i>Rhinella marina</i></b>, hembra. Bernard Dupont, CC BY-SA 2.0.") +
     foto("pares/rhinella_horribilis_1.jpg", 150, "<b><i>Rhinella horribilis</i></b>. Foto del proyecto Anura.") +
     '</div><div class="c2">'
     f'<p>Coseno entre sus centroides: <b>0,980</b>, el par más cercano de las 56 especies. Sus altitudes se solapan (25–2.500 m frente a 4,5–2.467 m): ni la geografía ni la altitud las separan {E("PROYECTO")}.</p>'
     '<p>La diversidad críptica es enorme: <i>Engystomops</i> pasó de 2 especies a 5–7 y <i>Boana</i> de 2 a 6–9 (Funk et al. 2012).</p>'
     '<h3>Qué las separa</h3>'
     f'<p>En <i>Pristimantis</i> y <i>Dendropsophus</i> hay caracteres diagnósticos con fuente {E("FUENTE")}: el iris, los colores ocultos de la ingle y el muslo, la membrana entre los dedos y, sobre todo, el <b>canto</b> y el ADN (16S).</p>'
     '<p>Esos rasgos solo ayudan si la foto los muestra. Si no se ven, pide otra foto o un canto antes de dar la especie.</p>'
     '</div>' +
     nota("Truco.", "Documenta los pares conflictivos y avisa al usuario: «grupo <i>R. marina</i>/<i>R. horribilis</i>, requiere un detalle». Es mejor que un top-1 al azar."),
     "Especies casi idénticas")

hoja(titulo("Etapa, sexo y edad") +
     '<p class="lead">La etapa tiene escalas estándar para etiquetar; el sexo depende de la especie; la edad casi nunca sale de una foto.</p>' +
     fig(C.gosner_bbch(467), "<b>Gosner (1960)</b> y <b>BBCH (Meier 2001)</b>, leídos en el original. Los estadios 26–40 de Gosner son la mejor ventana para fijar la etapa en foto; los 21–25 son «difíciles para la identificación de especies».") +
     '<div class="fotos" style="grid-template-columns:repeat(4,1fr)">' +
     foto("renacuajos/bufo_02_renacuajos.jpg", 70, "Renacuajo. A. Karwath, CC BY-SA 2.5.") +
     foto("renacuajos/bufo_03_renacuajos_patas_traseras.jpg", 70, "Patas traseras. C. Fischer, CC BY-SA 3.0.") +
     foto("renacuajos/bufo_04_metamorfo_con_cola.jpg", 70, "Metamorfo. J. Lindsey, CC BY-SA 3.0.") +
     foto("renacuajos/bufo_05_juvenil.jpg", 70, "Juvenil. Syrio, CC BY-SA 4.0.") +
     '</div><div class="c2">'
     '<h3>Sexo en anuros</h3><p>Las hembras suelen ser más grandes. Rasgos útiles: saco vocal, almohadillas nupciales y amplexo, todos dependientes de la especie y la época. En <i>R. marina</i> el macho adulto es más pequeño y amarillento; un macho inmaduro también es manchado, así que el color solo no sexa.</p>'
     '<h3>Edad</h3><p>En anuros se cuentan líneas de crecimiento en las falanges; la talla no es fiable. Una guía solo puede ofrecer <b>clases de edad</b>: cría, joven, adulto.</p>'
     '</div>',
     "Etapa, sexo y edad")

hoja(titulo("Enfermedad en fauna y flora") +
     '<p class="lead">Una foto muestra síntomas, no la causa. Un buen resultado dice «lesión compatible con X; otras causas posibles; confirmar con laboratorio».</p>'
     '<div class="g2"><div>' +
     fig(C.vbars([{"l": "LABORATORIO", "v": 99.35, "hi": 1, "t": "99,35%"}, {"l": "CAMPO 1", "v": 31.40, "t": "31,40%"}, {"l": "CAMPO 2", "v": 31.69, "t": "31,69%"}], 100, 222, 150),
         "<b>PlantVillage</b> (Mohanty 2016): 99,35 % en su test y ~31 % con fotos externas.") +
     '</div><div>'
     '<h3>Qué ayuda en plantas</h3><p>Clasificar <b>lesiones individuales</b> subió la exactitud media un 12 % (Barbedo 2019). También ayudan varias fotos, varios órganos y el contexto de lugar y cultivo.</p>'
     '<h3>Hongos</h3><p>Nunca uses una foto para decidir si algo se come: la mejor de tres apps acertó el 49 % y confundió <i>Amanita phalloides</i>.</p>'
     '</div></div>' +
     tabla([["Grupo", "Signos visibles", "Confirmación"],
            ["Anuros", "Letargo, muda anormal, enrojecimiento, edema: inespecíficos (quitridio, ranavirus, <i>Aeromonas</i>)", "qPCR, histología. Sin ML publicado para fotos"],
            ["Aves", "Viruela aviar, conjuntivitis", "Laboratorio"],
            ["Mamíferos", "Sarna, nariz blanca en murciélagos", "Laboratorio; algunas solo post mortem"],
            ["Peces", "Puntos blancos de ich", "Microscopio"],
            ["Abejas", "Varroa, loque, cría de tiza", "Laboratorio; varroa F1 0,874"],
            ["Plantas", "Manchas, clorosis, marchitez, roya, mildiu, daño de plagas", "PCR o cultivo; extensionista"]], [14, 52, 34], "sm") +
     nota("Cuidado.", "algunas enfermedades animales son de notificación obligatoria (lista de la WOAH). La guía da pistas; el diagnóstico es de un profesional."),
     "Enfermedad en fauna y flora")

hoja(titulo("Del animal a la flora") +
     '<p class="lead">La guía es de animales, pero la teoría se traslada a las plantas con pocos cambios.</p>' +
     tabla([["En animales", "En flora", "Particularidad"],
            ["Rango fácil de separar", "Familia o género con rasgo visible", "Las claves usan flor y fruto: varios órganos ayudan"],
            ["Etapa (renacuajo, larva)", "BBCH: germinación → senescencia", "Diez estadios principales verificados"],
            ["Sexo", "Flores masculinas, femeninas o hermafroditas; dioicas", "Solo el principio"],
            ["Edad", "Anillos", "Requiere muestra"],
            ["Salud", "Síntomas en hoja, rama o planta", "99,35 % en laboratorio → ~31 % en campo"],
            ["Foto mala", "Pedir otro órgano o cambiar a «estado de la planta»", "Cascada de preguntas"],
            ["Prior de lugar", "Región, altitud, cultivo y hospedero", "EPPO, CABI, Plantwise"],
            ["Plaga como contexto", "Insecto vector → enfermedad que transmite", "Trips y TSWV (capítulo 06)"],
            ["Pocas imágenes", "Los mismos métodos", "Pl@ntNet-300K, PlantVillage"]], [24, 38, 38]) +
     '<div class="sp"></div><div class="c2">'
     '<p>Para plantas, los modelos de biodiversidad ayudan menos que uno de enfermedades: BioCLIP 2 saca 40,4 en PlantDoc.</p>'
     '<p>Pl@ntNet acepta de 1 a 5 fotos de la misma planta, cada una con su órgano. En otro estudio con 101 especies, el top-1 subió del 77 % (planta entera) al 97 % fusionando todas las vistas.</p>'
     '</div>',
     "Del animal a la flora")

hoja(titulo("Método por organismo y por pregunta") +
     '<p class="lead">La tabla de decisión: tu organismo, tu pregunta y el método que la evidencia respalda.</p>' +
     tabla([["Organismo", "Especie", "Etapa", "Sexo", "Edad", "Salud", "Método principal", "Contexto"],
            ["Anuros", "<b>F</b> (62,9 %)", "P", "P", "L", "P / L", "Embeddings + centroides, paquete regional", "Lugar, altitud, canto"],
            ["Aves", "F", "F", "P", "P", "P", "Foto + canto", "Fecha y lugar"],
            ["Mamíferos", "F", "P", "P", "P", "P / L", "Detector → clasificador", "Sitio"],
            ["Reptiles", "P", "P", "P / L", "L", "—", "Foto + caracteres", "Localidad"],
            ["Peces", "P", "—", "—", "—", "P", "Foto en acuario o cultivo", "Hábitat"],
            ["Insectos", "P", "F", "P", "—", "—", "Foto + hospedero", "EPPO, CABI"],
            ["Plantas", "F", "F", "P", "L", "P / L", "Foto de varios órganos", "Región"],
            ["Hongos", "P", "P", "—", "—", "—", "Foto + ADN", "Sustrato"]], [12, 10, 7, 7, 7, 9, 27, 21], "sm") +
     '<p style="font-size:8.2pt;color:#333"><b>F</b> factible desde una foto · <b>P</b> parcial · <b>L</b> requiere laboratorio · — sin evidencia encontrada.</p>'
     '<div class="sp2"></div><h2>Cómo elegir</h2>'
     '<div class="c2"><ol><li>¿Qué quieres saber: especie, etapa, sexo, edad o salud?</li><li>¿La respuesta es visible? Si no, laboratorio o clase de edad.</li>'
     '<li>¿Cuántas clases y cuántas fotos? Sigue la ruta de método.</li><li>¿La foto alcanza? Si no, pide otra o cambia de pregunta.</li>'
     '<li>¿Hay especies gemelas? Documenta los pares, usa contexto acotado y baja de rango.</li></ol></div>',
     "Tabla de decisión")

# =====================================================================================
# CAP 06 · FRANKLINIELLA
# =====================================================================================
apertura(6, "Frankliniella", ["Caso conductor:", "los trips"],
         "Reconocer la etapa de vida en una foto y recomendar el manejo adecuado.", ["HUEVO", "LARVA", "PUPA", "ADULTO"], 29)

hoja(titulo("El ciclo de vida del trips") +
     '<p class="lead">La etapa decide qué se ve en una foto y qué control llega al insecto.</p>' +
     fig(C.ciclo_trips(467), "<b><i>Frankliniella occidentalis</i></b>. Lima: etapas que se ven con macro. Negro: ocultas en el tejido o en el suelo. Fuentes: UF/IFAS (IN1089) y EPPO.") +
     tabla([["Etapa", "Tamaño y color", "Dónde está", "¿Se ve en foto?"],
            ["Huevo", "Dentro del tejido vegetal", "Hojas, pétalos", "Casi nunca; solo por el daño"],
            ["Larva I", "&lt; 1 mm (~0,56 mm), incolora o blanca", "Hojas y flores", "Sí, con macro"],
            ["Larva II", "~0,86–1 mm, amarillo dorado", "Hojas y flores", "Sí, con macro"],
            ["Prepupa", "Esbozos alares cortos; antenas hacia delante", "Suelo; a veces dentro de la flor", "Difícil"],
            ["Pupa", "Esbozos largos; antenas dobladas hacia atrás", "Suelo; a veces dentro de la flor", "Difícil"],
            ["Adulto", "&lt; 2 mm (1,2–1,4 mm); alas con flecos", "Flores y hojas", "Sí, con macro"]], [13, 38, 27, 22], "sm") +
     '<div class="c2"><p>Habrá muchas fotos de adultos y pocas de huevo, prepupa y pupa: es un caso claro de clases escasas y desbalanceadas. Si una etapa no alcanza, fusiónala con la vecina (prepupa + pupa) y reporta a ese nivel.</p>'
     '<p>Cómo fotografiar: lente macro, escala visible, fondo neutro, luz uniforme; trampa azul o amarilla para adultos.</p></div>',
     "El ciclo de vida del trips")

hoja(titulo("Identificar un trips cuando la foto no basta") +
     '<p class="lead">La especie requiere microscopio. Lo que da la foto es la etapa y el género; el contexto ayuda a ordenar candidatos.</p>'
     '<div class="c2">'
     '<h3>Lo que exige microscopio</h3>'
     '<p><i>Frankliniella</i> tiene antena de 8 segmentos (<i>Thrips</i>, 7). <i>F. occidentalis</i> se separa por las setas ocelares, las del protórax y el peine del segmento VIII. Separar especies es «tarea de expertos» (EPPO).</p>'
     '<p>Consecuencia: el rango alcanzable por foto es <b>género o «trips»</b>, y el modelo de etapa debe ser independiente de la especie.</p>'
     '<h3>Sexo</h3>'
     '<p>Los machos salen de huevos no fecundados y son más pequeños y pálidos; las hembras tienen el abdomen más redondeado y formas pálida, intermedia y oscura. Hay unas 4 hembras por macho (EPPO). «Pequeño y pálido» no es otra especie.</p>'
     '<h3>Hospedero</h3>'
     '<p>EPPO registra 244 hospederos de 62 familias para <i>F. occidentalis</i>. En especies tan generalistas, el hospedero reordena, no confirma.</p>'
     '<h3>Daño</h3>'
     '<p>Plateado, deformaciones y un punteado de excremento <b>verde oscuro</b>; los ácaros dejan gránulos negros. Separa trips de ácaros sin ver al animal.</p>'
     '<h3>Trampa</h3>'
     '<p>Las trampas azules capturan más <i>F. occidentalis</i> que las amarillas. Una feromona específica sesga la captura, pero no prueba que cada individuo sea esa especie.</p>'
     '<h3>Lugar</h3>'
     '<p>En La Ceja (Antioquia), en invernadero, la especie más frecuente en crisantemo fue <i>F. panamensis</i>, y <i>F. occidentalis</i> apareció en bouvardia. «Trips en crisantemo» no es automáticamente <i>F. occidentalis</i>.</p>'
     '</div>' +
     tabla([["Especie", "¿Vector de TSWV?", "Pista de contexto"],
            ["<i>F. occidentalis</i>", "Sí, el más eficaz", "Ornamentales; domina en la Sabana de Bogotá y Medellín"],
            ["<i>F. fusca</i>", "Sí", "Principal vector en maní (EE. UU.)"],
            ["<i>F. schultzei</i>", "Sí (TSWV, TCSV, GRSV)", "Flores y hojas; difícil de separar de <i>F. occidentalis</i>"],
            ["<i>F. tritici</i>, <i>T. palmi</i>", "No competentes", "Si hay síntomas de TSWV, no son la causa"]], [22, 26, 52], "sm"),
     "Identificar por contexto")

hoja(titulo("De la etapa al manejo") +
     '<p class="lead">La etapa decide qué control llega. Esta guía da principios por etapa, no recetas ni dosis.</p>'
     '<div class="c2">'
     '<h3>Qué llega a cada etapa</h3>'
     '<p>Los huevos están dentro del tejido, y la prepupa y la pupa en el suelo: un tratamiento foliar no los alcanza. Larvas y adultos están expuestos.</p>'
     '<h3>Opciones habituales</h3>'
     '<p>Control cultural; biológico (ácaros depredadores <i>Amblyseius</i>, chinche <i>Orius</i>, hongos <i>Beauveria</i> y <i>Metarhizium</i>, nematodos contra las pupas del suelo) y químico, con <b>resistencia a insecticidas documentada</b> en <i>F. occidentalis</i>.</p>'
     '<h3>La etapa también es riesgo</h3>'
     '<p>Solo las larvas adquieren el virus del bronceado del tomate (TSWV); los adultos lo transmiten, 3 a 10 días después. Un adulto que lo adquiere ya adulto no lo transmite (EPPO).</p>'
     '<p>Pista de contexto: insecto vector + síntomas en la planta ⇒ más probable la enfermedad que transmite. El TSWV no se diagnostica a simple vista: confirma en laboratorio.</p>'
     '<h3>Siempre</h3>'
     '<p>Consulta al agrónomo y la norma vigente del ICA. En flores de exportación el umbral puede ser cero por cuarentena del país de destino.</p>'
     '</div><div class="sp"></div><h2>Resumen operativo para el estudiante</h2>' +
     tabla([["#", "Paso"], ["1", "Fija el alcance (género <i>Frankliniella</i> o trips) con un rasgo visible"],
            ["2", "Esquema de etiquetas con etapa, sexo, sitio e individuo, y protocolo de etiquetado"],
            ["3", "Línea base con BioCLIP congelado: ¿separa las etapas?"],
            ["4", "Si falta una etapa, escalera de pocas imágenes y fusión (larva / prepupa-pupa / adulto)"],
            ["5", "Contexto dinámico: cultivo, región, época, síntomas, vector de virus"],
            ["6", "Devolver etapa + confianza + manejo general por etapa, y cuándo pedir otra foto o un experto"]], [6, 94], "sm"),
     "De la etapa al manejo")

verde("06", "La foto da la etapa y el género. La especie la confirma el microscopio.",
      "<p>El contexto (cultivo, sitio, trampa, tipo de daño) reordena candidatos, pero nunca decide solo.</p>"
      "<p>Etiqueta la variación dentro de la especie: sexo, forma de color y etapa. Es lo que más confunde a un clasificador visual.</p>", 99)

# =====================================================================================
# CAP 07 · DESPLIEGUE
# =====================================================================================
apertura(7, "Despliegue", ["Del modelo", "al telefono"],
         "Kotlin, React Native o Flutter en local, o el móvil como entrada de un servidor.", ["KOTLIN", "REACT NATIVE", "FLUTTER", "SERVIDOR"], 17)

hoja(titulo("Elegir el stack") +
     '<p class="lead">La pregunta que decide: ¿habrá conexión donde se toma la foto?</p>' +
     fig(C.stack_diagrama(467), "<b>Dos arquitecturas.</b> Arriba, todo en el teléfono con BioCLIP 1 en ONNX. Abajo, el móvil captura y un servidor con GPU analiza con BioCLIP 2.5.") +
     tabla([["Opción", "Piezas habituales", "A favor", "En contra"],
            ["<b>Kotlin nativo, local</b>", "ONNX Runtime para Android, CameraX, SQLite (+ sqlite-vec) para paquetes regionales", "Sin conexión; control del rendimiento; es lo que usó Anura", "Solo Android; el modelo (165,6 MB) se descarga aparte"],
            ["<b>React Native, local</b>", "<code>onnxruntime-react-native</code>, una librería de cámara nativa", "Un código para Android e iOS; equipo web", "Preprocesado nativo e idéntico; más capas que depurar"],
            ["<b>Flutter, local</b>", "Un plugin de ONNX Runtime para Flutter, <code>camera</code>", "Un código para dos plataformas; buena interfaz", "Plugins de terceros; mismas cautelas"],
            ["<b>Cliente + servidor</b>", "Cualquier app (también web) envía foto, GPS, fecha y notas por HTTPS a una API (p. ej. FastAPI) con BioCLIP 2.5", "Modelo grande y actualizable sin publicar la app", "Necesita red; latencia; coste; privacidad de coordenadas"],
            ["<b>Híbrido</b>", "BioCLIP 1 local responde al instante; la foto se reenvía al servidor cuando hay red", "Funciona en campo y mejora con conexión", "Dos modelos y dos contratos de embedding"]], [17, 33, 26, 24], "sm"),
     "Elegir el stack")

hoja(titulo("Cómo decidir y qué vale en cualquier stack") +
     '<div class="c2">'
     '<h2>Tres preguntas</h2>'
     '<ol><li><b>¿Hay conexión en campo?</b> Si no, todo local (Kotlin, React Native o Flutter). Si sí, el servidor da el modelo grande.</li>'
     '<li><b>¿Qué sabe el equipo?</b> Kotlin, JavaScript o Dart: usa lo que ya domina. El modelo es el mismo archivo ONNX.</li>'
     '<li><b>¿Hace falta el modelo grande?</b> Especies muy parecidas o plantas: servidor o híbrido.</li></ol>'
     '<p>Para el caso de trips, con laboratorio e internet, el cliente + servidor suele bastar: el teléfono es solo la herramienta de entrada.</p>'
     '<h2>Contrato de embedding</h2>'
     '<p>Hash del encoder + dimensión + preprocesado + normalización. Solo son comparables los vectores con contrato idéntico. En Anura, un extractor con el preprocesado mal copiado dejó la aceptación de conocidas en 0 %.</p>'
     '<h2>Exportar sin sorpresas</h2>'
     '<p><code>torch.onnx.export</code> con opset 18 y batch fijo = 1; pesos en un solo archivo; FP16 con las entradas y salidas en FP32. Verifica el tamaño y que las predicciones son idénticas a las de Python.</p>'
     '<h2>Servidor caliente</h2>'
     '<p>Descarga el modelo una vez (≈3,9 GB en FP32) a una carpeta fija con <code>HF_HOME</code>, usa <code>HF_HUB_OFFLINE=1</code> en producción, mantén el proceso cargado y precalcula los vectores de texto.</p>'
     '<h2>Qué devuelve la app</h2>'
     '<p>Top-3 con porcentaje, el nivel alcanzado (especie, género, etapa) y cuándo pedir otra foto. Nunca solo un nombre.</p>'
     '</div>' +
     bocadillo("Antes de publicar, pasa las mismas 64 fotos por Python y por el teléfono: deben dar exactamente lo mismo.", expresion="alerta", forma="flor"),
     "Cómo decidir el stack")

hoja(titulo("Varias preguntas a la vez, abstención y calibración") +
     '<div class="c2">'
     '<h2>Una base, varias cabezas</h2>'
     '<p>Un solo encoder (BioCLIP) y cabezas ligeras por pregunta: especie, etapa, sexo y salud. Es una hipótesis razonable apoyada en BioCLIP 2, no un resultado probado en Anura.</p>'
     '<h2>Saber decir «no sé»</h2>'
     '<p>Escalado de temperatura para calibrar (Guo 2017), clasificación selectiva (Geifman y El-Yaniv 2017) y reconocimiento de conjunto abierto (Vaze 2021). Elige el umbral en validación y repórtalo en test sin tocarlo.</p>'
     '<p>Rechazo jerárquico: «familia Hylidae, género probable <i>Boana</i>» vale más que «desconocido».</p>'
     '<h2>Cámaras trampa</h2>'
     '<p>Primero detector, después clasificador. El rendimiento cae en sitios nuevos (Beery 2018).</p>'
     '<h2>Evaluación</h2>'
     '<p>Separa por individuo y por sitio; reporta con condiciones; AUROC para el rechazo; calibración (ECE).</p>'
     '<h2>Coste de los errores</h2>'
     '<p>Un falso conocido contamina la base científica; un falso desconocido solo molesta. Por eso el umbral es conservador.</p>'
     '</div>' +
     nota("Recuerda.", "mínimo de imágenes por clase, acuerdo entre anotadores y manejo de enfermedades raras no tienen una cifra publicada: hay que medirlos, como se hizo con la especie."),
     "Multi-pregunta y calibración")

verde("07", "No es un diagnóstico. Es una sugerencia con su nivel de confianza.",
      "<p>Enfermedad, edad y sexo dudosos se devuelven como «compatible con…». Nunca uses una foto para decidir si un hongo se come.</p>"
      "<p>Oculta las coordenadas de especies amenazadas. Las observaciones privadas viven solo en tu servidor. Las enfermedades de notificación obligatoria se avisan a la autoridad.</p>", 55)

hoja(titulo("Glosario") +
     '<div class="c2" style="font-size:9pt">' + "".join(f"<p><b>{a}.</b> {b}</p>" for a, b in [
         ("Aumentación", "Variaciones artificiales de una foto (volteo, color, recorte) para entrenar con más variedad"),
         ("AUROC", "Qué tan bien separa un detector dos grupos; 0,5 es azar y 1 es perfecto"),
         ("Centroide", "El vector medio de las fotos de una clase; se compara cada foto nueva con él"),
         ("Contrato de embedding", "Hash del encoder + dimensión + preprocesado + normalización: lo que hace comparables dos vectores"),
         ("Embedding (vector)", "La representación numérica de una foto que produce el encoder"),
         ("Encoder congelado", "Se usa el modelo preentrenado sin cambiar sus pesos"),
         ("FAR / KAR", "Desconocidas aceptadas por error / conocidas aceptadas"),
         ("FP16", "Números de media precisión: el modelo ocupa la mitad"),
         ("Gosner", "Escala de 46 estadios del desarrollo de anuros"),
         ("kNN", "Clasificar por los vecinos más cercanos en el espacio de vectores"),
         ("LP-FT", "Entrenar primero una capa lineal y después todo el modelo"),
         ("ONNX", "Formato para correr el modelo fuera de Python, también en el móvil"),
         ("Prior", "Probabilidad previa por lugar, fecha u hospedero que reordena candidatas"),
         ("Sobreajuste", "El modelo memoriza el entrenamiento y falla con fotos nuevas"),
         ("Subajuste", "El modelo es demasiado simple y falla incluso en entrenamiento"),
         ("Top-1 / top-3", "La primera opción acierta / la correcta está entre las tres primeras"),
         ("Zero-shot", "Clasificar sin ejemplos de entrenamiento, solo con texto"),
     ]) + '</div>',
     "Glosario")

hoja(titulo("Fuentes y créditos") +
     '<div class="c2" style="font-size:8.2pt;line-height:1.45">'
     '<h3>Modelos y métodos</h3>'
     '<p>Stevens et al. 2024, <i>BioCLIP</i>, CVPR (arXiv 2311.18803). Gu et al. 2025, <i>BioCLIP 2</i>, NeurIPS (arXiv 2505.23883). Fichas de Hugging Face: imageomics/bioclip, bioclip-2, bioclip-2.5-vith14. Perfil de modelos de OpenCLIP. Kumar et al. 2022, ICLR (arXiv 2202.10054). Wortsman et al., WiSE-FT (arXiv 2109.01903). Hinton et al. 2015, destilación. PTQ4ViT (arXiv 2111.12293); RepQ-ViT (arXiv 2212.08254). Xiao et al. (arXiv 2006.09994). Northcutt et al. 2021, errores de etiqueta.</p>'
     '<p>Mac Aodha, Cole y Perona 2019, ICCV, priors geográficos. Cole et al. 2023, SINR. Guo et al. 2017; Geifman y El-Yaniv 2017; Vaze et al. 2021; Beery et al. 2018.</p>'
     '<h3>Datos y herramientas</h3>'
     '<p>Documentación de las API de iNaturalist, GBIF y MediaWiki; iNaturalist Open Data (AWS). Mohanty, Hughes y Salathé 2016, PlantVillage. Barbedo 2019. IP102 (CVPR 2019). Pl@ntNet. AmphibiaWeb.</p>'
     '<h3>Biología</h3>'
     '<p>Gosner 1960, <i>Herpetologica</i> 16. Meier 2001, monografía BBCH. Funk et al. 2012, <i>Proc. R. Soc. B</i>. Bell y Zamudio 2012, <i>Proc. R. Soc. B</i>. Lynch y Suárez 2011, <i>Caldasia</i>. Fichas de AmphibiaWeb (<i>Rhinella marina</i>).</p>'
     '<p>EPPO Global Database, ficha FRANOC. UF/IFAS EDIS IN1089 e IN401. Hamilton, Hall y Kirk 2005, <i>J. Chem. Ecol.</i> Labandeira et al. 2007, tipos de daño. Revista Colombiana de Entomología y Agronomía Colombiana (trips en Antioquia, Bogotá y Cauca).</p>'
     '<h3>Proyecto Anura</h3>'
     '<p>Cifras medidas en la base de producción (v5, 56 especies) y en los informes de las fases de septiembre de 2026: <code>teoria/anura-hallazgos.md</code>.</p>'
     '<h3>Fotos</h3>'
     '<p>Wikimedia Commons: Bernard Dupont (<i>R. marina</i>, CC BY-SA 2.0); André Karwath (CC BY-SA 2.5); Christian Fischer (CC BY-SA 3.0); James Lindsey (CC BY-SA 3.0); Syrio (CC BY-SA 4.0). <i>R. horribilis</i>: proyecto Anura.</p>'
     '<h3>Tipografía</h3>'
     '<p>Aquire (freeware, uso no comercial), Bricolage Grotesque y JetBrains Mono (OFL).</p>'
     '</div>',
     "Fuentes y créditos")


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
