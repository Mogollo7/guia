"""Muestras de diseño (portada, divisor negro, divisor verde y hojas blancas) con el tono didáctico.
Reutiliza las piezas de build.py sin generar la guía completa."""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(AQUI, "build.py"), encoding="utf-8").read()
exec(src[:src.index("\nportada()\n")])  # helpers, CSS y portada()

CSS_DIDACTICO = """
/* --- piezas didácticas --- */
.aprende{display:flex;gap:14pt;align-items:flex-start;background:#0b0d12;color:#fff;border-radius:12pt;padding:12pt 14pt;margin:0 0 16pt}
.aprende .k{font:700 6.6pt JBMono,monospace;letter-spacing:.08em;color:#dfff04;flex:0 0 74pt;padding-top:2pt}
.aprende ul{list-style:none;margin:0;padding:0;font-size:9.2pt;line-height:1.5}
.aprende li{padding-left:13pt;position:relative;margin:0 0 2pt}
.aprende li::before{content:"";position:absolute;left:0;top:4.5pt;width:5pt;height:5pt;border:1.3pt solid #dfff04;border-radius:50%}
.paso{display:grid;grid-template-columns:22pt 1fr;gap:0 9pt;margin:0 0 10pt;break-inside:avoid}
.paso .nn{font:700 15pt/1 Aquire,sans-serif;padding-top:1pt}
.paso h3{margin:0 0 2pt}.paso p{margin:0}
.exp{border:1pt solid #000;border-radius:12pt;padding:10pt 12pt;break-inside:avoid;display:flex;flex-direction:column;gap:5pt}
.exp .top{display:flex;justify-content:space-between;align-items:center;gap:8pt}
.exp .q{font:700 6.4pt JBMono,monospace;letter-spacing:.08em;text-transform:uppercase;color:#333}
.exp h3{margin:0;font-size:10.4pt}
.exp dl{display:grid;grid-template-columns:58pt 1fr;gap:3pt 6pt;margin:2pt 0 0;font-size:8.6pt;line-height:1.42}
.exp dt{font:700 6.2pt/1.9 JBMono,monospace;letter-spacing:.06em;text-transform:uppercase;color:#333}
.exp dd{margin:0}
.ver{font:700 6.4pt JBMono,monospace;letter-spacing:.06em;border-radius:99px;padding:3pt 8pt;white-space:nowrap;border:1.2pt solid #000}
.ver.si{background:#dfff04}.ver.no{background:#000;color:#dfff04;border-color:#000}.ver.medio{background:#fff}
.cambio{display:grid;grid-template-columns:1fr 26pt 1fr;align-items:stretch;margin:4pt 0 14pt;break-inside:avoid}
.cambio>div{border-radius:12pt;padding:10pt 12pt;font-size:9pt;line-height:1.45}
.cambio .antes{background:#f1f2f4}.cambio .despues{background:#dfff04;border:.8pt solid #000}
.cambio small{display:block;font:700 6.4pt JBMono,monospace;letter-spacing:.08em;margin:0 0 3pt}
.cambio .fl{display:grid;place-items:center;font:700 16pt Bricolage,sans-serif}
.turno{border-top:2.4pt solid #000;padding-top:8pt;margin-top:4pt;break-inside:avoid}
.turno .k{font:700 6.6pt JBMono,monospace;letter-spacing:.08em;margin:0 0 5pt}
.turno ul{list-style:none;margin:0;padding:0;columns:2;column-gap:23pt;font-size:9pt}
.turno li{padding-left:15pt;position:relative;margin:0 0 4pt;break-inside:avoid}
.turno li::before{content:"";position:absolute;left:0;top:2.5pt;width:8pt;height:8pt;border:1.2pt solid #000;border-radius:1.5pt}
.rot{position:absolute;left:8pt;top:5pt;font:700 6.4pt JBMono,monospace;letter-spacing:.1em;color:#fff;background:#0b0d12;padding:3pt 7pt;border-radius:99px}
"""


def aprende(items):
    return '<div class="aprende"><div class="k">AL TERMINAR<br>SABRÁS</div><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"


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


def rotular(html, texto):
    """Pone una etiqueta de muestra en la esquina (solo para revisar el diseño)."""
    return html.replace("</section>", f'<div class="rot">{texto}</div></section>', 1)


# ---------------- 1 · portada ----------------
portada()

# ---------------- 2 · divisor negro ----------------
apertura(3, "Los datos", ["Los datos pesan", "mas que el modelo"],
         "Vas a aprender de dónde sacar fotos, cuántos individuos hacen falta y cómo no engañarte al medir.",
         ["SCRAPING", "INDIVIDUOS", "ETIQUETAS", "DIVISIÓN"], 63)

