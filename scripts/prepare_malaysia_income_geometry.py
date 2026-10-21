"""Optional full-detail geometry audit and representative-point preparation.
Requires shapely and scipy. Main analysis uses the small saved outputs offline.
"""
from pathlib import Path
import json,hashlib
import numpy as np,pandas as pd
from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely import make_valid
from scipy.spatial.distance import cdist
from scipy.sparse.csgraph import connected_components
R=Path(__file__).resolve().parents[1];D=R/'src/content/datasets/malaysia_income_areal';D.mkdir(exist_ok=True)
import urllib.request,urllib.parse
CACHE=R/'build/malaysia_income_geometry';CACHE.mkdir(parents=True,exist_ok=True)
params={'where':"kod_negeri NOT IN ('12','13','15')",'outFields':'negeri,kod_negeri,daerah,kod_daerah','returnGeometry':'true','outSR':'3375','f':'json'}
query='https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0/query?'+urllib.parse.urlencode(params)
raw=CACHE/'full.json'
if not raw.exists():
    with urllib.request.urlopen(query,timeout=180) as response:raw.write_bytes(response.read())
payload=raw.read_bytes()
expected='d5aafcfa17d2d28a10d7a9a7b98b1b9d16dc63111b195047a3a85cb7be8f4ad9'
assert hashlib.sha256(payload).hexdigest()==expected,'Boundary source changed: review as a new snapshot rather than overwriting silently.'
layer=json.loads(payload);assert len(layer['features'])==92 and not layer.get('exceededTransferLimit')
geometries=[];invalid=[];overlap=[]
for f in layer['features']:
 shells=[];holes=[]
 for ring in f['geometry']['rings']:
  a=np.array(ring);signed=np.sum(a[:-1,0]*a[1:,1]-a[1:,0]*a[:-1,1])/2
  (shells if signed<0 else holes).append(Polygon(ring))
 if not shells:raise ValueError('No clockwise shell')
 g=unary_union([make_valid(p) for p in shells]);g=g.difference(unary_union([make_valid(p) for p in holes])) if holes else g
 if not g.is_valid:invalid.append(f['attributes']['kod_daerah']);g=make_valid(g)
 geometries.append(g)
table=pd.DataFrame([f['attributes'] for f in layer['features']]);table['kod_daerah']=table.kod_daerah.astype(str)
income=pd.read_csv(R/'src/content/datasets/peninsula_income_2022/hh_income_district.csv');income=income[(income.date.str.startswith('2022'))&(~income.state.isin(['Sabah','Sarawak','W.P. Labuan']))].copy()
alias={'Ulu Langat':'HULU LANGAT','Ulu Selangor':'HULU SELANGOR','W.P. Kuala Lumpur':'KUALA LUMPUR','W.P. Putrajaya':'PUTRAJAYA','Perlis':'KANGAR','Kecil Lojing':'LOJING','Larut dan Matang':'LARUT & MATANG','Timur Laut':'TIMOR LAUT'}
income['join_state']=income.state.str.upper();income['join_district']=income.district.map(lambda s:alias.get(s,s.upper()));table['join_state']=table.negeri.str.upper();table['join_district']=table.daerah.str.upper()
table=table.merge(income,on=['join_state','join_district'],how='left',validate='one_to_one',sort=False);assert len(table)==92 and table.income_median.notna().all() and table.kod_daerah.is_unique
points=[g.representative_point() for g in geometries];xy=np.array([[p.x,p.y] for p in points]);table['x_m']=xy[:,0];table['y_m']=xy[:,1];table['cell']=table.kod_daerah;table['value']=table.income_median
rook=np.zeros((92,92),int);queen=rook.copy()
for i,g in enumerate(geometries):
 for j in range(i):
  h=geometries[j]
  if not g.envelope.intersects(h.envelope):continue
  if g.intersects(h):
   queen[i,j]=queen[j,i]=1
   length=g.boundary.intersection(h.boundary).length
   if length>1e-6:rook[i,j]=rook[j,i]=1
   area=g.intersection(h).area
   if area>1:overlap.append({'i':table.cell.iloc[i],'j':table.cell.iloc[j],'area_m2':area})
dist=cdist(xy,xy);np.fill_diagonal(dist,np.inf)
records=[];diagnostics={}
for name,A in [('rook',rook),('queen',queen)]:
 diagnostics[name]={'isolates':table.loc[A.sum(1)==0,'daerah'].tolist(),'components':int(connected_components(A,directed=False)[0]),'undirected_edges':int(A.sum()/2)}
for k in [4,6]:
 neighbours=np.argsort(dist,axis=1,kind='stable')[:,:k];directed=np.zeros((92,92),int);directed[np.arange(92)[:,None],neighbours]=1;A=np.maximum(directed,directed.T)
 diagnostics[f'union_knn_{k}']={'components':int(connected_components(A,directed=False)[0]),'isolates':int((A.sum(1)==0).sum()),'undirected_edges':int(A.sum()/2),'min_degree':int(A.sum(1).min()),'max_degree':int(A.sum(1).max()),'maximum_link_km':float(dist[A>0].max()/1000),'median_link_km':float(np.median(dist[A>0])/1000)}
 for i,j in zip(*np.where(np.triu(A,1))):records.append({'graph':f'union_knn_{k}','i':table.cell.iloc[i],'j':table.cell.iloc[j],'distance_m':dist[i,j]})
table[['cell','state','district','value','income_mean','x_m','y_m']].to_csv(D/'observations.csv',index=False,float_format='%.8f');pd.DataFrame(records).to_csv(D/'edges.csv',index=False,float_format='%.8f')
meta={'retrieved':'2026-10-21','boundary_query':query,'full_boundary_sha256':hashlib.sha256(payload).hexdigest(),'full_boundary_bytes':len(payload),'geometry_count':92,'invalid_after_conversion':invalid,'overlaps_over_1m2':overlap,'geometry_method':'Esri clockwise shells unioned; counterclockwise holes subtracted; make_valid applied to source rings before union. Interior representative_point per full geometry.','crs':'EPSG:3375','income_year':2022,'variable':'median gross monthly household income (RM)','income_sha256':hashlib.sha256((R/'src/content/datasets/peninsula_income_2022/hh_income_district.csv').read_bytes()).hexdigest(),'diagnostics':diagnostics,'primary':'union_knn_4','sensitivity':'union_knn_6','selection':'Rules chosen before computing association: retain all 92 areas including islands; primary symmetric union of four nearest interior representative points, sensitivity six. These are proximity relations, not commuting links or boundary contiguity.'}
(D/'geometry_audit.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
