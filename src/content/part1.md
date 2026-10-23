# Core Chapters

The seven core chapters offer a route from **noticing geographical differences** to **examining evidence** and **communicating what the evidence can—and cannot—tell us**. Statistics, spatial analysis and visualisation are treated as connected forms of geographical reasoning rather than isolated techniques.

You can read the chapters in order, or use this roadmap to choose a topic and follow its links to related methods.

## A roadmap through the book

```{mermaid}
flowchart TD
    A["Chapter 1<br/>Geographical and statistical thinking"]
    B["Chapter 2<br/>Spatial data and representation"]
    C["Chapter 3<br/>Statistical patterns<br/>Compare observations and groups"]
    D["Chapters 4–5<br/>Point patterns<br/>Distribution, density and clusters"]
    E["Chapter 6<br/>Areal patterns<br/>Neighbourhood relationships"]
    F["Chapter 7<br/>Geovisualisation and storytelling"]
    A --> B
    B --> C
    B --> D
    B --> E
    C --> F
    D --> F
    E --> F
```

The middle branches are **complementary analytical perspectives**, not mandatory prerequisites for one another. A problem may call for one or several of them. Visualisation also supports exploration throughout the book; Chapter 7 returns to it explicitly as a way of explaining and communicating evidence.

## Find your starting point

| Chapter | Guiding question | Begin here |
| --- | --- | --- |
| **1. Introduction** | How do observations become geographical questions? | [Geographical and statistical thinking](chapter_1/chapter-1-intro.md) |
| **2. Spatial data** | What do our data represent, and how should we prepare them? | [Spatial data and representation](chapter_2/chapter-2-spatial_data.md) |
| **3. Statistical patterns** | How can we describe and compare groups without overstating differences? | [Statistical patterns](chapter_3/chapter-3-stat_pattern.md) |
| **4. Global point patterns** | Is an observed point distribution consistent with a reference pattern? | [Global point patterns](chapter_4/chapter-4-global_point_pattern.md) |
| **5. Local point patterns** | Where do density and clustering vary within a study area? | [Local point patterns](chapter_5/chapter-5-local_point_pattern.md) |
| **6. Areal patterns** | How are values associated across neighbouring areas? | [Areal patterns](chapter_6/chapter-6-areal_pattern.md) |
| **7. Geovisualisation** | How can we communicate findings clearly and responsibly? | [Geovisualisation and storytelling](chapter_7/chapter-7-geovisualisation.md) |

## Choosing a reading path

**New to the subject?** Start with Chapters 1 and 2, then read Chapters 3–6 to explore different forms of geographical patterns. Finish with Chapter 7 to consider how analytical choices shape the story we tell. Some longer sections offer optional deeper explanations: a first reading need not include every technical detail.

**Looking for a particular method?** Enter at the relevant chapter. For point-event clustering, start with Chapters 4 or 5; for spatial autocorrelation among areas, start with Chapter 6. Refer back to Chapter 2 whenever data representation, boundaries or scale matter.

**Teaching or reviewing?** Use the guiding questions to select chapters according to the reasoning students need to practise, rather than assuming all chapters must be taught in one fixed order.

## From reading to practice

The [worked examples](part2.md) connect geographical questions to analytical decisions and interpretation, while [data and notebooks](part3.md) provide opportunities to explore selected methods in Python. These resources complement the explanations in Part 1: you do not need to complete every practical exercise before continuing to the next chapter.
