# Contenido de la guía. Se ejecuta dentro de build.py (usa sus funciones).
# Regla de orden: cada capítulo abre con hoja negra; su hoja verde va EN MEDIO, siempre entre dos hojas blancas.

# =====================================================================================
# CAP 01 · FUNDAMENTOS
# =====================================================================================
apertura(1, "Fundamentos", ["Que se le puede", "preguntar a una foto"],
         "Vas a aprender qué puede responder una foto, qué no, y por qué una especie no es una sola apariencia.", ["TAXÓN", "ETAPA", "SEXO", "RANGO"], 81)

hoja(titulo("Cómo leer esta guía") +
     '<p class="lead">Esta guía no diseña tu modelo. Te enseña los conceptos, las opciones y, sobre todo, lo que pasó cuando alguien las probó de verdad: lo que funcionó, lo que no y qué se cambió después.</p>' +
     aprende(["Para quién es y qué caso la acompaña.", "Cómo distinguir un dato medido de una opinión.", "Qué partes del problema están resueltas y cuáles no."]) +
     '<div class="c2">'
     '<h3>Para quién es</h3><p>Para estudiantes que van a construir un modelo que reconozca un organismo en una foto. El caso conductor son los trips del género <i>Frankliniella</i>: saber <b>en qué etapa de vida</b> está el insecto y recomendar el manejo.</p>'
     '<h3>De dónde salen las cifras</h3><p>Casi todas las mediciones vienen de <b>Anura</b>, un proyecto que identifica ranas de Colombia con BioCLIP en el móvil. Sus aciertos y sus errores sirven para cualquier otro grupo.</p>'
     '<h3>Las etiquetas de cada dato</h3>'
     f'<p>{E("FUENTE")} leído en un paper o una ficha. {E("PROYECTO")} medido en Anura. {E("CALC")} calculado. {E("INF")} recomendación sin fuente. {E("SIMULACIÓN")} supuesto, nunca resultado.</p>'
     '<h3>Qué está resuelto</h3><p><b>Sólido:</b> identificar la especie de un animal y, si no se puede, el género o la familia. <b>Parcial:</b> etapa, sexo, plantas y salud. <b>No desde una foto:</b> la edad en años y el diagnóstico.</p>'
     '</div>' +
     '<h2>Cómo está contada cada sección</h2>' +
     tabla([["Pieza", "Para qué sirve"],
            ["Al terminar sabrás", "Lo que vas a aprender en la sección"],
            ["Experimento (FUNCIONÓ, NO FUNCIONÓ, A MEDIAS)", "Qué se preguntó, qué se midió, por qué salió así y qué cambio dejó"],
            ["Antes → Después", "La decisión que se tomó a partir de un resultado"],
            ["Gráfico: qué muestra y qué enseñó", "Cada gráfico dice qué representa y qué lección deja"],
            ["Tu turno", "Lo que puedes hacer en tu propio proyecto"]], [36, 64]),
     "Cómo leer esta guía")

hoja(titulo("Qué se puede preguntar a una foto") +
     '<p class="lead">Una foto responde cinco familias de preguntas, cada una con una fiabilidad distinta. Saber cuál estás haciendo cambia el método.</p>' +
     aprende(["Qué preguntas son fiables desde una foto.", "Qué hacer cuando la foto no alcanza."]) +
     tabla([["Pregunta", "Qué evidencia visual usa", "Fiabilidad típica"],
            ["Especie, género, familia", "Forma, color, patrón", "Alta si hay datos; baja en especies gemelas"],
            ["Etapa de vida", "Cambios de forma (larva → adulto), fenología", "Media; depende del grupo"],
            ["Sexo", "Dimorfismo: tamaño, color, estructuras", "Solo si la especie lo tiene y se ve"],
            ["Edad", "Casi nada fiable en foto", "Baja: se usan clases de edad (cría, joven, adulto)"],
            ["Salud", "Lesiones visibles", "Pistas inespecíficas; no es diagnóstico"]], [24, 42, 34]) +
     '<div class="c2">'
     '<h3>La regla</h3><p>Responde con el nivel que la evidencia sostiene: «adulto, sexo no determinable» o «signos compatibles con una enfermedad de la piel; requiere confirmación». Un sistema que siempre contesta todo es peor que uno que a veces dice «no sé».</p>'
     '<h3>Cuando la foto no basta</h3>'
     '<ol><li>Pide otra foto: otro ángulo, más cerca, con escala.</li><li>Pide otro órgano: hoja, flor; el vientre de la rana.</li>'
     '<li>Cambia de pregunta: de «qué plaga» a «estado de la planta».</li><li>Añade contexto: lugar, fecha, cultivo.</li>'
     '<li>Baja de rango o di «no determinable».</li></ol>'
     '</div>' +
     bocadillo("La edad en años casi nunca sale de una foto: en anuros se cuentan líneas de crecimiento en un hueso del dedo.", expresion="pensando"),
     "Qué se puede preguntar a una foto")

hoja(titulo("Elegir el rango taxonómico") +
     '<p class="lead">El grupo que quieres evaluar debe separarse fácilmente de sus vecinos. Empieza por un rango cuyo límite se vea en la foto.</p>'
     '<div class="g2"><div>' +
     aprende(["Por qué conviene empezar por un grupo fácil.", "Cómo comprobar que el rasgo se ve."]) +
     '<p>Los anuros se separan del resto de anfibios porque <b>no tienen cola</b> (<i>Anura</i> significa «sin cola»). Rana frente a no-rana se resuelve con un umbral. Especie frente a especie del mismo género necesita datos y contexto.</p>'
     '<p>El rasgo depende de la etapa: los renacuajos <b>sí</b> tienen cola.</p>'
     '</div><div>' +
     fig(C.arbol(222), "<b>Siete rangos</b>, de lo general a lo particular. BioCLIP aprende con la cadena completa en el texto, pero no devuelve los siete rangos solo.") +
     '</div></div>' +
     exp("¿Se separa fácil el grupo?", "Rana frente a no-rana, y rana frente a rana", "A MEDIAS",
         [("Se midió", "El rechazo de fotos que no son ranas y de ranas de otras especies (Anura)"),
          ("Resultado", "«No es una rana»: AUROC 0,987–0,992, casi perfecto. Una rana frente a otra rana: AUROC 0,665"),
          ("Por qué", "El límite del orden es visible; el de la especie no. Lo que más se coló fueron reptiles (23 %) y salamandras (15 %), los vecinos más parecidos"),
          ("Cambio", "Dos decisiones separadas: primero «¿es del grupo?», después «¿cuál es?»")]) +
     turno(["Escribe los rasgos que separan tu grupo de sus vecinos.", "Comprueba que esos rasgos se ven en tus fotos.",
            "Mide el rechazo del grupo antes que el de la especie.", "En trips: orden fácil (alas con flecos, &lt;2 mm); especie, no."]),
     "Elegir el rango taxonómico")

verde("01", "Devuelve solo el nivel que la evidencia sostiene.",
      "<p>«Familia Hylidae, género probable <i>Boana</i>, especie no determinable» vale más que un nombre de especie equivocado.</p>"
      "<p>En Anura, 27 de 28 especies con pocos datos quedaron cubiertas a nivel de género o familia. El rescate vino de la taxonomía, no de inflar los datos.</p>", 71,
      boca="Bajar de rango no es fallar: es decir la verdad.")

hoja(titulo("Una especie no es una sola apariencia") +
     '<p class="lead">Un individuo tiene un rango taxonómico, pero también una etapa y un sexo, y los tres cambian lo que se ve.</p>' +
     graf("Especie × etapa × sexo en un trips · ilustración", C.matriz_eta_sexo(467),
          "Cada celda es una combinación de etapa y sexo con su propio prototipo; el borde discontinuo marca etapas con pocas fotos esperables.",
          "Una sola etiqueta «especie» mezcla apariencias muy distintas: un único centroide queda en el medio y no representa a ninguna.") +
     '<div class="c2">'
     f'<p>BioCLIP 2 reporta que la variación dentro de una especie (etapas, sexos) se conserva en el espacio de vectores, separada de la variación entre especies {E("FUENTE")}. Los autores aclaran que no lo probaron formalmente.</p>'
     '<h3>Tres maneras de modelarlo</h3>'
     '<ol><li>Una etiqueta compuesta «especie-etapa».</li><li>Un vector común y <b>cabezas separadas</b> por pregunta.</li><li>Prototipos por celda, con préstamo del global si hay menos de 3 individuos.</li></ol>'
     '</div>' +
     tabla([["Campo", "Valores", "Si no se puede saber"],
            ["Taxón", "Familia, género o especie (el más fino confirmado)", "<code>no_determinable</code> + rango"],
            ["Etapa", "Las del grupo: huevo, larva I, larva II, prepupa, pupa, adulto", "<code>no_determinable</code>"],
            ["Sexo", "Macho, hembra, indiferenciado", "<code>no_determinable</code>"],
            ["Salud, calidad", "Sano o síntoma; nítida, borrosa, escala visible", "<code>no_determinable</code>"],
            ["Individuo, sitio, fecha", "Identificadores", "—"]], [22, 50, 28], "sm") +
     turno(["Diseña la etiqueta con todos los campos desde el principio.", "Cuenta cuántas fotos tienes por celda, no por especie."]),
     "Una especie no es una sola apariencia")