# ---------------- 3 · hoja blanca de lectura (tono didáctico) ----------------
hoja(titulo("Quitar el fondo: lo que se probó") +
     '<p class="lead">Parecía obvio: si recortas al animal, el modelo deja de mirar el fondo y acierta más. Lo probamos. Pasó lo contrario.</p>' +
     aprende(["Por qué recortar o segmentar puede empeorar el resultado.", "Cómo comprobarlo en 7 minutos antes de construir nada.",
              "Qué papel le queda a la segmentación."]) +
     '<div class="c2">'
     '<div class="paso"><span class="nn">1</span><div><h3>La idea</h3><p>Las fotos de ranas traen hojarasca, rocas y manos. Si el modelo aprende ese fondo, se equivoca en otro sitio. Recortar la rana debería quitar ese atajo.</p></div></div>'
     '<div class="paso"><span class="nn">2</span><div><h3>Lo que se hizo</h3><p>Se entrenó un segmentador (IoU 83 % en test) y se compararon 150 fotos pareadas con BioCLIP: imagen completa, recorte y recorte con fondo negro.</p></div></div>'
     '<div class="paso"><span class="nn">3</span><div><h3>Lo que pasó</h3><p>El acierto bajó en cada paso: <b>60,7 → 50,7 → 44,7 %</b>. La rana ocupaba solo el 6–18 % del encuadre: al recortarla y ampliarla quedaba borrosa, y BioCLIP nunca había visto fondos negros.</p></div></div>'
     '<div class="paso"><span class="nn">4</span><div><h3>Lo que aprendimos</h3><p>Antes de construir un pipeline, haz un A/B con el modelo que vas a usar. Aquí bastaban 7 minutos de GPU; se perdieron días esperando la segmentación.</p></div></div>'
     '</div>' +
     cambio("El clasificador veía la rana recortada y con el fondo en negro.",
            "El clasificador ve la imagen completa. La segmentación solo <b>explica</b> después; nunca decide.") +
     fig(C.vbars([{"l": "COMPLETA", "v": 60.7, "hi": 1}, {"l": "RECORTE", "v": 50.7}, {"l": "FONDO NEGRO", "v": 44.7}], 100, 467, 130),
         "<b>Top-1 con las mismas 150 fotos</b> " + E("PROYECTO") + ". Lo que no se probó: reentrenar desde cero sobre los recortes.") +
     turno(["Mide tu modelo con y sin recorte antes de construir el segmentador.", "Mira cuánto ocupa el animal en el encuadre.",
            "Si recortas, reentrena con recortes; no los pases a un modelo que nunca los vio.", "Varía los fondos en el entrenamiento en vez de borrarlos."]),
     None)

# ---------------- 4 · hoja blanca de experimentos (mostrar cambios) ----------------
hoja(titulo("Lo que funcionó y lo que no") +
     '<p class="lead">Cuatro decisiones del proyecto Anura, contadas como experimentos: la pregunta, lo que se midió y el cambio que dejó.</p>'
     '<div class="g2">' +
     exp("¿Mejora entrenar todo el modelo?", "Ajuste fino de BioCLIP", "NO FUNCIONÓ",
         [("Se probó", "Descongelar 28,7 M parámetros con ~2.200 fotos"), ("Resultado", "69,2 % frente a 70,4 % sin entrenar"),
          ("Por qué", "Memorizó: pérdida 0,92 → 0,01"), ("Cambio", "Encoder congelado por defecto")]) +
     exp("¿Ayuda saber dónde se tomó la foto?", "Prior geográfico", "A MEDIAS",
         [("Se probó", "Multiplicar por la frecuencia de cada especie en 50 km"), ("Resultado", "+15 a +25 pp de top-1"),
          ("Pero", "Volteó una especie bien identificada"), ("Cambio", "El prior solo reordena; nunca decide")]) +
     exp("¿Cabe el modelo en el móvil?", "De FP32 a FP16", "FUNCIONÓ",
         [("Se probó", "Exportar la torre de imagen a ONNX en FP16"), ("Resultado", "165,6 MB, predicciones idénticas"),
          ("Ojo", "INT8 falló en cinco intentos (0,2–51 %)"), ("Cambio", "FP16 es el límite práctico en ViT")]) +
     exp("¿Menos especies, más acierto?", "Paquete regional + kNN", "FUNCIONÓ",
         [("Se probó", "Comparar solo con las especies de la región"), ("Resultado", "+11,8 pp frente a 41 clases"),
          ("Por qué", "No reparte probabilidad en especies ausentes"), ("Cambio", "Un paquete descargable por zona")]) +
     '</div><div class="sp2"></div>' +
     bocadillo("Un resultado que no funcionó también es un resultado: dice qué no repetir y ahorra semanas al siguiente equipo.", expresion="guino", forma="gota") +
     turno(["Escribe cada experimento con su pregunta antes de correrlo.", "Anota la condición: especies, fotos, división y versión.",
            "Guarda también lo que falló, con la causa.", "Deja escrito el cambio que tomaste por cada resultado."]),
     None)

# ---------------- 5 · divisor verde ----------------
verde("01", "Mide antes de construir.", "70,4 %",
      "acertó la línea base sin entrenar; el modelo ajustado se quedó en 69,2 %.",
      "Ese número costaba una tarde; construir el ajuste y la segmentación costó semanas, y ninguno mejoró el resultado.",
      "Antes de entrenar, calcula embeddings con BioCLIP y compara cada foto con el promedio de su especie.", 61,
      boca="Si la línea base ya alcanza tu objetivo, no entrenes.")

# ---------------- salida ----------------
etiquetas = ["MUESTRA 1 · PORTADA", "MUESTRA 2 · DIVISOR NEGRO", "MUESTRA 3 · HOJA BLANCA DE LECTURA",
             "MUESTRA 4 · HOJA BLANCA DE EXPERIMENTOS", "MUESTRA 5 · DIVISOR VERDE"]
paginas = [rotular(p, e) for p, e in zip(PAGINAS, etiquetas)]
doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Muestras de diseño</title><style>{CSS}{CSS_DIDACTICO}</style></head><body>'
       + C.DEFS + "".join(paginas) + "</body></html>")
with open(os.path.join(RAIZ, "salida", "muestras.html"), "w", encoding="utf-8") as fh:
    fh.write(doc)
print(len(paginas), "muestras")
