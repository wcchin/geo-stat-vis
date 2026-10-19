import json, numpy as np
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'src/content/notebooks/lab-05-nna-self-study.ipynb'
n=json.loads(p.read_text());ns={}
import matplotlib
matplotlib.use('Agg')
for cell in n['cells']:
 if cell['cell_type']=='code':exec(''.join(cell['source']),ns)
f=ns['nearest_distances'];pts=np.array([[0,0],[3,0],[0,4]],float)
np.testing.assert_allclose(f(pts),[3,3,4])
# Independent all-pairs reference, including coincident observations.
rng=np.random.default_rng(21);a=rng.uniform(0,100,(25,2));a[1]=a[0]
d=np.sqrt(((a[:,None]-a[None,:])**2).sum(axis=2));np.fill_diagonal(d,np.inf)
np.testing.assert_allclose(f(a),d.min(axis=1))
assert f(np.array([[0,0],[0,0],[5,0]]))[0]==0
# Edge validation and finite simulation ties.
for bad in [np.array([[0,0]]),np.array([[0,0],[float('nan'),0]]),np.array([[0,0],[1001,0]])]:
 try:ns['validate_points'](bad,ns['WINDOW'])
 except ValueError:pass
 else:raise AssertionError('Invalid points accepted')
assert ns['monte_carlo_pvalue'](2,[1,2,3],'less')==0.75
assert ns['monte_carlo_pvalue'](2,[1,2,3],'greater')==0.75
assert ns['monte_carlo_pvalue'](2,[1,2,3],'two-sided')==1
# All default modes yield the intended ordering; each has an independent null stream.
means={}
for kind in ['clustered','csr','regular']:
 observed_seed,simulation_seed=np.random.SeedSequence(7).spawn(2)
 points=ns['make_pattern'](kind,100,ns['WINDOW'],np.random.default_rng(observed_seed))
 ns['validate_points'](points,ns['WINDOW']);means[kind]=f(points).mean()
assert means['clustered'] < means['csr'] < means['regular']
# Verify the illustrative numerical example and enlarged-window result.
assert np.isclose(0.5/np.sqrt(100/1e6),50)
assert np.isclose(ns['observed']/ns['new_expected'],ns['ratio']/np.sqrt(2))
print('PASS: all notebook cells executed; distances match independent brute-force calculation; validation, duplicate points, tails, modes and window sensitivity checked.')
print('Mean distances:',means)