hoja(titulo("Taxonomía y cómo identifican los expertos") +
     '<p class="lead">Los expertos combinan varias evidencias; la foto es solo una. Conocerlas te dice cuándo tu modelo debe pedir ayuda.</p>' +
     '<div class="c2">'
     '<h3>Morfología y claves</h3><p>Claves dicotómicas (dos opciones por paso) y caracteres diagnósticos.</p>'
     f'<h3>ADN</h3><p>Código de barras: COI (648 pares de bases) en animales; rbcL + matK en plantas; ITS en hongos {E("FUENTE")}.</p>'
     '<h3>Sonido</h3><p>Cantos de ranas y aves (Xeno-canto, Merlin).</p>'
     f'<h3>Ciencia ciudadana</h3><p>En iNaturalist, el «grado de investigación» exige que más de 2/3 de los identificadores coincidan en la especie {E("FUENTE")}.</p>'
     '<h3>Cuándo la foto no basta</h3><p>Especies crípticas, partes que no se ven (vientre translúcido) y estadios distintos.</p>'
     '</div>' +
     tabla([["Grupo", "Ruta habitual", "Pista de apoyo"],
            ["Anfibios", "Cuerpo entero + vientre; canto", "Altitud, región, hora"], ["Reptiles", "Escamas, color, papada", "Región, microhábitat"],
            ["Aves", "Foto + canto", "Fecha y lugar"], ["Mamíferos", "Cámaras trampa; detector primero", "Sitio"],
            ["Insectos", "Foto + estadio", "Planta hospedera"], ["Plantas", "Hoja, flor, fruto", "Región, altitud"], ["Hongos", "Cuerpo fructífero; ADN", "Sustrato"]], [20, 46, 34], "sm") +
     exp("¿Se puede confiar en el nombre?", "Sinónimos y cambios de nombre", "NO FUNCIONÓ",
         [("Pasó", "<i>D. labialis</i> y <i>D. molitor</i> resultaron ser la misma especie: el 79,1 % de sus fotos era la misma observación"),
          ("Efecto", "Contaminó una evaluación de rechazo en Anura"),
          ("Cambio", "Versionar la taxonomía, guardar sinónimos y mapear nombres con un diccionario explícito")]),
     "Taxonomía y cómo identifican los expertos")

# =====================================================================================
# CAP 02 · EL MODELO
# =====================================================================================
apertura(2, "El modelo", ["BioCLIP y la", "ruta de metodo"],
         "Vas a aprender qué es BioCLIP, cuál elegir, cómo instalarlo y por qué casi nunca hay que entrenarlo.", ["BIOCLIP", "ONNX", "RUTA", "CONGELADO"], 91)

hoja(titulo("BioCLIP: qué es y cómo funciona") +
     '<p class="lead">BioCLIP convierte una foto en un vector que ya «sabe» de taxonomía. Es el punto de partida de todo lo demás.</p>' +
     aprende(["Qué aprende BioCLIP y por qué sirve con especies raras.", "Qué cambia entre las versiones 1, 2 y 2.5."]) +
     '<div class="g2"><div>'
     f'<p><b>BioCLIP</b> es un modelo de visión y lenguaje para el árbol de la vida (Imageomics; CVPR 2024; licencia MIT) {E("FUENTE")}. Acerca el vector de una foto al vector del texto que la describe.</p>'
     '<p>El texto lleva la <b>cadena taxonómica completa</b>, por eso las especies del mismo género quedan cerca. En una ablación: texto mixto 30,9; taxonómico + común 30,4; solo científico 22,3.</p>'
     '</div><div>' +
     graf("Zero-shot, media de 10 tareas", C.vbars([{"l": "BIOCLIP 1", "l2": "512-d", "v": 37.6, "t": "37,6"}, {"l": "BIOCLIP 2", "l2": "768-d", "v": 55.6, "t": "55,6"}, {"l": "BIOCLIP 2.5", "l2": "1024-d", "v": 61.3, "hi": 1, "t": "61,3"}], 100, 222, 132),
          "Acierto sin ejemplos de entrenamiento en 10 conjuntos públicos " + E("FUENTE") + ".",
          "Cada versión acierta más, pero son benchmarks: con tus especies hay que medirlo.") +
     '</div></div>' +
     tabla([["", "BioCLIP 1", "BioCLIP 2", "BioCLIP 2.5 Huge"],
            ["Torre de imagen", "ViT-B/16", "ViT-L/14", "ViT-H/14"], ["Embedding", "512", "768", "1024"],
            ["Datos", "~10,4 M imágenes, 454 mil taxones", "214 M imágenes, 952 mil taxones", "~19 M más"],
            ["Tamaño FP16 " + E("CALC"), "0,30 GB", "0,86 GB", "1,97 GB"], ["Cómputo (torre de imagen)", "35 GFLOPs", "162 GFLOPs", "335 GFLOPs"]], [25, 25, 25, 25], "sm") +
     bocadillo("La mejora de 2.5 no se debe solo a las 1024 dimensiones: el modelo es ~6,6 veces más grande y vio ~20 veces más datos.", expresion="guino", forma="nube"),
     "BioCLIP: qué es y cómo funciona")

hoja(titulo("Conseguir BioCLIP y configurarlo") +
     '<p class="lead">Los tres modelos están en Hugging Face. Se cargan con OpenCLIP o con pybioclip, según lo que necesites hacer.</p>' +
     aprende(["Dónde descargar cada versión.", "Cómo sacar un vector de una foto.", "Qué configuración usar en móvil y en servidor."]) +
     '<div class="c2">'
     '<h3>Dónde está</h3><ul><li><code>imageomics/bioclip</code> (v1, MIT).</li><li><code>imageomics/bioclip-2</code>.</li><li><code>imageomics/bioclip-2.5-vith14</code> (MIT).</li></ul>'
     '<h3>OpenCLIP o pybioclip</h3><p><b>OpenCLIP</b> da el modelo, su preprocesado exacto y el tokenizador: es la base para centroides y ONNX. <b>pybioclip</b> trae clasificadores listos (<code>TreeOfLifeClassifier</code>, <code>CustomLabelsClassifier</code>) y la orden <code>bioclip predict</code>.</p>'
     '</div>'
     '<pre>pip install open_clip_torch pybioclip\n\nimport open_clip, torch\nfrom PIL import Image\nm, _, prep = open_clip.create_model_and_transforms("hf-hub:imageomics/bioclip")\nm.eval()\nwith torch.no_grad():\n    v = m.encode_image(prep(Image.open("foto.jpg")).unsqueeze(0))\nv = v / v.norm(dim=-1, keepdim=True)   # vector L2 para centroides o kNN</pre>' +
     tabla([["Necesidad", "Configuración"],
            ["Probar en una tarde", "<code>bioclip predict</code> o <code>CustomLabelsClassifier</code> con tus nombres"],
            ["Pocas fotos por clase", "Embeddings congelados + un centroide por especie, etapa o sexo"],
            ["Móvil sin conexión", "Torre de imagen de BioCLIP 1 en ONNX FP16 (165,6 MB) + centroides en SQLite " + E("PROYECTO")],
            ["Servidor con GPU", "BioCLIP 2.5 cargado una vez; <code>HF_HOME</code> fijo, <code>HF_HUB_OFFLINE=1</code>, textos precalculados"],
            ["Siempre", "Mismo preprocesado y un <b>contrato de embedding</b>: hash del encoder + dimensión + preprocesado + normalización"]], [26, 74], "sm") +
     exp("¿Da lo mismo cualquier preprocesado?", "Un extractor de vectores mal copiado", "NO FUNCIONÓ",
         [("Pasó", "Un script cargaba el modelo con otro preprocesado manual"), ("Resultado", "Aceptación de especies conocidas: 0 %"),
          ("Cambio", "El contrato de embedding: solo se comparan vectores con contrato idéntico")]),
     "Conseguir BioCLIP y configurarlo")

hoja(titulo("Fine-tuning o congelado") +
     '<p class="lead">Ajustar todos los pesos parece la forma de «enseñarle tus especies» al modelo. Con pocas fotos por especie, lo que hace es memorizarlas.</p>' +
     aprende(["Qué pasa dentro del modelo cuando lo ajustas.", "Qué se midió en Anura y en la literatura.", "Cuándo sí conviene ajustar."]) +
     '<div class="g2"><div>' +
     graf("Kumar et al. 2022 · 3 métodos", C.agrupadas([("FT", [85.1, 59.3]), ("LP", [82.9, 66.2]), ("LP-FT", [85.7, 68.9])], [("ID", "n"), ("OOD", "l")], 100, 222, 138),
          "Acierto medio dentro (negro) y fuera (lima) de la distribución de entrenamiento " + E("FUENTE") + ".",
          "Ajustar todo gana 2 puntos dentro pero pierde 7 fuera; LP-FT gana en ambos.") +
     '</div><div>' +
     graf("Anura · 28 especies", C.vbars([{"l": "SIN ENTRENAR", "v": 70.4, "hi": 1}, {"l": "AJUSTE FINO", "v": 69.2}, {"l": "+ ALBUMENT.", "v": 19.7, "gris": 1}], 100, 222, 138),
          "Top-1 en test de la línea base sin entrenar, del ajuste fino y del ajuste con una aumentación mal configurada " + E("PROYECTO") + ".",
          "El ajuste no mejoró nada y una configuración equivocada lo hundió.") +
     '</div></div>' +
     '<div class="c2">'
     '<h3>Por qué pasa</h3><p>Una cabeza nueva empieza al azar y, al entrenarla, arrastra las capas de abajo: se deforman las características que el modelo ya traía. Con ~2.200 imágenes y 28,7 M parámetros, la pérdida de entrenamiento bajó de 0,92 a 0,01: memorizó.</p>'
     '<h3>Si aun así hace falta ajustar</h3><p>Primero solo la capa lineal; luego LP-FT con tasa de aprendizaje baja o WiSE-FT. Valida en sitios nuevos y recalcula todos los vectores.</p>'
     '</div>' +
     cambio("Ajustar BioCLIP con las fotos del proyecto.", "Encoder <b>congelado</b>; añadir una especie es calcular un vector."),
     "Fine-tuning o congelado")

verde("02", "Usa BioCLIP congelado por defecto y ajusta solo si demuestras que hace falta.",
      "<p>La medición propia dice que el ajuste no mejora el top-1 y memoriza. La literatura lo respalda: el ajuste completo rinde peor fuera de distribución.</p>"
      "<p>Regla: ajuste fino completo solo con más de 500 imágenes por clase y buen equilibrio.</p>", 77,
      boca="Congelado también es más barato: no necesitas GPU para mantenerlo.")

