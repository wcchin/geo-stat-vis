# Geospatial Statistics and Visualisation

An open, self-study book for understanding geographical patterns through **statistical reasoning, spatial analysis and visualisation**.

**Read the book:** https://wcchin.github.io/geo-stat-vis/

This resource connects concepts, geographical examples, figures, self-check activities and Python notebooks. It is intended for students, educators and practitioners, whether reading systematically or consulting individual topics.

## Contents

- **Part 1 — Core Chapters:** geographical thinking, spatial data, statistical patterns, point patterns, areal patterns and geovisualisation.
- **Part 2 — Worked Examples:** applied demonstrations connecting methods to geographical questions.
- **Part 3 — Data and Notebooks:** Python notebooks and related data for selected analyses.
- **Part 4 — Lecture Slides:** supplementary lecture material from the original course context.

## Origins

Developed and maintained by **Benny Chin**, Department of Geography, National University of Singapore (NUS). The materials originated in **GE5230 Geospatial Statistics and Visualisation**, part of NUS's MSc in Applied GIS programme, and have been reorganised and expanded for a wider audience. The original course connection is retained in relevant lecture slides and notebooks.

## Build locally

The book uses Jupyter Book 2 / MyST. A validated version is **Jupyter Book 2.1.7**:

```bash
npm install -g jupyter-book@2.1.7
jupyter-book build --html
```

Reproducibility checks and preparation scripts are available under `scripts/`. For development and validation details, see [the update status document](docs/2610-update-status.md).

## Licensing

© 2026 Benny Chin · Content CC BY-NC-ND 4.0 · Code MIT. See the [book homepage](src/index.md) for licence details.
