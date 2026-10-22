"""Offline analysis. Python: pandas, numpy, scipy, pyproj, shapely."""
from pathlib import Path
import json,hashlib
import pandas as pd,numpy as np
from scipy.spatial import cKDTree
from pyproj import Transformer
from shapely import wkt
P=Path(__file__).resolve().parent
import lzma
def snapshot(path):
 path=Path(path)
 if not path.exists() and Path(str(path)+'.xz').exists():
  path.write_bytes(lzma.decompress(Path(str(path)+'.xz').read_bytes()))
 return path

D=P/'data';T=Transformer.from_crs(4326,3414,always_xy=True)
for name in ['transactions.csv','blocks.csv','stops.csv','hawkers_raw.json','sg_schools.csv','sg_parks.csv']: snapshot(D/name)
h=pd.read_csv(D/'transactions.csv');b=pd.read_csv(D/'blocks.csv');bus=pd.read_csv(D/'stops.csv',dtype={'PT_CODE':str})
# Only fields needed for the lesson are retained in the prepared POI table.
rows=[]
def add(category,name,lon,lat):
 try:
  lon,lat=float(lon),float(lat)
  if not(103.5<lon<104.2 and 1.1<lat<1.6):return
  x,y=T.transform(lon,lat);rows.append(dict(category=category,name=name,longitude=lon,latitude=lat,x=x,y=y))
 except (ValueError,TypeError):return
raw=json.load(open(D/'hawkers_raw.json'))['result'];assert len(raw['records'])==raw['total']
for r in raw['records']:add('Hawker centre',r['name'],r['longitude_hc'],r['latitude_hc'])
for file,cat,name in [('sg_schools.csv','School','school_name'),('sg_parks.csv','Park reference point','name')]:
 for _,r in pd.read_csv(D/file).iterrows():
  if isinstance(r.geom_4326,str):
   pt=wkt.loads(r.geom_4326);add(cat,r[name],pt.x,pt.y)
p=pd.DataFrame(rows);assert not p.duplicated(['category','name','x','y']).any();p.to_csv(D/'pois.csv',index=False)
valid=bus.dropna(subset=['x','y']).copy();tree=cKDTree(valid[['x','y']]);xy=b[['x','y']].to_numpy()
b['nearest_stop_m']=tree.query(xy)[0]
for radius in [500,800]:
 ns=tree.query_ball_point(xy,radius)
 b[f'stops_{radius}']=[len(i) for i in ns]
 b[f'known_stops_{radius}']=[int(valid.iloc[i].weekday_daily.notna().sum()) for i in ns]
 b[f'boardings_{radius}']=[float(valid.iloc[i].weekday_daily.sum(min_count=1)) if len(i) else np.nan for i in ns]
 for cat,key in [('Hawker centre','hawkers'),('School','schools'),('Park reference point','parks')]:
  v=p[p.category==cat];ids=cKDTree(v[['x','y']]).query_ball_point(xy,radius);b[f'{key}_{radius}']=[len(i) for i in ids]
town=h.groupby('address').town.first();b['town']=b.address.map(town)
selected=[]
for town in ['BISHAN','TAMPINES','WOODLANDS']:
 target=float(h[h.town==town].resale_price.median());v=b[(b.town==town)&(b.transactions>=3)].copy();assert len(v)
 v['selection_difference']=(v.median_price-target).abs();r=v.sort_values(['selection_difference','address']).iloc[0].to_dict();r['town_transaction_median']=target;selected.append(r)
s=pd.DataFrame(selected);s.to_csv(D/'selected_blocks.csv',index=False);b.to_csv(D/'block_metrics.csv',index=False)
a={'transactions':len(h),'selling_blocks':len(b),'poi_counts':p.category.value_counts().to_dict(),'school_missing_coordinates':int(pd.read_csv(D/'sg_schools.csv').geom_4326.isna().sum()),'mapped_bus_records':len(valid),'bus_records_without_coordinates':len(bus)-len(valid),'selection_rule':'Towns fixed in advance: Bishan, Tampines, Woodlands. Among blocks with >=3 transactions, minimise absolute difference between block median and town transaction median; break ties alphabetically by address.','selected':selected,'crs':'EPSG:3414 metres','radii_m':[500,800]}
(D/'audit.json').write_text(json.dumps(a,indent=2,allow_nan=False))
print(s[['town','address','transactions','median_price','nearest_stop_m','stops_500','boardings_500','hawkers_500','schools_500','parks_500']].to_string(index=False));print(a['poi_counts'])
