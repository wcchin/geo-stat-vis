"""Validate new concept-based learner/solution notebooks using synthetic data."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

folder = Path(__file__).resolve().parents[1] / "src/content/notebooks"
stems = ["global-point-patterns", "spatial-kernel-density", "spatial-clustering-methods"]
for stem in stems:
    learning = json.loads((folder / (stem + ".ipynb")).read_text())
    answer = json.loads((folder / (stem + "-solution.ipynb")).read_text())
    cells = lambda book: ["".join(cell["source"]) for cell in book["cells"] if cell["cell_type"] == "code"]
    assert sum("# TODO:" in s for s in cells(learning)) >= 2
    assert not any("# TODO:" in s for s in cells(answer))
    namespace = {"__name__": "__main__"}
    for i, code in enumerate(cells(answer)):
        exec(compile(code, f"{stem}:cell{i}", "exec"), namespace)
    if stem == "global-point-patterns":
        assert namespace["counts"].sum() == len(namespace["observed"])
        assert np.isfinite(namespace["R"]) and namespace["R"] > 0
    if stem == "spatial-kernel-density":
        assert np.isfinite(namespace["surface"]).all()
        assert np.isfinite(namespace["wide_surface"]).all()
    if stem == "spatial-clustering-methods":
        assert len(namespace["km"].labels_) == len(namespace["points"])
        assert len(namespace["labels"]) == len(namespace["points"])
    plt.close("all")
    print("PASS", stem)
