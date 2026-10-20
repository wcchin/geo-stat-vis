"""Reproduce the two-window FIRMS count analysis. Run from repository root.
Dependencies: numpy pandas matplotlib. Figures use sequential OrRd, without sketch distortion.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path('.')
DATA=ROOT/'src/content/datasets/firms_sumatra'
if DATA.exists():
    points=pd.read_csv(DATA/'detections.csv.gz')
    metadata=json.loads((DATA/'assessment.json').read_text())
else:
    import urllib.request
    base='https://raw.githubusercontent.com/wcchin/geo-stat-vis/main/src/content/datasets/firms_sumatra/'
    points=pd.read_csv(base+'detections.csv.gz',compression='gzip')
    metadata=json.loads(urllib.request.urlopen(base+'assessment.json').read())
B=9999
rng=np.random.default_rng(5230)
counts=[];areas=[];results=[]
for spec in metadata['windows']:
    label=spec['window'][0];q=points[points.window==label]
    x,y,right,top=spec['bounds_m']
    assert ((q.easting_m>=x)&(q.easting_m<right)&(q.northing_m>=y)&(q.northing_m<top)).all()
    c=np.histogram2d((q.easting_m-x)/1000,(q.northing_m-y)/1000,bins=(np.arange(0,101,20),np.arange(0,101,20)))[0].T
    assert c.astype(int).tolist()==spec['counts_south_to_north']
    counts.append(c);areas.append(np.array(spec['land_cell_area_km2']))
assert len(points)==6201 and not points.duplicated().any()
for label,c,a in [('A',counts[0],areas[0]),('B',counts[1],areas[1]),('A+B',np.hstack(counts),np.hstack(areas))]:
    n=int(c.sum());prob=a.ravel()/a.sum();expected=n*prob
    observed=float(np.sum((c.ravel()-expected)**2/expected))
    simulations=rng.multinomial(n,prob,size=B)
    reference=np.sum((simulations-expected)**2/expected,axis=1)
    result=dict(window=label,n=n,m=c.size,land_km2=float(a.sum()),expected_min=float(expected.min()),expected_max=float(expected.max()),T=observed,df=c.size-1,p_upper=float((1+(reference>=observed).sum())/(B+1)),simulations=B,seed=5230)
    results.append(result);print(result)
fig,ax=plt.subplots(figsize=(12,6),layout='constrained')
image=ax.pcolormesh(np.arange(0,201,20),np.arange(0,101,20),np.hstack(counts),cmap='OrRd',vmin=0,vmax=1207,edgecolors='#777777',linewidth=.5)
for j in range(5):
    for i in range(10):
        value=int(np.hstack(counts)[j,i]);ax.text(i*20+10,j*20+10,str(value),ha='center',va='center',color='white' if value>650 else '#222222')
ax.axvline(100,color='#222222',lw=2)
ax.set(aspect='equal',xlabel='km east of western origin',ylabel='km north of shared origin',title='Combined South Sumatra window: A (west) + B (east)\n6,201 detections · September 2026 · 20 km quadrats')
fig.colorbar(image,ax=ax,label='Satellite detections per quadrat',shrink=.8)
if DATA.exists():
    (DATA/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    fig.savefig(ROOT/'src/content/resources/original/firms-combined-window.svg')
plt.show()