hoja(titulo("Ruta de método, paso 0 a 5") +
     '<p class="lead">El orden importa: primero mide lo más simple. Solo subes de peldaño si el anterior no alcanza tu objetivo.</p>' +
     graf("Pipeline de referencia", C.pipeline(467),
          "Los ocho pasos de un proyecto, del alcance a la interfaz. En lima, la línea base sin entrenar.",
          "En Anura la línea base sin entrenar fue el mejor resultado; medirla primero habría ahorrado semanas.") +
     '<div class="c2">'
     '<h3>Paso 0 · Define la pregunta</h3><p>Qué se distingue, cuántas clases, dónde corre y qué error es peor: confundir dos clases parecidas o no reconocer nada.</p>'
     '<h3>Paso 1 · Mira tus datos</h3>' +
     tabla([["Si tienes", "Empieza por"], ["&lt; 50 fotos por clase", "Embeddings + vecino más cercano"], ["50 a 500", "Capa lineal, encoder congelado"],
            ["&gt; 500 y equilibrio", "Ajuste fino, con cuidado"], ["Clases que cambian", "Búsqueda por similitud"]], [45, 55], "sm") +
     '<h3>Paso 2 · Escalera de métodos</h3><ol><li>Línea base sin entrenar.</li><li>Clasificador lineal.</li><li>Ajuste de la última capa.</li><li>Ajuste fino completo.</li><li>Detección + clasificación.</li><li>Modelo grande en servidor.</li></ol>'
     '<h3>Paso 3 · Evalúa siempre igual</h3><p>Top-1, top-5, F1 por clase y matriz de confusión; división por individuo; un umbral para decir «no sé».</p>'
     '<h3>Pasos 4 y 5</h3><p>No prometas un número antes de medirlo. Despliega según el dispositivo (capítulo 07).</p>'
     '</div>',
     "Ruta de método")

hoja(titulo("Otras opciones y con qué compararlo") +
     '<p class="lead">BioCLIP no es la única opción. Conocer las demás te ayuda a elegir una buena comparación y a saber qué no hace cada una.</p>' +
     tabla([["Modelo", "Qué es", "Cuándo usarlo", "Límite"],
            ["CLIP / OpenCLIP", "Visión y lenguaje general", "Comparación", "21,9 y 20,4 de media frente a 39,4 de BioCLIP 1"],
            ["SigLIP", "Visión y lenguaje general", "Comparación", "39,5 de media (BioCLIP 1: 37,6, mismo protocolo)"],
            ["DINO / DINOv2", "Visión autosupervisada", "Vectores sin texto", "BioCLIP solo compara con DINO v1"],
            ["BioTrove (BT-CLIP)", "CLIP biológico", "Alternativa", "Sin comparación directa"],
            ["SpeciesNet", "Más de 2.000 etiquetas", "Cámaras trampa", "Cerrado a su catálogo"],
            ["MegaDetector", "Detecta animal, persona, vehículo", "Filtrar fotos vacías", "No da especie"],
            ["Pl@ntNet", "1 a 5 fotos por consulta, con órgano", "Plantas", "Propietario"],
            ["Merlin", "Foto y sonido con lugar y fecha", "Diseño de paquetes regionales", "Cerrado"]], [17, 29, 24, 30], "sm") +
     '<div class="c2">'
     '<h3>Cuál BioCLIP elegir</h3><p><b>Móvil sin internet:</b> BioCLIP 1 en ONNX FP16. <b>Servidor con GPU:</b> BioCLIP 2.5. <b>Compromiso:</b> BioCLIP 2. En cualquier caso, mide con tus fotos.</p>'
     '<h3>Dónde fallan</h3><p>BioCLIP 1 saca 6,1 en Plankton y apenas mejora a CLIP en enfermedades de plantas (28,4 frente a 26,1).</p>'
     '</div>' +
     turno(["Compara siempre contra CLIP y contra tu línea base.", "Si tu problema son enfermedades de plantas, busca un modelo de enfermedades.",
            "Usa MegaDetector para quitar fotos vacías antes de clasificar.", "Guarda la versión exacta del modelo que usaste."]),
     "Otras opciones")

# =====================================================================================
# CAP 03 · LOS DATOS
# =====================================================================================
apertura(3, "Los datos", ["Los datos pesan", "mas que el modelo"],
         "Vas a aprender de dónde sacar fotos, cuántos individuos hacen falta y cómo no engañarte al medir.", ["SCRAPING", "INDIVIDUOS", "ETIQUETAS", "DIVISIÓN"], 63)

hoja(titulo("De dónde sacar imágenes de cualquier animal") +
     '<p class="lead">Casi todo empieza en iNaturalist y GBIF. La calidad depende de guardar los metadatos de cada foto y de no mezclar fuentes duplicadas.</p>' +
     aprende(["Qué fuentes públicas hay y qué da cada una.", "Qué cuidar antes de descargar."]) +
     tabla([["Fuente", "Qué da", "Cómo se accede", "Cuidado"],
            ["iNaturalist", "Fotos con observación, lugar, fecha, autor, licencia y grado de investigación", "API v1 (<code>/v1/observations</code>; hasta 200 por página); <code>pyinaturalist</code>; volcado abierto en AWS", "Cuotas; en insectos las etiquetas son las menos fiables"],
            ["GBIF", "Registros de muchas colecciones", "API <code>occurrence/search</code> con <code>mediaType=StillImage</code>; descargas con DOI; <code>pygbif</code>", "Duplica registros de iNaturalist"],
            ["Wikimedia Commons", "Fotos curadas con autor y licencia", "API de MediaWiki por categoría", "Pocas fotos por especie"],
            ["Conjuntos armados", "iNat2021, TreeOfLife-10M, BIOSCAN-5M, IP102, Pl@ntNet-300K, PlantVillage", "Hugging Face o su página", "Licencias; test de laboratorio"],
            ["Xeno-canto", "Cantos", "API v3 con clave", "La v2 se retiró"],
            ["Fotos propias", "Etapas raras y tu región", "Protocolo con escala", "Caras, pero las más útiles"]], [15, 28, 36, 21], "sm") +
     '<div class="c2">'
     '<h3>Antes de descargar</h3><p>Haz la lista de taxones con sus <b>sinónimos</b>. Elige licencias que puedas usar (CC0, CC BY; CC BY-NC si no es comercial) y cita al autor.</p>'
     f'<h3>Lo que tarda</h3><p>En Anura {E("PROYECTO")}: GBIF ≈7 s por especie; iNaturalist 5–10 min por especie (40 individuos, 3 fotos por individuo).</p>'
     '</div>' +
     bocadillo("En iNaturalist la URL de una foto cambia de tamaño reemplazando <b>square</b> por <b>medium</b>, <b>large</b> u <b>original</b>.", expresion="guino", forma="gota"),
     "De dónde sacar imágenes")

hoja(titulo("Cómo scrapear sin romper nada") +
     '<p class="lead">Ocho pasos. Los dos en lima son los que más evaluaciones han arruinado cuando se saltan.</p>' +
     graf("El pipeline de descarga", C.scraping(467),
          "El recorrido de una foto desde la API hasta el conjunto versionado.",
          "Deduplicar por observación y dividir por individuo evitan métricas infladas.") +
     '<div class="c2">'
     '<h3>1 · Taxones y sinónimos</h3><p>Usa el backbone de GBIF o el catálogo del grupo.</p>'
     '<h3>2 · Siempre por API</h3><p>Una especie a la vez, con <code>User-Agent</code>, pausa y reintentos. iNaturalist pide alrededor de una petición por segundo y menos de 10.000 al día.</p>'
     '<h3>3 · Metadatos antes que fotos</h3><p><code>obs_id</code>, <code>photo_id</code>, URL, licencia, autor, coordenadas y precisión, fecha, calidad.</p>'
     '<h3>4 · Filtra</h3><p>Licencias, coordenadas imprecisas (Anura descartó errores de hasta 7.270 km), cautivos, fotos de manejo.</p>'
     '<h3>5 · Descarga</h3><p>Con cola, límite y reanudación (<code>img2dataset</code>). Comprueba que cada archivo abre.</p>'
     '<h3>6 · Deduplica</h3><p>Por hash exacto, por pHash <b>y por observación</b> entre fuentes.</p>'
     '<h3>7 · Divide por individuo</h3><p>Antes de aumentar; congela el test.</p>'
     '<h3>8 · Versiona</h3><p>Fecha, consulta y conteos por especie y etapa.</p>'
     '</div>'
     '<pre>import requests, time\nURL = "https://api.inaturalist.org/v1/observations"\nq = {"taxon_name": "Frankliniella", "quality_grade": "research", "photos": "true",\n     "photo_license": "cc0,cc-by,cc-by-nc", "per_page": 200, "page": 1}\nr = requests.get(URL, params=q, headers={"User-Agent": "guia-ia/1.0 (correo@ejemplo)"}).json()\nfor o in r["results"]:\n    for f in o["photos"]:\n        print(o["id"], f["id"], f["license_code"], f["url"].replace("square", "medium"))\ntime.sleep(1)   # una petición por segundo</pre>',
     "Cómo scrapear")

hoja(titulo("Individuos frente a fotos") +
     '<p class="lead">Lo que estabiliza un centroide es la variación <b>entre individuos</b>, no cuántas fotos tienes del mismo animal.</p>' +
     graf("Mismo número de fotos, distinta variedad · ilustración", C.individuos(467),
          "Dos muestras de 20 fotos: a la izquierda, un solo individuo; a la derecha, diez. La elipse es la especie real; la ✕, el centroide aprendido.",
          "Con un individuo el modelo aprende ese animal, su fondo y su luz; con diez, aprende la especie.") +
     '<div class="g2"><div>' +
     tabla([["Nivel", "Fotos", "Individuos"], ["Mínimo viable", "10–15", "3–5"], ["Recomendado", "30–50", "8–12"], ["Robusto", "80–100+", "15+"],
            ["Piso de un paquete (v5)", "≥ 80", "≥ 10"], ["Identificación entrenada", "—", "≥ 70"]], [50, 25, 25], "sm") +
     f'<p class="pie">Reglas de Anura por clase {E("PROYECTO")}.</p></div><div>' +
     exp("¿Más fotos, más acierto?", "Fotos frente a individuos", "NO FUNCIONÓ",
         [("Se midió", "La relación entre acierto y número de individuos (56 especies)"), ("Resultado", "Con ≥38 individuos, más fotos ya no ayudó: correlación −0,05"),
          ("Lo que sí", "Lo cerca que está la especie vecina (−0,62)")]) +
     '</div></div>' +
     turno(["Pide variedad: animales, sitios, luces y fondos distintos.", "Cuenta individuos por celda (especie × etapa × sexo)."]),
     "Individuos frente a fotos")

