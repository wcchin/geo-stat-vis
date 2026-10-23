"""Run the portable clustering-across-time notebook."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
p=Path(__file__).resolve().parents[1]/"src/content/notebooks/spatial-clustering-across-time.ipynb"
nb=json.loads(p.read_text());ns={}
for cell in nb["cells"]:
    if cell["cell_type"]=="code":exec("".join(cell["source"]),ns)
assert len(ns["summary"])==2
assert {x[0] for x in ns["summary"]}=={"morning","afternoon"}
assert sum(x[1] for x in ns["summary"])==len(ns["data"])
print("PASS synthetic clustering across time")
