"""Validate Part 3 navigation and notebook pair hygiene without executing lessons."""
from pathlib import Path
import json
import re
root = Path(__file__).resolve().parents[1]
yaml = (root / "myst.yml").read_text()
toc = re.findall(r"^\s+- file: (src/content/notebooks/[^\s]+\.ipynb)\s*$", yaml, re.M)
assert toc, "No notebook paths in MyST TOC"
assert len(toc) == len(set(toc)), "Duplicate notebook TOC entries"
for name in toc:
    p = root / name
    assert p.exists(), f"Missing notebook: {name}"
    assert "-solution.ipynb" not in name, "Solution duplicated in sidebar: " + name
    nb = json.loads(p.read_text())
    assert nb.get("nbformat") == 4, f"Invalid notebook format: {name}"
    assert any(c["cell_type"] == "markdown" for c in nb["cells"])
for name in toc:
    if name.endswith("-solution.ipynb"): continue
    stem = name[:-6]
    solution = root / (stem + "-solution.ipynb")
    if solution.exists():
        notebook = json.loads((root/name).read_text())
        text = "\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"]=="markdown")
        assert "-solution.ipynb" in text, f"No solution link in learner: {name}"
print(f"PASS: {len(toc)} unique published learner/complete notebook entries; pairs linked")