verde("03", "Más individuos distintos valen más que más fotos del mismo.",
      "<p>100 fotos de un animal enseñan ese animal. 20 individuos × 5 fotos enseñan la especie.</p>"
      "<p>Y divide siempre por individuo: si el mismo animal está en entrenamiento y en prueba, la métrica miente.</p>", 57,
      boca="En la Fase 13 de Anura, el 100 % del test ya estaba en el entrenamiento.")

hoja(titulo("Sobreajuste y subajuste") +
     '<p class="lead">El modelo puede quedarse corto (subajuste) o aprenderse de memoria las fotos de entrenamiento (sobreajuste). La curva de validación lo delata.</p>' +
     graf("Error de entrenamiento y de validación · ilustración", C.curvas_ajuste(467),
          "El error de entrenamiento (continua) baja siempre; el de validación (discontinua) baja, toca fondo y sube.",
          "El mejor modelo es el de la parada temprana, no el último. En Anura el pico de validación llegó en la época 10.") +
     tabla([["", "Señal", "Ejemplo", "Remedio"],
            ["<b>Subajuste</b>", "Error alto en entrenamiento y validación", "Zero-shot con nombres que el modelo no conoce", "Centroides o capa lineal; más épocas"],
            ["<b>Punto justo</b>", "Validación en su mejor valor", "Anura: 72,7 % en la época 10", "Parada temprana"],
            ["<b>Sobreajuste</b>", "Entrenamiento baja; validación sube", "Anura: pérdida 0,92 → 0,01; test 69,2 %", "Congelar, más individuos, aumentación, regularización"]], [14, 26, 32, 28], "sm") +
     cambio("Dividir las fotos al azar y entrenar hasta la última época.", "Dividir por individuo y sitio, y guardar el modelo de la parada temprana.") +
     turno(["Mira entrenamiento y validación en el mismo gráfico.", "Mide la línea base sin entrenar.", "Prefiere más individuos a más fotos.", "Prueba la aumentación sola antes de entrenar."]),
     "Sobreajuste y subajuste")

hoja(titulo("Etiquetar bien") +
     '<p class="lead">Una etiqueta mala no se arregla con más datos: el modelo la aprende.</p>' +
     aprende(["Cuántos errores traen los conjuntos públicos.", "Un protocolo mínimo de etiquetado."]) +
     '<div class="c2">'
     f'<p>Al menos un 3,3 % de etiquetas erróneas de media en 10 conjuntos de prueba, y al menos un 6 % en la validación de ImageNet (Northcutt et al. 2021) {E("FUENTE")}. La herramienta cleanlab estima las sospechosas.</p>'
     '<p>En iNaturalist, una estimación informal de 2019 daba ~85 % de grado de investigación correcto: 91 % en aves y 65 % en insectos.</p>'
     '</div>' +
     exp("¿Están limpias las etiquetas?", "Errores reales del proyecto Anura", "NO FUNCIONÓ",
         [("Pasó", "Siete errores de nomenclatura; carpetas con errores de tipeo; el <code>individual_id</code> era la observación y no un animal"),
          ("Efecto", "La búsqueda de negativos difíciles elegía una y otra vez el error"),
          ("Cambio", "Diccionario explícito de nombres y regla «ante la duda, <code>no_determinable</code>»")]) +
     '<div class="sp"></div>' +
     tabla([["#", "Protocolo mínimo"], ["1", "Guía de anotación con ejemplos de cada valor y de cada <code>no_determinable</code>"],
            ["2", "Ante la duda, <code>no_determinable</code>; ante desacuerdo, el valor más conservador"],
            ["3", "Dos anotadores sobre una muestra; medir el acuerdo (kappa de Cohen)"], ["4", "Un experto para la especie (en trips, microscopio)"],
            ["5", "Versionar la taxonomía y guardar sinónimos"], ["6", "Revisar los casos de mayor pérdida antes de reentrenar"], ["7", "Congelar el test antes de mirar resultados"]], [6, 94], "sm"),
     "Etiquetar bien")

hoja(titulo("Pocas imágenes: aumentación y alternativas") +
     '<p class="lead">Si faltan fotos, baja peldaño a peldaño, de lo más barato a lo más costoso.</p>' +
     graf("Escalera si no hay suficientes imágenes", C.escalera(467),
          "Seis respuestas a la falta de fotos, ordenadas por coste. Las cifras del primer peldaño son de BioCLIP 1, no de trips.",
          "Con 1 a 5 fotos por clase ya hay un punto de partida útil; las imágenes sintéticas son el último recurso.") +
     '<div class="c2">'
     f'<h3>Aumentación de Anura {E("PROYECTO")}</h3>'
     '<p><b>Moderada</b>: recorte 0,6–1,0, volteos, rotación ±20°, brillo y contraste 0,25, matiz 0,05. <b>Agresiva</b> solo en las repeticiones de especies con menos de 70 individuos. Validación y test sin aumentación.</p>'
     '<h3>Qué no romper</h3>'
     '<ul><li>Color diagnóstico: matiz ≤ ±10 a 15°.</li><li>Tamaño: si la etapa se distingue por tamaño, deja una escala.</li><li>Fondo: varíalo para que no lo aprenda.</li></ul>'
     '</div>' +
     exp("¿Cualquier librería de aumentación sirve?", "Albumentations mal normalizada", "NO FUNCIONÓ",
         [("Pasó", "Se cambió de torchvision a Albumentations sin revisar la normalización"), ("Resultado", "El top-1 cayó de 69,2 % a 19,7 %"),
          ("Cambio", "Volver a torchvision y probar la aumentación sola antes de entrenar")]),
     "Pocas imágenes")

# =====================================================================================
# CAP 04 · CASO REAL
# =====================================================================================
apertura(4, "Caso real", ["Anuros de", "Colombia"],
         "Vas a ver qué se midió en un proyecto real, qué funcionó, qué no y qué decisión dejó cada resultado.", ["TOP-1", "TOP-3", "RECHAZO", "ERRORES"], 53)

hoja(titulo("Cuánto acierta el sistema") +
     '<p class="lead">El dataset vigente tiene 56 especies, 5.818 fotos y 3.240 individuos. Así se comporta con fotos que nunca vio.</p>'
     '<div class="mets">' + met("Top-1", "62,9%", "la primera opción acierta", "l") + met("Top-3", "86,1%", "la correcta está entre tres", "n") +
     met("Especies", "56", "5.818 fotos · 3.240 individuos", "g") + '</div>'
     '<div class="g2"><div>' +
     graf("Acierto con 56 especies", C.vbars([{"l": "TOP-1", "v": 62.85, "hi": 1, "err": 3.2, "t": "62,85%"}, {"l": "TOP-3", "v": 86.11, "t": "86,11%"}, {"l": "TOP-5", "v": 91.09, "t": "91,09%"}], 100, 222, 140),
          "Acierto en 864 fotos de prueba comparando con el promedio de cada especie " + E("CALC") + ". La barra es el margen de error.",
          "Mostrar tres candidatas sube el acierto 23 puntos: la app debe enseñar el top-3.") +
     '</div><div>' +
     graf("Más especies, menos acierto", C.linea([(5, 87.3), (18, 78.2), (28, 74.3), (56, 64.4)], (0, 60), (60, 100), "especies en el modelo", "% acierto", 222, 140),
          "Acierto en validación a medida que el catálogo creció de 5 a 56 especies " + E("PROYECTO") + ".",
          "Cada especie nueva compite con las demás: por eso conviene acotar por región.") +
     '</div></div>' +
     cambio("Un solo modelo con todas las especies y una sola respuesta.", "Paquetes por región y tres candidatas con su porcentaje."),
     "Cuánto acierta")

hoja(titulo("Lo que funcionó y lo que no") +
     '<p class="lead">Cuatro decisiones del proyecto contadas como experimentos: la pregunta, lo que se midió y el cambio que dejó.</p>'
     '<div class="g2">' +
     exp("¿Ayuda saber dónde se tomó la foto?", "Prior geográfico", "A MEDIAS",
         [("Se probó", "Multiplicar por la frecuencia de cada especie en 50 km"), ("Resultado", "+15 a +25 pp de top-1"),
          ("Pero", "Volteó una especie bien identificada"), ("Cambio", "El prior solo reordena; nunca decide")]) +
     exp("¿Menos especies, más acierto?", "Paquete regional + kNN", "FUNCIONÓ",
         [("Se probó", "Comparar solo con las especies de la región"), ("Resultado", "+11,8 pp frente a 41 clases"),
          ("Por qué", "No reparte probabilidad en especies ausentes"), ("Cambio", "Un paquete descargable por zona")]) +
     exp("¿Mejora un centroide regional?", "Promedio por región", "NO FUNCIONÓ",
         [("Se probó", "Centroides calculados solo con fotos de la región (Sinú)"), ("Resultado", "70,99 % frente a 73,83 % con los globales"),
          ("Por qué", "Menos fotos por especie; la diferencia cae dentro del ruido"), ("Cambio", "Se usan los centroides globales")]) +
     exp("¿Cabe el modelo en el móvil?", "De FP32 a FP16", "FUNCIONÓ",
         [("Se probó", "Exportar la torre de imagen a ONNX en FP16"), ("Resultado", "165,6 MB, predicciones idénticas"),
          ("Ojo", "INT8 falló en cinco intentos (0,2–51 %)"), ("Cambio", "FP16 es el límite práctico")]) +
     '</div><div class="sp"></div>' +
     bocadillo("Un resultado que no funcionó también es un resultado: dice qué no repetir y ahorra semanas al siguiente equipo.", expresion="guino", forma="gota"),
     "Lo que funcionó y lo que no")

