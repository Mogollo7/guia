# Prompt para generar el PDF (sesión en la nube, repo Mogollo7/guia)

Pega esto como primer mensaje en una sesión de Claude Code con este repo:

---
Lee completo `teoria/CONTINUAR.md`, `teoria/guia.md` (Partes 1 a 5; tabla de contenido definitiva en §33; vacíos cerrados e insectos por contexto en §35–§37; pendientes en §34) y `teoria/anura-hallazgos.md` (Parte A y Parte B). Después lee `research_notes/*/*.md` (fuentes) y mira `teoria/imagenes/` (+ `creditos.csv` y `LEEME.md`), `teoria/graficos-datos.html` (T1–T9) y `teoria/graficos-nuevos.html` (G1–G11, ya dibujados; se pasan a SVG del PDF).

Objetivo: PDF A4 «Guía de IA: cómo hacer que un modelo distinga animales», teoría de cómo desarrollar un modelo que identifique especie, etapa, sexo y salud usando contexto. Lectores: estudiantes; caso conductor Frankliniella (trips, §32). Sin app, sin PNG de portada (portada solo tipográfica, sin mascota).

Reglas (CONTINUAR.md §3, no reabrir): negro #0b0d12, lima #dfff04 (nunca como texto sobre blanco), papel blanco; títulos en Aquire (`teoria/fonts/`, solo mayúsculas sin tildes); bloques con esquinas interiores cóncavas (radio 44 pt); fondo de glifos grises (◎ ✕ □ + ·) nunca bajo texto; mascota con bocadillo solo en notas extra; sin neón, scanlines, glitch ni sombras; hojas normal / verde / negra de apertura / tablero, todas con cabecera y pie HUD. Cifras sin dato: «dato pendiente». Estimaciones solo con la marca «SIMULACIÓN». Respeta las etiquetas [FUENTE]/[INF]/[SIN FUENTE] de guia.md.

Haz: 1) sigue la tabla de §33; 2) redacta cada sección desde su § de origen; 3) usa los gráficos de `graficos-datos.html` y `graficos-nuevos.html` (línea de vida del trips, especie×etapa×sexo, fine-tuning vs congelado, escalera de pocas imágenes, escala del prior, árbol taxonómico, pipeline, Gosner/BBCH, cómputo de BioCLIP, iNaturalist) en la paleta del PDF, sin copiar el fondo oscuro de la página; los marcados ILUSTRACIÓN o SIMULACIÓN conservan su marca; 4) donde falte una imagen escribe «IMAGEN NECESARIA»; 5) renderiza el PDF a `salida/guia.pdf` (HTML + Chromium/WeasyPrint) y revisa páginas; 6) al final lista qué quedó pendiente.
---

## Estado a 2026-10-15 (lo completado en la sesión de revisión)
- **Hecho:** §35–§37 de `guia.md` integran `research_notes/Fotos vacíos e insectos por contexto/` (crípticos, dimorfismo, Gosner, BBCH, FLOPs, Pl@ntNet/iNat, datos de gráficos, insectos por contexto, trips por especie, tamaños y conflictos). Los 11 gráficos nuevos están en `teoria/graficos-nuevos.html`. Inventario de fotos en `teoria/imagenes/LEEME.md`; el par *R. marina*/*R. horribilis* ya tiene las dos especies.
- **Falta y va como «IMAGEN NECESARIA»:** fotos de trips (todas las etapas), síntomas (plateado, punteado, TSWV), trampas, renacuajos neotropicales, mockup de la app. El entorno de esa sesión no podía bajar de Wikimedia Commons.
- **Dato pendiente (sin fuente hallada):** tamaño de prepupa y pupa de trips; si *F. occidentalis* figura en el anexo de la Res. ICA 3593/2015; dimorfismo de *R. horribilis*; método y precisión de Pl@ntNet; *Boana* y *Rhinella* crípticas por iris o ingle.
- **Fuentes por revisar:** lo marcado «snippet» viene de resúmenes de búsqueda, no del documento abierto; no citar sin comprobar.
- **Créditos por resolver:** `rhinella_marina_macho_2.jpg` tiene dos filas en `creditos.csv`; `rhinella_horribilis_1.jpg` sin autor ni licencia.
- **Preguntas abiertas al usuario (§34):** cultivo y región de los estudiantes, fotos por etapa, microscopio, alcance del «remedio», si se leen las notas de app y las fases 11, 12, 14, 15 y 18.
