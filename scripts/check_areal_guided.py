"""Execute synthetic areal-analysis solution notebooks."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
root=Path(__file__).resolve().parents[1]/"src/content/notebooks"
for name in ("global-spatial-autocorrelation","local-spatial-autocorrelation"):
    learner=json.loads((root/(name+".ipynb")).read_text())
    solution=json.loads((root/(name+"-solution.ipynb")).read_text())
    cells=lambda n:["".join(c["source"]) for c in n["cells"] if c["cell_type"]=="code"]
    assert sum("# TODO:" in c for c in cells(learner))==2
    ns={}
    for code in cells(solution):exec(code,ns)
    assert np.isfinite(ns["observed"])
    if name.startswith("global"):
        assert len(ns["permutations"])==999 and 0<ns["p_upper"]<=1
    else:
        assert len(ns["local_i"])==len(ns["values"])
    print("PASS",name)