hoja(titulo("Quitar el fondo: lo que se probó") +
     '<p class="lead">Parecía obvio: si recortas al animal, el modelo deja de mirar el fondo y acierta más. Se probó. Pasó lo contrario.</p>' +
     aprende(["Por qué recortar puede empeorar el resultado.", "Cómo comprobarlo en minutos antes de construir nada.", "Qué papel le queda a la segmentación."]) +
     '<div class="c2">' +
     paso(1, "La idea", "Las fotos traen hojarasca, rocas y manos. Si el modelo aprende ese fondo, se equivoca en otro sitio. Recortar la rana debería quitar ese atajo.") +
     paso(2, "Lo que se hizo", "Se entrenó un segmentador (IoU 83 % en test) y se compararon 150 fotos pareadas con BioCLIP: completa, recorte y fondo negro.") +
     paso(3, "Lo que pasó", "El acierto bajó en cada paso. La rana ocupaba el 6–18 % del encuadre: ampliada, quedaba borrosa, y BioCLIP nunca había visto fondos negros.") +
     paso(4, "Lo que aprendimos", "Haz un A/B con el modelo que vas a usar antes de construir el pipeline. Bastaban 7 minutos de GPU; se perdieron días.") +
     '</div>' +
     graf("Top-1 con las mismas 150 fotos", C.vbars([{"l": "COMPLETA", "v": 60.7, "hi": 1}, {"l": "RECORTE", "v": 50.7}, {"l": "FONDO NEGRO", "v": 44.7}], 100, 467, 118),
          "Acierto de BioCLIP con la foto completa, recortada y recortada con fondo negro " + E("PROYECTO") + ".",
          "Cuanto más se aleja la foto de lo que el modelo vio al entrenarse, peor rinde. Reentrenar sobre recortes no se probó.") +
     cambio("El clasificador veía la rana recortada y con fondo negro.", "Ve la imagen completa; la segmentación solo <b>explica</b> después."),
     "Quitar el fondo")

verde("04", "Mide antes de construir.",
      "<p>En Anura, la línea base sin entrenar (70,4 %) le ganó al modelo ajustado (69,2 %), y la foto completa le ganó al recorte. Esos números costaban una tarde; construir lo otro costó semanas.</p>"
      "<p><b style=\"color:#dfff04\">Qué puedes hacer:</b> calcula embeddings con BioCLIP y compara cada foto con el promedio de su especie antes de entrenar nada.</p>", 61,
      boca="Si la línea base ya alcanza tu objetivo, no entrenes.")

hoja(titulo("Rechazar lo que no conoce") +
     '<p class="lead">Un buen sistema debe decir «no la conozco» ante una especie que no está en su catálogo. Es lo más difícil que tuvo el proyecto.</p>' +
     '<div class="g2"><div>' +
     graf("Aceptar conocidas frente a dejar pasar ajenas", C.linea([(78.5, 61.3, "78,5"), (81.5, 68.2, "81,5"), (86.4, 75.1, "86,4"), (95.3, 91.6, "95,3"), (98.8, 97.6, "98,8")], (75, 100), (40, 100), "% de conocidas aceptadas", "% de ajenas que pasan", 222, 150),
          "Cada punto es un umbral: a la derecha acepta más especies conocidas, arriba deja pasar más ajenas (Sinú) " + E("PROYECTO") + ".",
          "No hay umbral bueno: subir de 90 a 95 % de aceptadas deja pasar ~16 puntos más de ajenas.") +
     '</div><div>' +
     graf("Dos métodos de rechazo", C.vbars([{"l": "SABANAS", "l2": "MAHAL.", "v": .576, "t": "0,576"}, {"l": "SABANAS", "l2": "COSENO", "v": .826, "hi": 1, "t": "0,826"}, {"l": "SINÚ", "l2": "MAHAL.", "v": .578, "t": "0,578"}, {"l": "SINÚ", "l2": "COSENO", "v": .665, "hi": 1, "t": "0,665"}], 1, 222, 150, ""),
          "AUROC (0,5 = azar, 1 = perfecto) de Mahalanobis y de coseno + Weibull en dos regiones.",
          "La distancia simple separa mejor que la sofisticada, pero en el Sinú sigue siendo débil.") +
     '</div></div>' +
     exp("¿Se puede rechazar una rana ajena?", "Rechazo de especies desconocidas", "NO FUNCIONÓ",
         [("Se probó", "Mahalanobis, coseno, kNN, ensambles, topografía y altitud"), ("Resultado", "Entre el 61 y el 92 % de las ranas ajenas se cuelan"),
          ("Por qué", "Hay pares de especies casi idénticos en el espacio de vectores"), ("Lo que sí", "«No es una rana» se rechaza bien: solo se cuela el 4,6 %")]) +
     turno(["Separa «no es del grupo» de «es del grupo pero no la conozco».", "Elige el umbral en validación y no lo toques en test."]),
     "Rechazar lo que no conoce")

hoja(titulo("Especies gemelas: dónde se equivoca") +
     '<p class="lead">Los errores no se reparten al azar: se concentran en pocos pares de especies muy parecidas.</p>' +
     graf("Pares que más se confunden", C.hbars([{"l": "D. bogerti → D. microcephalus", "v": 8, "hi": 1}, {"l": "R. marina → R. horribilis", "v": 7, "hi": 1}, {"l": "H. tatayoi → E. prosoblepon", "v": 5},
                                               {"l": "D. columbianus → D. bogerti", "v": 5}, {"l": "C. metriosistus → C. raniformis", "v": 5}, {"l": "O. taurinus → T. macrotis", "v": 4},
                                               {"l": "N. grandisonae → E. prosoblepon", "v": 4}, {"l": "R. humboldti → R. beebei", "v": 4}], 9, 467, 146),
          "Número de fotos de prueba en que la especie de la izquierda se confundió con la de la derecha " + E("CALC") + ".",
          "Casi siempre del mismo género. Cuanto más cerca está la especie vecina, peor el acierto (correlación −0,62).") +
     exp("¿Un ajuste fino corrige los pares?", "Adaptadores ArcFace para pares gemelos", "NO FUNCIONÓ",
         [("Se probó", "Entrenar un pequeño adaptador por cada uno de los 5 pares más cercanos"), ("Resultado", "Promedio 69,2 → 69,0 %; un par bajó 20 puntos y otro subió 16"),
          ("Por qué", "Con 28–50 fotos por par, el error de muestreo es de ±12 a ±16 puntos"), ("Cambio", "El adaptador marca el par; una persona decide el grupo")]) +
     cambio("Dar siempre una especie, aunque sea un par gemelo.", "«Grupo <i>R. marina</i> / <i>R. horribilis</i>: requiere un detalle», con la clave para distinguirlas."),
     "Especies gemelas")

hoja(titulo("Lo que falló al hacerlo pequeño") +
     '<p class="lead">Meter un modelo grande en un teléfono tiene tres caminos. Solo uno funcionó.</p>'
     '<div class="g2">' +
     exp("¿Un modelo pequeño puede imitar al grande?", "Destilación a MobileNetV3", "NO FUNCIONÓ",
         [("Se probó", "Un alumno pequeño aprende a imitar a BioCLIP"), ("Resultado", "57,7 → 24,3 % (−33,4 pp)"),
          ("Por qué", "Tenía que aprender «qué es una rana» y «cuál» a la vez, con la rana en el 10 % de la foto"), ("Sí quedó", "La coherencia taxonómica se transfirió")]) +
     exp("¿Se puede usar enteros de 8 bits?", "Cuantización INT8", "NO FUNCIONÓ",
         [("Se probó", "Cinco herramientas distintas"), ("Resultado", "Entre 0,2 y 51 %"),
          ("Por qué", "Los ViT tienen valores atípicos tras LayerNorm y softmax"), ("Cambio", "Solo con entrenamiento consciente de cuantización")]) +
     exp("¿Y con media precisión?", "FP16 en ONNX", "FUNCIONÓ",
         [("Se probó", "Torre de imagen, opset 18, batch 1, FP16"), ("Resultado", "165,6 MB; predicciones idénticas; coseno 0,999999"),
          ("Ojo", "No gana velocidad en CPU, solo tamaño"), ("Cambio", "Es el formato del móvil")]) +
     exp("¿La exportación avisa si falla?", "ONNX en silencio", "NO FUNCIONÓ",
         [("Pasó", "Con opset 17 salió un archivo de 1,2 MB sin ningún error"), ("Por qué", "Una conversión corrompió el grafo"),
          ("Cambio", "Verificar tamaño y predicciones idénticas tras exportar")]) +
     '</div><div class="sp"></div>' +
     bocadillo("Antes de optimizar un ViT, lee la literatura: el fallo de INT8 ya estaba documentado.", expresion="serio", forma="cubo"),
     "Lo que falló al hacerlo pequeño")

hoja(titulo("Quince lecciones") +
     '<p class="lead">El resumen del capítulo: lo que este proyecto enseña a cualquier otro.</p>' +
     tabla([["#", "Lección", "Evidencia"],
            ["1", "Mide una línea base sin entrenar antes de construir nada", "70,4 % sin entrenar frente a 69,2 %"],
            ["2", "Quitar el fondo no ayudó", "60,7 → 50,7 → 44,7 %"],
            ["3", "El contexto es la mayor ganancia y el mayor riesgo", "+15 a +25 pp; volteó un acierto"],
            ["4", "Filtrar por región mejora la precisión", "+11,8 pp"],
            ["5", "Los ViT no se cuantizan a INT8 sin reentrenar", "0,2–51 %"],
            ["6", "La destilación a un modelo pequeño falló", "57,7 → 24,3 %"],
            ["7", "Una distancia simple rechaza mejor que Mahalanobis", "AUROC 0,69 frente a 0,59"],
            ["8", "El rechazo de desconocidos no está resuelto", "61–92 % se cuelan"],
            ["9", "Una evaluación se contamina sin querer", "100 % del test en train"],
            ["10", "Un resultado perfecto suele ser una trampa", "AUROC 1,0 sobre los mismos datos"],
            ["11", "Separa «no es una rana» de «rana que no conozco»", "Una se separa limpio; la otra no"],
            ["12", "La exportación a ONNX falla en silencio", "1,2 MB sin error"],
            ["13", "Las especies raras se salvan con la taxonomía", "27 de 28 cubiertas"],
            ["14", "La documentación se desincroniza", "«BioCLIP 2.5 no existe» era falso"],
            ["15", "Reporta siempre con condiciones", "Especies, división, n, versión"]], [5, 57, 38], "sm") +
     turno(["Escribe cada experimento con su pregunta antes de correrlo.", "Anota especies, fotos, división y versión.", "Guarda también lo que falló, con la causa.", "Deja escrito el cambio que tomaste."]),
     "Quince lecciones")

