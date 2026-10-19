# Semester 2610 book update

This branch contains the first integrated pilot of the book update. The book remains organised by topic, while lecture slides retain their semester and week labels.

## Included in this batch

- Correct the quadrat chi-squared equation and distinguish upper-tail inference from a test of regularity.
- Correct the global Moran equation and negative null expectation; clarify weight dependence and permutation interpretation.
- State an explicit Local Moran scaling convention and its conditional local-to-global identity, rather than tying the scaling factor to row standardisation.
- Correct the silhouette within-cluster average and clarify the singleton convention.
- Replace the NNA slide outline with a connected explanation, numerical example, geographical limitations, notebook links and self-check feedback.
- Add `lab-05-nna-self-study.ipynb`: a synthetic-data practical with optional projected-coordinate CSV input, fixed-window simulations, explicit test alternatives and analytical comparison.
- Preserve the full HDB point-pattern lab, add a route to the companion, and correct its K/L simulation to compare simulated points with themselves. Clear its old outputs because they predate that correction.
- Link the NNA section, notebook, Gordon Square worked example and lecture collection.
- Add Part 4 and the Week 5 HTML deck, its local runtime, fonts and referenced illustrations. Apply targeted inference-wording corrections to the public slide copy; update both its embedded source and search index.
- Include the book's existing custom fonts in static output, prevent the long mobile header and decorative maths from widening the page, pin the book builder to 2.1.7, and add a pull-request workflow that checks calculations and builds without deploying.

## Source record

Book baseline: `3ad62eb52de98e8f9e4b14ab4a4c625b9410dfaa`.

Course source snapshot: `2365ed5a6299a17e8e6dac52be0a896c1f0b46f9`. Week 5 provides the NNA standard-error addition, teaching context and slide snapshot. The public copy includes wording corrections; it is not an automatic mirror of the course repository. Existing book illustrations are reused unchanged.

Slide files live in `slides/2610/`. `myst.yml` copies the complete `slides` folder as static content. The lecture index uses the canonical Pages URL because the current builder hashes ordinary file links, which would detach the deck from its relative assets. Preserve the internal resource and runtime paths when adding more decks.

## Local validation

The book's HTML export was checked with Jupyter Book 2.1.7, its bundled MyST 1.11.0, Node 24.19.0 and `BASE_URL=/geo-stat-vis`. CI uses Node 22. The restricted local environment required a process-local workaround for network-interface enumeration; that workaround is not part of the repository or deployment.

All seven code cells in the self-study notebook execute sequentially, with saved text and figure outputs. Numerical checks compare the KD-tree distances with an independent all-pairs calculation, cover coincident points and invalid input, check simulation tails including ties, compare synthetic pattern modes, and verify the area-sensitivity calculation. Run `python scripts/check_nna_pilot.py` with NumPy, SciPy and Matplotlib installed.

A socket-based Jupyter kernel could not start in the restricted local environment. Outputs were therefore produced by sequential execution in one Python process, and the notebook format was validated. The full external-data HDB lab was not executed; it remains an application requiring its data and wider dependency setup.

Browser checks cover the chapter at desktop and 390-pixel mobile widths, the slide-index link, 61-slide navigation, mathematical rendering, image loads and fonts. The mobile layout has no page-level horizontal overflow. No page JavaScript errors or missing asset requests were observed in these checks.

All local slide and nested CSS dependencies were checked. The 61-slide search index and the agreement between slide Markdown and embedded source were verified. Existing book warnings about duplicated identifiers and heading depth remain outside this pilot.

## Dataset distribution

The notebook update also includes public data access without Google Drive mounting. See [dataset inventory and large-file distribution plan](2610-data-inventory.md). Small files can remain in Git; larger per-notebook packages should use versioned Release downloads. The inventory distinguishes existing public data from inputs still requiring transfer. No missing data or release assets have been uploaded by this planning change.

## Next batches

1. Review this pilot's level of explanation, mathematical detail and balance of figures with prose.
2. Complete the remaining Chapter 6 implementation/version checks, especially Local Geary labels and Getis–Ord output interpretation; migrate the current Week 8 notebook.
3. Bring across the Week 3 effect-size additions and Week 4 stationarity/CSR explanations, coordinating shared concepts across chapters.
4. Add the other weekly decks after reviewing their content and dependencies. Regenerate and check PDFs before offering downloads; the Week 5 pilot intentionally has no PDF link.
5. Expand the remaining book sections and update the associated practical materials chapter by chapter.

Do not include generated `_build/` files in this change. The existing deployment workflow still publishes only after a push to `main`; the pull-request check does not deploy.
