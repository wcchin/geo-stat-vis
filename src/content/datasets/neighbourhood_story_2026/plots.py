"""Reproduce original Chapter 7 figures from bundled prepared data; no network."""
from pathlib import Path
import json
import numpy as np,pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import Normalize,LogNorm,LinearSegmentedColormap
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch,Circle
from pyproj import Transformer
P=Path(__file__).resolve().parent
import lzma
def snapshot(path):
 path=Path(path)
 if not path.exists() and Path(str(path)+'.xz').exists():
  path.write_bytes(lzma.decompress(Path(str(path)+'.xz').read_bytes()))
 return path

font_manager.fontManager.addfont(str(P.parents[3]/'_static/css/fonts/ComicNeue-Regular.ttf'));plt.rcParams.update({'font.family':['Comic Neue','DejaVu Sans'],'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
T=Transformer.from_crs(4326,3414,always_xy=True);context=json.load(open(snapshot(P/'planning_areas.geojson')))
for name in ['block_metrics.csv','selected_blocks.csv','pois.csv','stops.csv']: snapshot(P/'data'/name)
b=pd.read_csv(P/'data/block_metrics.csv');s=pd.read_csv(P/'data/selected_blocks.csv');p=pd.read_csv(P/'data/pois.csv');bus=pd.read_csv(P/'data/stops.csv').dropna(subset=['x','y'])
colors={'Hawker centre':'#a34c17','School':'#67518c','Park reference point':'#267f80'};markers={'Hawker centre':'s','School':'^','Park reference point':'D'}
cmap=LinearSegmentedColormap.from_list('OrRd_cut',plt.get_cmap('OrRd')(np.linspace(.23,1,256)))
def bg(ax,local=None):
 for f in context['features']:
  g=f['geometry'];polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
  for poly in polys:
   verts=[];codes=[]
   for ring in poly:
    a=np.array(ring);x,y=T.transform(a[:,0],a[:,1]);v=np.column_stack([x,y])/1000;verts.extend(v);codes.extend([MPath.MOVETO]+[MPath.LINETO]*(len(v)-2)+[MPath.CLOSEPOLY])
   ax.add_patch(PathPatch(MPath(verts,codes),fc='#f2efe8',ec='#b9b3a8',lw=.4,zorder=0))
 if local is None:
  ax.set(xlim=(0,58),ylim=(14,54));ax.plot([3,8],[18,18],c='#555',lw=2);ax.text(5.5,16.5,'5 km',ha='center',fontsize=9)
 else:
  x,y=local;ax.set(xlim=(x-1.15,x+1.15),ylim=(y-1.15,y+1.15));ax.plot([x-.95,x-.45],[y-1,y-1],c='#555',lw=2);ax.text(x-.7,y-1.1,'500 m',ha='center',fontsize=9)
 ax.set_aspect('equal');ax.set_axis_off();ax.text(.98,.97,'N ↑',transform=ax.transAxes,ha='right',fontsize=9)
def save(fig,name,foot):
 fig.text(.025,.015,foot,fontsize=9,color='#5e554b');fig.savefig(P/'figures'/name,dpi=165,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(1,3,figsize=(16,5.7));fig.subplots_adjust(bottom=.2,top=.83,wspace=.14)
for ax in axs:bg(ax)
sc=axs[0].scatter(b.x/1000,b.y/1000,c=b.median_price/1000,cmap=cmap,s=8,lw=0,norm=Normalize(300,1400));axs[0].set_title('Price: 3,236 selling blocks\nMedian four-room resale price');fig.colorbar(sc,ax=axs[0],orientation='horizontal',fraction=.045,pad=.03,label='S$ thousands (values beyond endpoints clipped)',extend='both')
v=bus[bus.weekday_daily>0];sc=axs[1].scatter(v.x/1000,v.y/1000,c=v.weekday_daily,cmap=cmap,norm=LogNorm(1,v.weekday_daily.max()),s=6,lw=0);axs[1].set_title('Activity: geocoded bus stops\nAverage weekday boardings');fig.colorbar(sc,ax=axs[1],orientation='horizontal',fraction=.045,pad=.03,label='Boardings/day (log colour scale)')
for cat,col in colors.items():
 v=p[p.category==cat];axs[2].scatter(v.x/1000,v.y/1000,c=col,marker=markers[cat],s=9,lw=0,label=cat)
axs[2].set_title('Selected amenities: 922 records\nDifferent categories, different meanings');axs[2].legend(loc='lower left',bbox_to_anchor=(0,-.25),fontsize=9,frameon=False)
fig.suptitle('One city, three kinds of evidence',fontsize=20)
save(fig,'01_evidence.png','HDB Jan–Jun 2026; LTA Sep 2026; MOE/NParks source mirror and NEA directory. URA MP2019 planning areas; EPSG:3414. Layers are not time-matched.')
fig,axs=plt.subplots(1,3,figsize=(15,6));fig.subplots_adjust(top=.8,bottom=.22,wspace=.13)
for ax,(_,r) in zip(axs,s.iterrows()):
 x,y=r.x/1000,r.y/1000;bg(ax,(x,y));v=bus[np.hypot(bus.x-r.x,bus.y-r.y)<=1700];ax.scatter(v.x/1000,v.y/1000,s=12,c='#a9a29a',label='Bus stop',zorder=2)
 for rad,ls in [(800,'--'),(500,'-')]:ax.add_patch(Circle((x,y),rad/1000,fill=False,lw=1.5,ls=ls,ec='#8b571f',zorder=3))
 for cat,col in colors.items():
  v=p[(p.category==cat)&(np.hypot(p.x-r.x,p.y-r.y)<=1700)];ax.scatter(v.x/1000,v.y/1000,c=col,marker=markers[cat],s=42,edgecolors='white',lw=.45,label=cat,zorder=4)
 ax.scatter([x],[y],c='#221b13',s=110,marker='*',label='Selected block',zorder=5);ax.set_title(r.town.title()+'\n'+r.address,fontsize=13)
handles,labels=axs[0].get_legend_handles_labels();fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.5,.065),ncol=5,frameon=False,fontsize=10)
fig.suptitle('What is nearby? Hold map extent and symbols constant',fontsize=20)
save(fig,'02_neighbourhoods.png','Solid circle: 500 m; dashed: 800 m straight-line radius. Stars are block reference points. Park diamonds are reference points, not entrances. No street network is shown.')
fig,axs=plt.subplots(1,5,figsize=(16,5.4));fig.subplots_adjust(left=.11,right=.99,top=.76,bottom=.19,wspace=.6)
metrics=[('median_price','Block median price\nS$ thousands',1000),('stops_500','Bus-stop records\nwithin 500 m',1),('boardings_500','Weekday boardings\nnearby stops / day',1),('schools_500','School records\nwithin 500 m',1),('parks_500','Park reference points\nwithin 500 m',1)]
for ax,(key,title,div) in zip(axs,metrics):
 ax.barh(range(3),s[key]/div,color=['#a7652a','#c88742','#e0b069'],height=.55);ax.invert_yaxis();ax.set_title(title,fontsize=11);ax.set_yticks(range(3),s.town.str.title() if ax==axs[0] else ['']*3);ax.spines[['top','right']].set_visible(False);ax.set_xlim(0,max(s[key]/div)*1.45 if s[key].max() else 1)
 for i,val in enumerate(s[key]/div):ax.text(val,i,' '+f'{val:,.0f}',va='center',fontsize=10)
fig.suptitle('Equal stop counts do not imply equal recorded activity',fontsize=20)
save(fig,'03_comparison.png','Three illustrative blocks, each with five four-room sales. Separate axes retain natural units. No hawker-centre records lie within 500 m of these blocks; absence from this category is not absence of food.')
fig,axs=plt.subplots(1,4,figsize=(15,5.5));fig.subplots_adjust(top=.75,bottom=.21,left=.1,wspace=.6)
for ax,key,title in zip(axs,['stops','hawkers','schools','parks'],['Bus-stop records','Hawker-centre records','School records','Park reference points']):
 y=np.arange(3);ax.barh(y-.15,s[f'{key}_500'],height=.28,color='#a7652a',label='500 m');ax.barh(y+.15,s[f'{key}_800'],height=.28,color='#e5b979',label='800 m');ax.invert_yaxis();ax.set_yticks(y,s.town.str.title() if ax==axs[0] else ['']*3);ax.set_title(title,fontsize=12);ax.set_xlabel('Records within radius');ax.spines[['top','right']].set_visible(False)
axs[-1].legend(frameon=False);fig.suptitle('A nearby-amenity story depends on the boundary',fontsize=20)
save(fig,'04_radius.png','Both radii use the same input records and selected blocks. Counts can rise mechanically with radius; this is a sensitivity check, not an estimate of walking accessibility.')
# Deliberate hierarchy comparison with identical local records, extent and selection.
r=s.iloc[1];x,y=r.x/1000,r.y/1000;fig,axs=plt.subplots(1,2,figsize=(12,6));fig.subplots_adjust(top=.8,bottom=.19,wspace=.12)
for i,ax in enumerate(axs):
 bg(ax,(x,y));v=bus[np.hypot(bus.x-r.x,bus.y-r.y)<=1700];ax.scatter(v.x/1000,v.y/1000,s=70 if i==0 else 12,c='#928a80',alpha=.9,zorder=2)
 for cat,col in colors.items():
  v=p[(p.category==cat)&(np.hypot(p.x-r.x,p.y-r.y)<=1700)];ax.scatter(v.x/1000,v.y/1000,c=col,marker=markers[cat],s=130 if i==0 else 45,edgecolors='white',lw=.5,zorder=3)
 ax.add_patch(Circle((x,y),.5,fill=False,ec='#6c3b10',lw=3 if i==0 else 1.5,zorder=4));ax.scatter([x],[y],c='#211a12',s=180 if i==0 else 100,marker='*',zorder=5)
 if i==0:ax.text(.5,.45,'TAMPINES',transform=ax.transAxes,ha='center',fontsize=32,weight='bold',color='#31261a');ax.set_title('Everything asks for attention',fontsize=16)
 else:ax.set_title('Start with the block and its 500 m radius',fontsize=16);ax.annotate('Selected block',(x,y),(x-.9,y+.8),arrowprops={'arrowstyle':'-','color':'#6c3b10'},fontsize=11,color='#513315')
fig.suptitle('Visual hierarchy changes emphasis; the underlying records stay fixed',fontsize=18)
save(fig,'05_hierarchy.png','Tampines example. Same extent, record filters, locations and categories in both panels; symbol size and typography change. Read category symbols using Figure 2’s key.')
print('Wrote 5 original figure plates')