# =====================================================================================
# CAP 05 · CONTEXTO
# =====================================================================================
apertura(5, "Contexto", ["Cuando la imagen", "ya no alcanza"],
         "Vas a aprender a usar lugar, fecha y hospedero para ordenar candidatas, sin dejar que decidan solos.", ["LUGAR", "HOSPEDERO", "ÉPOCA", "ACOTADO"], 41)

hoja(titulo("El contexto dinámico") +
     '<p class="lead">El lugar, la fecha o el cultivo cambian qué especies son probables. Pero una especie endémica y una presente en todas partes no se tratan igual.</p>' +
     aprende(["Cómo combinar foto y lugar.", "Por qué el prior debe ser dinámico y acotado."]) +
     '<div class="g2"><div>'
     f'<p>Mac Aodha et al. 2019 {E("FUENTE")}: P(clase | imagen, lugar) ∝ P(clase | imagen) · P(clase | lugar). En iNat2018 el top-1 pasó de 60,2 a <b>72,7</b>. Donde los datos no tienen estructura geográfica, no ayuda.</p>'
     '<p>SINR (Cole et al. 2023) aprende un mapa por especie: con 10 ejemplos ya supera a una cuadrícula con todos los datos.</p>'
     '</div><div>' +
     graf("Escala del prior por especie · ilustración", C.prior(222),
          "Cuánto multiplica el prior a una especie según la distancia a sus observaciones.",
          "La endémica pesa mucho cerca y poco lejos; la amplia, casi igual en todas partes. Nunca baja de 0,5.") +
     '</div></div>' +
     tabla([["#", "Regla del diseño dinámico"],
            ["1", "Escala por especie calculada de los datos, nunca fija"],
            ["2", "Perfiles editables: generalista 80/10/10, microendémica 30/60/10, par críptico 35/35/30"],
            ["3", "Prior acotado: nunca elimina una especie; la oficial sale del voto visual"],
            ["4", "«No observado» no es «ausente»: tres estados"],
            ["5", "Recalcular en cada versión y evaluar sin usar la especie real como entrada"]], [6, 94], "sm") +
     cambio("Prior sin límite: multiplicaba la probabilidad hasta 5 veces.", "Prior acotado entre 0,5 y 1,5 que solo reordena alternativas."),
     "El contexto dinámico")

hoja(titulo("Especies casi idénticas") +
     '<p class="lead">Muchas especies de anuros se ven casi iguales aunque sean distintas. El par que más se confunde en Anura es este.</p>'
     '<div class="g2">' +
     foto("dimorfismo/rhinella_marina_hembra.jpg", 150, "<b><i>Rhinella marina</i></b>, hembra. Bernard Dupont, CC BY-SA 2.0.") +
     foto("pares/rhinella_horribilis_1.jpg", 150, "<b><i>Rhinella horribilis</i></b>. Foto del proyecto Anura.") +
     '</div><div class="c2">'
     f'<p>Coseno entre sus centroides: <b>0,980</b>, el par más cercano de las 56 especies. Sus altitudes se solapan (25–2.500 m frente a 4,5–2.467 m): ni la geografía ni la altitud las separan {E("PROYECTO")}.</p>'
     '<p>La diversidad críptica es grande: <i>Engystomops</i> pasó de 2 especies a 5–7 y <i>Boana</i> de 2 a 6–9 (Funk et al. 2012).</p>'
     '<h3>Qué las separa</h3>'
     f'<p>En <i>Pristimantis</i> y <i>Dendropsophus</i> hay caracteres con fuente {E("FUENTE")}: el iris, los colores ocultos de ingle y muslo, la membrana entre los dedos y, sobre todo, el <b>canto</b> y el ADN (16S).</p>'
     '<p>Solo ayudan si la foto los muestra. Si no se ven, pide otra foto o un canto.</p>'
     '</div>' +
     turno(["Haz la lista de tus pares gemelos con la matriz de confusión.", "Para cada par, escribe qué rasgo los separa y si se ve en foto.",
            "Avisa al usuario cuando la respuesta cae en un par.", "Pide el dato que desempata: otra foto, el canto, el lugar."]),
     "Especies casi idénticas")

verde("05", "El contexto reordena candidatas. Nunca decide solo.",
      "<p>En Anura, un prior sin acotar volteó una <i>D. bogerti</i> bien identificada a <i>D. truncatus</i>, con una razón de prior de casi 5 veces.</p>"
      "<p>Desde entonces la especie oficial sale del voto visual, y el lugar solo cambia el orden y el porcentaje.</p>", 43,
      boca="Los registros más valiosos son los que aparecen donde no se esperaba.")

hoja(titulo("Etapa, sexo y edad") +
     '<p class="lead">La etapa tiene escalas estándar para etiquetar; el sexo depende de la especie; la edad casi nunca sale de una foto.</p>' +
     graf("Escalas de etapa: Gosner y BBCH", C.gosner_bbch(467),
          "Los 46 estadios de los renacuajos (Gosner 1960) y los 10 de las plantas (BBCH, Meier 2001), leídos en el original.",
          "Usa la escala del grupo como etiqueta. En anuros, los estadios 26–40 son la mejor ventana para fijar la etapa en foto.") +
     '<div class="fotos" style="grid-template-columns:repeat(4,1fr)">' +
     foto("renacuajos/bufo_02_renacuajos.jpg", 64, "Renacuajo. A. Karwath, CC BY-SA 2.5.") +
     foto("renacuajos/bufo_03_renacuajos_patas_traseras.jpg", 64, "Patas traseras. C. Fischer, CC BY-SA 3.0.") +
     foto("renacuajos/bufo_04_metamorfo_con_cola.jpg", 64, "Metamorfo. J. Lindsey, CC BY-SA 3.0.") +
     foto("renacuajos/bufo_05_juvenil.jpg", 64, "Juvenil. Syrio, CC BY-SA 4.0.") +
     '</div><div class="c2">'
     '<h3>Sexo</h3><p>En anuros las hembras suelen ser más grandes; ayudan el saco vocal, las almohadillas nupciales y el amplexo. En <i>R. marina</i> el macho adulto es más pequeño y amarillento, pero un macho inmaduro también es manchado: el color solo no sexa.</p>'
     '<h3>Edad</h3><p>Se cuentan líneas de crecimiento en las falanges; la talla no es fiable. Una guía solo puede ofrecer <b>clases de edad</b>: cría, joven, adulto.</p>'
     '</div>',
     "Etapa, sexo y edad")

hoja(titulo("Enfermedad en fauna y flora") +
     '<p class="lead">Una foto muestra síntomas, no la causa. La respuesta correcta es «compatible con X; confirmar en laboratorio».</p>' +
     '<div class="g2"><div>' +
     graf("Laboratorio frente a campo", C.vbars([{"l": "LABORATORIO", "v": 99.35, "hi": 1, "t": "99,35%"}, {"l": "CAMPO 1", "v": 31.40, "t": "31,40%"}, {"l": "CAMPO 2", "v": 31.69, "t": "31,69%"}], 100, 222, 140),
          "Acierto de un modelo de enfermedades de plantas en su propio test y con fotos tomadas en otras condiciones (Mohanty 2016).",
          "Un test que comparte condiciones con el entrenamiento engaña: el acierto real fue un tercio.") +
     '</div><div>'
     '<h3>Qué ayuda en plantas</h3><p>Clasificar <b>lesiones individuales</b> subió la exactitud media un 12 % (Barbedo 2019). También ayudan varias fotos, varios órganos y el contexto.</p>'
     '<h3>Hongos</h3><p>Nunca uses una foto para decidir si algo se come: la mejor de tres apps acertó el 49 % y confundió <i>Amanita phalloides</i>.</p>'
     '</div></div>' +
     tabla([["Grupo", "Signos visibles", "Confirmación"],
            ["Anuros", "Letargo, muda anormal, enrojecimiento: inespecíficos", "qPCR, histología; sin ML publicado"],
            ["Aves", "Viruela aviar, conjuntivitis", "Laboratorio"], ["Mamíferos", "Sarna, nariz blanca en murciélagos", "Laboratorio"],
            ["Abejas", "Varroa, loque, cría de tiza", "Laboratorio; varroa F1 0,874"], ["Plantas", "Manchas, clorosis, marchitez, roya", "PCR o cultivo"]], [14, 52, 34], "sm") +
     turno(["Prueba tu modelo con fotos de campo, no solo con el test.", "Devuelve «compatible con…» y la confirmación necesaria."]),
     "Enfermedad en fauna y flora")

hoja(titulo("Del animal a la flora") +
     '<p class="lead">La guía es de animales, pero casi todo se traslada a las plantas con pocos cambios.</p>' +
     tabla([["En animales", "En flora", "Particularidad"],
            ["Rango fácil de separar", "Familia o género con rasgo visible", "Varios órganos ayudan"],
            ["Etapa (renacuajo, larva)", "BBCH: germinación → senescencia", "Diez estadios principales"],
            ["Sexo", "Flores masculinas, femeninas o hermafroditas", "Solo el principio"],
            ["Edad", "Anillos", "Requiere muestra"],
            ["Salud", "Síntomas en hoja, rama o planta", "Laboratorio 99 % → campo 31 %"],
            ["Prior de lugar", "Región, altitud, cultivo y hospedero", "EPPO, CABI, Plantwise"],
            ["Plaga como contexto", "Insecto vector → enfermedad", "Trips y TSWV (capítulo 06)"]], [26, 38, 36]) +
     exp("¿Fusionar varias fotos de la misma planta ayuda?", "Varias vistas de una planta", "FUNCIONÓ",
         [("Se midió", "101 especies, con una foto o con varias perspectivas (Plant Methods 2019)"), ("Resultado", "Top-1 del 77 % con la planta entera al 97 % fusionando todas las vistas"),
          ("Lección", "Pedir varios órganos es la versión vegetal de «pide otra foto»")]) +
     '<div class="sp"></div><p>Para plantas, un modelo de biodiversidad ayuda menos que uno de enfermedades: BioCLIP 2 saca 40,4 en PlantDoc.</p>',
     "Del animal a la flora")

