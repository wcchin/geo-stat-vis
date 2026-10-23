"""Execute the standalone origin-destination flow worked notebook."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
p=Path(__file__).resolve().parents[1]/"src/content/notebooks/visualising-origin-destination-flows.ipynb"
nb=json.loads(p.read_text());ns={}
for c in nb["cells"]:
    if c["cell_type"]=="code":exec("".join(c["source"]),ns)
assert int(ns["od"]["count"].sum())==119
assert ns["locations"]["id"].is_unique
assert ns["flow_export"].shape[0]==4
print("PASS portable OD worked example")
