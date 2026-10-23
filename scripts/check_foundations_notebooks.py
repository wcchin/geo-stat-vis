"""Execute all solution notebook code cells against staged HDB data."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
base = Path(__file__).resolve().parents[1] / "src/content/notebooks"
for stem in ("exploring-distributions", "data-transformation-classification", "statistical-group-comparisons"):
    learner = json.loads((base / (stem + ".ipynb")).read_text())
    solution = json.loads((base / (stem + "-solution.ipynb")).read_text())
    code = lambda nb: ["".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"]
    assert any("# TODO:" in c for c in code(learner))
    assert not any("# TODO:" in c for c in code(solution))
    ns = {"__name__": "__main__"}
    for i, cell in enumerate(code(solution), 1):
        try: exec(compile(cell, stem + ":" + str(i), "exec"), ns)
        except Exception as e: raise RuntimeError(stem + " cell " + str(i)) from e
    print("PASS", stem)