hoja(titulo("Método por organismo y por pregunta") +
     '<p class="lead">La tabla de decisión del capítulo: tu organismo, tu pregunta y el método que la evidencia respalda.</p>' +
     tabla([["Organismo", "Especie", "Etapa", "Sexo", "Edad", "Salud", "Método principal", "Contexto"],
            ["Anuros", "<b>F</b>", "P", "P", "L", "P / L", "Embeddings + centroides; paquete regional", "Lugar, altitud, canto"],
            ["Aves", "F", "F", "P", "P", "P", "Foto + canto", "Fecha y lugar"],
            ["Mamíferos", "F", "P", "P", "P", "P / L", "Detector → clasificador", "Sitio"],
            ["Reptiles", "P", "P", "P / L", "L", "—", "Foto + caracteres", "Localidad"],
            ["Peces", "P", "—", "—", "—", "P", "Foto en acuario o cultivo", "Hábitat"],
            ["Insectos", "P", "F", "P", "—", "—", "Foto + hospedero", "EPPO, CABI"],
            ["Plantas", "F", "F", "P", "L", "P / L", "Varios órganos", "Región"],
            ["Hongos", "P", "P", "—", "—", "—", "Foto + ADN", "Sustrato"]], [12, 9, 8, 8, 8, 9, 26, 20], "sm") +
     '<p style="font-size:8.2pt;color:#333"><b>F</b> factible desde una foto · <b>P</b> parcial · <b>L</b> requiere laboratorio · — sin evidencia encontrada.</p>'
     '<div class="sp"></div><h2>Cómo elegir, en cinco preguntas</h2>'
     '<div class="c2">' +
     paso(1, "¿Qué quieres saber?", "Especie, etapa, sexo, edad o salud.") + paso(2, "¿Se ve?", "Si no, laboratorio o clase de edad.") +
     paso(3, "¿Cuántas fotos?", "Sigue la ruta de método del capítulo 02.") + paso(4, "¿La foto alcanza?", "Si no, pide otra o cambia de pregunta.") +
     paso(5, "¿Hay gemelas?", "Documenta los pares, usa contexto acotado y baja de rango.") +
     '</div>',
     "Tabla de decisión")

# =====================================================================================
# CAP 06 · FRANKLINIELLA
# =====================================================================================
apertura(6, "Frankliniella", ["Caso conductor:", "los trips"],
         "Vas a aplicar todo lo anterior a un insecto real: reconocer su etapa en una foto y recomendar el manejo.", ["HUEVO", "LARVA", "PUPA", "ADULTO"], 29)

hoja(titulo("El ciclo de vida del trips") +
     '<p class="lead">La etapa decide qué se ve en una foto y qué control llega al insecto.</p>' +
     graf("Ciclo de Frankliniella occidentalis", C.ciclo_trips(467),
          "Días de cada etapa a 27 °C (UF/IFAS) y ciclo completo según la temperatura (EPPO). En lima, las etapas visibles con macro.",
          "Huevo, prepupa y pupa están ocultos: tendrás muchas fotos de adultos y muy pocas de esas etapas.") +
     tabla([["Etapa", "Tamaño y aspecto", "Dónde está", "¿Se ve en foto?"],
            ["Huevo", "Dentro del tejido vegetal", "Hojas, pétalos", "Casi nunca; solo el daño"],
            ["Larva I", "&lt; 1 mm (~0,56 mm), incolora o blanca", "Hojas y flores", "Sí, con macro"],
            ["Larva II", "~0,86–1 mm, amarillo dorado", "Hojas y flores", "Sí, con macro"],
            ["Prepupa", "Esbozos alares cortos; antenas hacia delante", "Suelo; a veces en la flor", "Difícil"],
            ["Pupa", "Esbozos largos; antenas dobladas hacia atrás", "Suelo; a veces en la flor", "Difícil"],
            ["Adulto", "&lt; 2 mm (1,2–1,4 mm); alas con flecos", "Flores y hojas", "Sí, con macro"]], [13, 38, 27, 22], "sm") +
     turno(["Si una etapa no alcanza, fusiónala con la vecina (prepupa + pupa).", "Fotografía con macro, escala, fondo neutro y luz uniforme.",
            "Usa trampas azules o amarillas para los adultos.", "Etiqueta la etapa en cada foto: las fuentes públicas no la traen."]),
     "El ciclo de vida del trips")

hoja(titulo("Identificar un trips cuando la foto no basta") +
     '<p class="lead">La especie requiere microscopio. La foto da la etapa y el género; el contexto ayuda a ordenar candidatos.</p>' +
     '<div class="c2">'
     '<h3>Lo que exige microscopio</h3><p><i>Frankliniella</i> tiene antena de 8 segmentos (<i>Thrips</i>, 7). Las especies se separan por setas y por el peine del segmento VIII: «tarea de expertos» (EPPO). Por eso el modelo de etapa debe ser independiente de la especie.</p>'
     '<h3>Sexo</h3><p>Los machos salen de huevos no fecundados y son más pequeños y pálidos; hay unas 4 hembras por macho (EPPO). «Pequeño y pálido» no es otra especie.</p>'
     '<h3>Hospedero</h3><p><i>F. occidentalis</i> tiene 244 hospederos de 62 familias: el hospedero reordena, no confirma.</p>'
     '<h3>Daño</h3><p>Plateado y un punteado de excremento <b>verde oscuro</b>; los ácaros dejan gránulos negros.</p>'
     '<h3>Trampa</h3><p>Las azules capturan más <i>F. occidentalis</i>; una feromona sesga la captura, pero no prueba la especie.</p>'
     '<h3>Lugar</h3><p>En La Ceja (Antioquia), la especie más frecuente en crisantemo fue <i>F. panamensis</i>.</p>'
     '</div>' +
     tabla([["Especie", "¿Vector de TSWV?", "Pista de contexto"],
            ["<i>F. occidentalis</i>", "Sí, el más eficaz", "Ornamentales; domina en la Sabana de Bogotá"],
            ["<i>F. fusca</i>", "Sí", "Principal vector en maní (EE. UU.)"],
            ["<i>F. schultzei</i>", "Sí", "Difícil de separar de <i>F. occidentalis</i>"],
            ["<i>F. tritici</i>, <i>T. palmi</i>", "No competentes", "Si hay síntomas de TSWV, no son la causa"]], [22, 26, 52], "sm") +
     cambio("«Trips en crisantemo de Antioquia» = <i>F. occidentalis</i>.", "Especie por microscopio; foto para etapa y género; contexto solo para ordenar."),
     "Identificar por contexto")

verde("06", "La foto da la etapa y el género. La especie la confirma el microscopio.",
      "<p>El contexto (cultivo, sitio, trampa, tipo de daño) reordena candidatos, pero nunca decide solo.</p>"
      "<p>Etiqueta la variación dentro de la especie: sexo, forma de color y etapa. Es lo que más confunde a un clasificador visual.</p>", 99,
      boca="Pequeño y pálido puede ser un macho, no otra especie.")

hoja(titulo("De la etapa al manejo") +
     '<p class="lead">La etapa decide qué control llega. Esta guía da principios por etapa, no recetas ni dosis.</p>' +
     '<div class="c2">'
     '<h3>Qué llega a cada etapa</h3><p>Los huevos están dentro del tejido, y la prepupa y la pupa en el suelo: un tratamiento foliar no los alcanza. Larvas y adultos están expuestos.</p>'
     '<h3>Opciones habituales</h3><p>Cultural; biológico (ácaros <i>Amblyseius</i>, chinche <i>Orius</i>, hongos <i>Beauveria</i> y <i>Metarhizium</i>, nematodos contra pupas) y químico, con <b>resistencia documentada</b> en <i>F. occidentalis</i>.</p>'
     '<h3>La etapa también es riesgo</h3><p>Solo las larvas adquieren el virus del bronceado del tomate (TSWV); los adultos lo transmiten 3 a 10 días después (EPPO).</p>'
     '<h3>Siempre</h3><p>Consulta al agrónomo y la norma vigente del ICA. En flores de exportación el umbral puede ser cero.</p>'
     '</div><h2>Resumen operativo para el estudiante</h2>' +
     tabla([["#", "Paso"], ["1", "Fija el alcance (género <i>Frankliniella</i> o trips) con un rasgo visible"],
            ["2", "Esquema de etiquetas con etapa, sexo, sitio e individuo"],
            ["3", "Línea base con BioCLIP congelado: ¿separa las etapas?"],
            ["4", "Si falta una etapa, escalera de pocas imágenes y fusión"],
            ["5", "Contexto dinámico: cultivo, región, época, síntomas"],
            ["6", "Devolver etapa + confianza + manejo general, y cuándo pedir otra foto"]], [6, 94], "sm") +
     bocadillo("Insecto vector + síntomas en la planta: sube la sospecha del virus que transmite, pero confírmalo en laboratorio.", expresion="pensando", forma="flor"),
     "De la etapa al manejo")

# =====================================================================================
# CAP 07 · DESPLIEGUE
# =====================================================================================
apertura(7, "Despliegue", ["Del modelo", "al telefono"],
         "Vas a aprender a elegir entre Kotlin, React Native, Flutter o un servidor, y qué debe devolver la app.", ["KOTLIN", "REACT NATIVE", "FLUTTER", "SERVIDOR"], 17)

