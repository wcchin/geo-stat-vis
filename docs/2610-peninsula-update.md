# Peninsula extent, sequential income palette and layout

Baseline: main commit `c6ef98c518d688ef2ea010404f9ae84ecc6b74e8` after PR #3 was merged.

The reviewed 11-area Selangor–KL example is expanded to **92 matched areas across Peninsular Malaysia**, following comparison of 11-, 42- and 92-area map previews. The chapter keeps its existing URL and conceptual structure, replaces the real-data figures and table, and updates all scope, projection and permutation explanations. The illustrative table now lists seven selected areas; the notebook provides all 92.

Replace the green preview and original red/blue diverging map with sequential **OrRd**, using fixed RM breaks across every map. The notebook also offers `YlOrBr` as a golden alternative. Synthetic grids use sequential pale/dark colours. None of these colours indicates statistical significance.

Use portrait, two-column and three-column figure layouts with equal x/y scale, compact legends and 200 dpi exports. Reduce the standalone portrait's book width to 70%; comparisons use the full content width. Remove repeated overall headings and excess margins.

The new source snapshot records EPSG:3375 and the PLANMalaysia service's **100 m display generalization**. It compresses to about 195 KiB and is not presented as full-detail geometry. It must not be used to derive exact adjacency weights; obtain original geometry and verify topology for that later task. The notebook still computes no Moran coefficient or p-value for these data. Earlier KL snapshots and images are retained for provenance and compatibility, but are no longer active in this section.

Validation uses the offline notebook to check complete 92-area matching, seven chapter-table values, CRS, fixed breaks, sequential palette, permutation invariants, mean-income option, chain arithmetic and rejection of incomplete 2024 coverage. Existing NNA and original-illustration checks plus a full book build run in CI. Figure inspection covers tall-map proportions, labels, legend readability and comparison layout.
