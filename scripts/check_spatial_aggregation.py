"""Execute the spatial aggregation solution and check key invariants."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
p=Path(__file__).resolve().parents[1]/"src/content/notebooks/spatial-aggregation-solution.ipynb"
nb=json.loads(p.read_text())
ns={}
for i,cell in enumerate(nb["cells"]):
    if cell["cell_type"]=="code":
        exec(compile("".join(cell["source"]),str(p)+":"+str(i),"exec"),ns)
assert ns["area_summary"]["transactions"].sum()<=len(ns["hdb"])
assert ns["area_summary"]["median_price"].notna().all()
assert ns["area_summary"]["transactions"].gt(0).all()
print("PASS spatial aggregation solution")
