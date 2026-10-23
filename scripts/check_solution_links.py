"""Verify every guided learner/solution pair has reciprocal introductory and closing links."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]/"src/content/notebooks"
pairs=sorted(p for p in root.glob("*-solution.ipynb") if (root/(p.name.replace("-solution.ipynb",".ipynb"))).exists())
assert pairs,"No learner/solution pairs found"
for solution in pairs:
    learner=root/solution.name.replace("-solution.ipynb",".ipynb")
    n=json.loads(learner.read_text()); s=json.loads(solution.read_text())
    def md(nb):
        return ["".join(c["source"]) if isinstance(c["source"],list) else c["source"] for c in nb["cells"] if c["cell_type"]=="markdown"]
    intro=md(n)[0]; closing=md(n)[-1]
    assert solution.name in intro and solution.name in closing, f"Missing solution navigation in {learner.name}"
    assert learner.name in md(s)[0] and learner.name in md(s)[-1], f"Missing return link in {solution.name}"
    assert "## Check your understanding" in closing
    print("PASS", learner.name)
print(f"{len(pairs)} learner/solution pairs verified")
