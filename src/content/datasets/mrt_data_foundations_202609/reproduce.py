"""Reproduce the small joins from the bundled extracts. Python + pandas; no network."""
from pathlib import Path
import pandas as pd,json,lzma
P=Path(__file__).resolve().parent;D=P/'data'
od=pd.read_csv(D/'od_selected.csv');lookup=pd.read_csv(D/'station_lookup.csv');ex=pd.read_csv(D/'selected_exits.csv')
assert lookup.station_code.is_unique
j=od.merge(lookup[['station_code','station_name']],left_on='ORIGIN_PT_CODE',right_on='station_code',how='left',validate='many_to_one').rename(columns={'station_name':'origin_name'}).drop(columns='station_code')
j=j.merge(lookup[['station_code','station_name']],left_on='DESTINATION_PT_CODE',right_on='station_code',how='left',validate='many_to_one').rename(columns={'station_name':'destination_name'}).drop(columns='station_code')
assert len(j)==12 and j.TOTAL_TRIPS.sum()==12904;assert not j[['origin_name','destination_name']].isna().any().any()
j.to_csv(D/'od_joined_reproduced.csv',index=False)
# Ray casting with explicit edge inclusion. Closed Polygon and MultiPolygon rings supported.
def ring_state(x,y,ring):
 inside=False
 for (ax,ay),(bx,by) in zip(ring,ring[1:]):
  cross=(x-ax)*(by-ay)-(y-ay)*(bx-ax)
  if abs(cross)<1e-13 and min(ax,bx)-1e-12<=x<=max(ax,bx)+1e-12 and min(ay,by)-1e-12<=y<=max(ay,by)+1e-12:return 0
  if (ay>y)!=(by>y) and x<(bx-ax)*(y-ay)/(by-ay)+ax:inside=not inside
 return 1 if inside else -1
def covers(g,x,y):
 for poly in (g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]):
  states=[ring_state(x,y,r) for r in poly]
  if 0 in states or (states[0]==1 and all(a==-1 for a in states[1:])):return True
 return False
geo=json.loads(lzma.decompress((D/'planning_areas.geojson.xz').read_bytes()))
for _,r in lookup.iterrows():
 matches=[f['properties']['PLN_AREA_N'] for f in geo['features'] if covers(f['geometry'],r.reference_lon,r.reference_lat)]
 assert matches==[r.planning_area],(r.station_name,matches)
 # Independent Matplotlib path check for points strictly inside these polygons.
 from matplotlib.path import Path as MPath
 matches2=[]
 for f in geo['features']:
  g=f['geometry'];polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
  if any(MPath(poly[0]).contains_point((r.reference_lon,r.reference_lat)) and not any(MPath(h).contains_point((r.reference_lon,r.reference_lat)) for h in poly[1:]) for poly in polys):matches2.append(f['properties']['PLN_AREA_N'])
 assert matches2==matches
print('PASS: two many-to-one joins; 12 rows and 12,904 trips preserved; all four reference-point spatial matches independently verified.')