hoja(titulo("Elegir el stack") +
     '<p class="lead">La pregunta que decide: ¿habrá conexión donde se toma la foto?</p>' +
     graf("Dos arquitecturas", C.stack_diagrama(467),
          "Arriba, todo en el teléfono con BioCLIP 1 en ONNX. Abajo, el móvil captura y un servidor con GPU analiza con BioCLIP 2.5.",
          "Lo local funciona sin red; el servidor da el modelo grande y se actualiza sin publicar la app.") +
     tabla([["Opción", "Piezas habituales", "A favor", "En contra"],
            ["<b>Kotlin nativo</b>", "ONNX Runtime para Android, CameraX, SQLite (+ sqlite-vec)", "Sin conexión; es lo que usó Anura", "Solo Android; modelo de 165,6 MB aparte"],
            ["<b>React Native</b>", "<code>onnxruntime-react-native</code>, cámara nativa", "Android e iOS; equipo web", "Preprocesado nativo e idéntico"],
            ["<b>Flutter</b>", "Plugin de ONNX Runtime, <code>camera</code>", "Dos plataformas; buena interfaz", "Plugins de terceros"],
            ["<b>Cliente + servidor</b>", "App que envía foto, GPS y fecha a una API (p. ej. FastAPI) con BioCLIP 2.5", "Modelo grande y actualizable", "Red, latencia, coste, privacidad"],
            ["<b>Híbrido</b>", "BioCLIP 1 local y reenvío al servidor con red", "Funciona en campo y mejora con red", "Dos modelos y dos contratos"]], [17, 35, 25, 23], "sm"),
     "Elegir el stack")

hoja(titulo("Cómo decidir y qué vale en cualquier stack") +
     '<p class="lead">Tres preguntas eligen el stack. Cuatro reglas valen para todos.</p>' +
     '<div class="c2">' +
     paso(1, "¿Hay conexión en campo?", "Si no, todo local. Si sí, el servidor da el modelo grande.") +
     paso(2, "¿Qué sabe el equipo?", "Kotlin, JavaScript o Dart: usa lo que ya domina. El modelo es el mismo archivo ONNX.") +
     paso(3, "¿Hace falta el modelo grande?", "Especies muy parecidas o plantas: servidor o híbrido.") +
     '<p>Para los trips, con laboratorio e internet, el cliente + servidor suele bastar: el teléfono es solo la herramienta de entrada.</p>'
     '<h3>Exportar sin sorpresas</h3><p>Opset 18, batch fijo = 1, pesos en un solo archivo, FP16 con entradas y salidas en FP32.</p>'
     '<h3>Servidor caliente</h3><p>Modelo descargado una vez con <code>HF_HOME</code>, <code>HF_HUB_OFFLINE=1</code>, proceso cargado y textos precalculados.</p>'
     '<h3>Qué devuelve la app</h3><p>Top-3 con porcentaje, el nivel alcanzado y cuándo pedir otra foto.</p>'
     '</div>' +
     exp("¿Da lo mismo en el teléfono que en Python?", "Prueba de punta a punta", "A MEDIAS",
         [("Se hizo", "64 fotos en Python y en ONNX: predicciones idénticas"), ("Falta", "La prueba en un teléfono real nunca se completó"),
          ("Cambio", "Ninguna versión se publica sin la prueba en el dispositivo")]) +
     bocadillo("Antes de publicar, pasa las mismas fotos por Python y por el teléfono: deben dar exactamente lo mismo.", expresion="alerta", forma="flor"),
     "Cómo decidir el stack")

verde("07", "No es un diagnóstico. Es una sugerencia con su nivel de confianza.",
      "<p>Enfermedad, edad y sexo dudosos se devuelven como «compatible con…». Nunca uses una foto para decidir si un hongo se come.</p>"
      "<p>Oculta las coordenadas de especies amenazadas y avisa a la autoridad las enfermedades de notificación obligatoria.</p>", 55,
      boca="Un falso conocido contamina la ciencia; un falso desconocido solo molesta.")

hoja(titulo("Varias preguntas a la vez y saber decir «no sé»") +
     '<p class="lead">Un mismo modelo puede responder especie, etapa y sexo. Lo importante es que también sepa cuándo no responder.</p>' +
     aprende(["Cómo organizar varias preguntas sobre un solo encoder.", "Qué técnicas ayudan a abstenerse.", "Cómo evaluar sin engañarte."]) +
     '<div class="c2">'
     '<h3>Una base, varias cabezas</h3><p>Un encoder (BioCLIP) y cabezas ligeras por pregunta. Es una hipótesis apoyada en BioCLIP 2, no un resultado probado.</p>'
     '<h3>Saber decir «no sé»</h3><p>Calibración por temperatura (Guo 2017), clasificación selectiva (Geifman y El-Yaniv 2017) y conjunto abierto (Vaze 2021). Elige el umbral en validación y repórtalo en test sin tocarlo.</p>'
     '<h3>Rechazo jerárquico</h3><p>«Familia Hylidae, género probable <i>Boana</i>» vale más que «desconocido».</p>'
     '<h3>Cámaras trampa</h3><p>Detector primero, clasificador después; el rendimiento cae en sitios nuevos (Beery 2018).</p>'
     '<h3>Evaluación</h3><p>Por individuo y por sitio; con condiciones; AUROC para el rechazo; calibración (ECE).</p>'
     '</div>' +
     exp("¿Un resultado perfecto es buena noticia?", "AUROC 1,0", "NO FUNCIONÓ",
         [("Pasó", "El detector se ajustó con los mismos datos con que se evaluó"), ("Resultado", "AUROC 1,0 y 0 % de falsos aceptados"),
          ("Real", "Con datos limpios: AUROC 0,59"), ("Cambio", "Ajustar en un conjunto, evaluar en otro, nunca en el mismo")]) +
     turno(["Calibra antes de fijar el umbral.", "Reporta lo que se acepta y lo que se cuela."]),
     "Multi-pregunta y calibración")

hoja(titulo("Glosario") +
     '<div class="c2" style="font-size:9pt">' + "".join(f"<p><b>{a}.</b> {b}</p>" for a, b in [
         ("Aumentación", "Variaciones artificiales de una foto (volteo, color, recorte) para entrenar con más variedad"),
         ("AUROC", "Qué tan bien separa un detector dos grupos; 0,5 es azar y 1 es perfecto"),
         ("Centroide", "El vector medio de las fotos de una clase; cada foto nueva se compara con él"),
         ("Contrato de embedding", "Hash del encoder + dimensión + preprocesado + normalización: lo que hace comparables dos vectores"),
         ("Embedding (vector)", "La representación numérica de una foto que produce el encoder"),
         ("Encoder congelado", "Se usa el modelo preentrenado sin cambiar sus pesos"),
         ("FAR / KAR", "Desconocidas aceptadas por error / conocidas aceptadas"),
         ("FP16", "Números de media precisión: el modelo ocupa la mitad"),
         ("Gosner", "Escala de 46 estadios del desarrollo de anuros"),
         ("kNN", "Clasificar por los vecinos más cercanos en el espacio de vectores"),
         ("LP-FT", "Entrenar primero una capa lineal y después todo el modelo"),
         ("ONNX", "Formato para correr el modelo fuera de Python, también en el móvil"),
         ("Parada temprana", "Guardar el modelo en la época en que la validación es mejor"),
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
     '<p>Stevens et al. 2024, <i>BioCLIP</i>, CVPR (arXiv 2311.18803). Gu et al. 2025, <i>BioCLIP 2</i>, NeurIPS (arXiv 2505.23883). Fichas de Hugging Face: imageomics/bioclip, bioclip-2, bioclip-2.5-vith14. Perfil de modelos de OpenCLIP. Kumar et al. 2022, ICLR (arXiv 2202.10054). Wortsman et al., WiSE-FT (arXiv 2109.01903). Hinton et al. 2015. PTQ4ViT (arXiv 2111.12293); RepQ-ViT (arXiv 2212.08254). Xiao et al. (arXiv 2006.09994). Northcutt et al. 2021.</p>'
     '<p>Mac Aodha, Cole y Perona 2019, ICCV. Cole et al. 2023, SINR. Guo et al. 2017; Geifman y El-Yaniv 2017; Vaze et al. 2021; Beery et al. 2018.</p>'
     '<h3>Datos y herramientas</h3>'
     '<p>Documentación de las API de iNaturalist, GBIF y MediaWiki; iNaturalist Open Data (AWS). Mohanty, Hughes y Salathé 2016. Barbedo 2019. IP102 (CVPR 2019). Plant Methods 2019. Pl@ntNet. AmphibiaWeb.</p>'
     '<h3>Biología</h3>'
     '<p>Gosner 1960, <i>Herpetologica</i> 16. Meier 2001, monografía BBCH. Funk et al. 2012 y Bell y Zamudio 2012, <i>Proc. R. Soc. B</i>. Lynch y Suárez 2011, <i>Caldasia</i>. AmphibiaWeb (<i>Rhinella marina</i>).</p>'
     '<p>EPPO Global Database, ficha FRANOC. UF/IFAS EDIS IN1089 e IN401. Hamilton, Hall y Kirk 2005, <i>J. Chem. Ecol.</i> Revista Colombiana de Entomología y Agronomía Colombiana.</p>'
     '<h3>Proyecto Anura</h3>'
     '<p>Cifras de la base de producción (v5, 56 especies) y de los informes de septiembre de 2026: <code>teoria/anura-hallazgos.md</code>.</p>'
     '<h3>Fotos</h3>'
     '<p>Wikimedia Commons: Bernard Dupont (CC BY-SA 2.0); André Karwath (CC BY-SA 2.5); Christian Fischer (CC BY-SA 3.0); James Lindsey (CC BY-SA 3.0); Syrio (CC BY-SA 4.0). <i>R. horribilis</i>: proyecto Anura.</p>'
     '<h3>Tipografía</h3>'
     '<p>Aquire (freeware, uso no comercial), Bricolage Grotesque y JetBrains Mono (OFL).</p>'
     '</div>',
     "Fuentes y créditos")
