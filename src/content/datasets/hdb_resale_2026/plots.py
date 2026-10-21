"""Reproduce pilot figures from the bundled prepared data. No network required."""
from pathlib import Path
import json,lzma
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize, LinearSegmentedColormap
from matplotlib import font_manager
P=Path(__file__).resolve().parent
font=P.parents[3]/'_static/css/fonts/ComicNeue-Regular.ttf'
if font.exists():
 font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']=['Comic Neue','DejaVu Sans']
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'figure.facecolor':'white','savefig.facecolor':'white'})
from pyproj import Transformer
ORRD=LinearSegmentedColormap.from_list('pilot_OrRd',plt.get_cmap('OrRd')(np.linspace(.23,1,256)))
T=Transformer.from_crs(4326,3414,always_xy=True)
CONTEXT=json.loads(lzma.decompress((P/'planning_areas.geojson.xz').read_bytes()))
def background(ax):
 from matplotlib.path import Path as MPath
 from matplotlib.patches import PathPatch
 for f in CONTEXT['features']:
  g=f['geometry'];polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
  for poly in polys:
   verts=[];codes=[]
   for ring in poly:
    a=np.array(ring);x,y=T.transform(a[:,0],a[:,1]);v=np.column_stack([x,y])/1000
    verts.extend(v);codes.extend([MPath.MOVETO]+[MPath.LINETO]*(len(v)-2)+[MPath.CLOSEPOLY])
   ax.add_patch(PathPatch(MPath(verts,codes),fc='#f2efe8',ec='#bbb6aa',lw=.45,zorder=0))
 ax.set(xlim=(0,58),ylim=(14,54),aspect='equal');ax.set_axis_off()
 ax.text(.97,.95,'N ↑',transform=ax.transAxes,ha='right')
 ax.plot([3,8],[18,18],c='#555',lw=2);ax.text(5.5,16.7,'5 km',ha='center',fontsize=9)

def save(fig,path,foot):
 fig.get_layout_engine().set(rect=(0,.08,1,.92))
 fig.text(.02,.015,foot,fontsize=9,color='#555555');fig.savefig(P/path,dpi=180);plt.close(fig)
def hdb_maps():
 h=pd.read_csv(P/'hdb/transactions.csv.xz');b=pd.read_csv(P/'hdb/blocks.csv.xz');a=json.loads((P/'hdb/audit.json').read_text())
 fig,axs=plt.subplots(1,3,figsize=(16,5.5),layout='constrained');norm=LogNorm(1,b.transactions.max())
 for ax,col,title in zip(axs,['transactions','lower','upper'],['All transactions',f'Lower quartile: ≤ S${a["q1"]:,.0f}',f'Upper quartile: ≥ S${a["q3"]:,.0f}']):
  background(ax);v=b[b[col]>0];sc=ax.scatter(v.x/1000,v.y/1000,c=v[col],cmap=ORRD,norm=norm,s=15,lw=0);ax.set_title(f'{title}\n{int(v[col].sum()):,} transactions at {len(v):,} blocks')
 fig.colorbar(sc,ax=axs,label='Transactions per block (shared log colour scale)',shrink=.65,pad=.01);fig.suptitle('Four-room HDB resale registrations · January–June 2026',fontsize=17)
 save(fig,'hdb/maps.png','HDB resale data; HDB/OneMap block locations via open-data snapshot; URA MP2019 planning areas. Co-located sales counted per block; no jitter.')
 fig,axs=plt.subplots(1,3,figsize=(15,4.8),layout='constrained')
 axs[0].hist(h.resale_price/1000,bins=35,color='#d88432',ec='white');axs[0].axvline(a['q1']/1000,c='#7e360c',ls='--');axs[0].axvline(a['q3']/1000,c='#7e360c',ls='--');axs[0].set(xlabel='Resale price (S$ thousands)',ylabel='Transactions',title='Price distribution and quartile cutoffs')
 axs[1].scatter(h.floor_area_sqm,h.resale_price/1000,s=6,alpha=.25,c='#b95e15');axs[1].set(xlabel='Floor area (m²)',ylabel='Resale price (S$ thousands)',title='Four-room flats still vary in size')
 ct=pd.crosstab(h.price_group,h.psm_group).reindex(index=['lower','middle','upper'],columns=['lower','middle','upper'],fill_value=0)
 axs[2].imshow(ct,cmap=ORRD);axs[2].set(xticks=range(3),xticklabels=ct.columns,yticks=range(3),yticklabels=ct.index,xlabel='Quartile group using price per m²',ylabel='Quartile group using total price',title='Sensitivity to the price measure')
 for i in range(3):
  for j in range(3):axs[2].text(j,i,str(ct.iloc[i,j]),ha='center',va='center',color='white' if ct.iloc[i,j]>ct.to_numpy().max()*.55 else '#42240d')
 save(fig,'hdb/distributions.png','All 5,379 transactions retained. Cutoffs use pandas linear quantiles, including all ties. Groups are descriptive; they do not establish significant clustering.')
 # Fraction views help distinguish price composition from transaction density.
 fig,axs=plt.subplots(1,2,figsize=(12,5.8),layout='constrained')
 for ax,col in zip(axs,['lower','upper']):
  background(ax);sc=ax.scatter(b.x/1000,b.y/1000,c=b[col]/b.transactions,cmap=ORRD,vmin=0,vmax=1,s=10+5*np.sqrt(b.transactions),lw=0);ax.set_title(f'{col.capitalize()}-quartile share of block sales')
 fig.colorbar(sc,ax=axs,label='Share (0–1)',shrink=.6);fig.suptitle('Price composition at selling blocks · exploratory sensitivity view',fontsize=16)
 save(fig,'hdb/shares.png','Shares at blocks with few sales are unstable. Marker area increases with √(sales); these are observations, not smoothed rates or significance tests.')
if __name__=='__main__':hdb_maps()
