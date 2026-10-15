# Prompt para generar el PDF (sesión en la nube, repo Mogollo7/guia)

Pega esto como primer mensaje en una sesión de Claude Code con este repo:

---
Lee completo `teoria/CONTINUAR.md`, `teoria/guia.md` (Partes 1 a 5; tabla de contenido definitiva en §33; pendientes en §34; la Parte 5, §35–§37, integra insectos por contexto, Gosner, BBCH, FLOPs, datos de gráficos y la lista de gráficos por dibujar) y `teoria/anura-hallazgos.md` (Parte A y Parte B). Después lee `research_notes/*/*.md` (fuentes) y mira `teoria/imagenes/` (`renacuajos/`, `dimorfismo/`, `pares/`; atribuciones en `creditos.csv`; cita autor y licencia en cada pie de foto) y `teoria/graficos-datos.html`.

Objetivo: PDF A4 «Guía de IA: cómo hacer que un modelo distinga animales», teoría de cómo desarrollar un modelo que identifique especie, etapa, sexo y salud usando contexto. Lectores: estudiantes; caso conductor Frankliniella (trips, §32). Sin app, sin PNG de portada (portada solo tipográfica, sin mascota).

Reglas (CONTINUAR.md §3, no reabrir): negro #0b0d12, lima #dfff04 (nunca como texto sobre blanco), papel blanco; títulos en Aquire (`teoria/fonts/`, solo mayúsculas sin tildes); bloques con esquinas interiores cóncavas (radio 44 pt); fondo de glifos grises (◎ ✕ □ + ·) nunca bajo texto; mascota con bocadillo solo en notas extra; sin neón, scanlines, glitch ni sombras; hojas normal / verde / negra de apertura / tablero, todas con cabecera y pie HUD. Cifras sin dato: «dato pendiente». Estimaciones solo con la marca «SIMULACIÓN». Respeta las etiquetas [FUENTE]/[INF]/[SIN FUENTE] de guia.md.

Haz: 1) sigue la tabla de §33; 2) redacta cada sección desde su § de origen; 3) usa los gráficos de `graficos-datos.html` y dibuja con SVG/CSS los de la tabla de guia.md §37 (línea de vida del trips, especie×etapa×sexo, fine-tuning vs congelado, escalera de pocas imágenes, escala del prior, laboratorio vs campo, cómputo de BioCLIP, árbol taxonómico, pipeline) con los datos de §36.7; 4) donde falte una imagen escribe «IMAGEN NECESARIA»; 5) renderiza el PDF a `salida/guia.pdf` (HTML + Chromium/WeasyPrint) y revisa páginas; 6) al final lista qué quedó pendiente.
---

## Estado (a 2026-10-15)

**Hecho**
- Notas de insectos por contexto y vacíos cerrados integradas en `guia.md` Parte 5 (§35–§37): hospedero, daño, trampas, ML imagen+contexto, trips, Gosner, BBCH, FLOPs, Pl@ntNet/iNaturalist, datos de gráficos.
- Fotos en el repo: `renacuajos/` (9), `dimorfismo/` (9, incluye *R. marina* macho, hembra y macho 2), `pares/rhinella_horribilis_1.jpg`. Con esto el par *R. marina*/*R. horribilis* tiene foto de ambas.

**Sigue abierto (el PDF debe escribir «dato pendiente» o «IMAGEN NECESARIA»)**
- Fotos: síntomas en planta y trips (huevo, larva, prepupa, pupa, adulto, daño); no están en el repo. Más fotos de *R. horribilis* si se quiere más de una.
- Gráficos de §37: no existen aún; los dibuja la sesión del PDF.
- Tamaños de larva II, prepupa y pupa de trips: fuentes en conflicto (guia.md §35.6). Norma ICA para *F. occidentalis*: no verificada (§35.7).
- Fuentes marcadas [snippet] en la Parte 5 salen de resúmenes de búsqueda: no las cites como «leído» sin revisarlas; verifica también el orden de columnas de ImageNet en Kumar 2022 y el desglose 31+91 de Bell y Zamudio.
- Contradicción de fuentes sobre dimorfismo en *R. marina* (AmphibiaWeb frente a ADW), guia.md §36.2.
- Siguen sin leerse ~100 notas de app/diseño y las fases 11, 12, 14, 15 y 18 (guia.md §34 punto 8).
