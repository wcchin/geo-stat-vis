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
def bus_maps():
 s=pd.read_csv(P/'bus/stops.csv.xz',dtype={'PT_CODE':str});p=s.dropna(subset=['weekday_daily','weekend_daily']);m=p.dropna(subset=['x','y']);h=pd.read_csv(P/'bus/hourly.csv.xz')
 fig,axs=plt.subplots(1,3,figsize=(16,5.5),layout='constrained');norm=LogNorm(1,max(m.weekday_daily.max(),m.weekend_daily.max()))
 for ax,col,title in zip(axs[:2],['weekday_daily','weekend_daily'],['Weekday: monthly boardings ÷ 22','Weekend: monthly boardings ÷ 8']):
  background(ax);v=m[m[col]>0];sc=ax.scatter(v.x/1000,v.y/1000,c=v[col],cmap=ORRD,norm=norm,s=8,lw=0);ax.set_title(title)
 fig.colorbar(sc,ax=axs[:2],label='Boardings per day (shared log scale)',shrink=.65,pad=.01)
 background(axs[2]);axs[2].scatter(m.x/1000,m.y/1000,c='#d2cfc9',s=5,lw=0)
 for mask,c,label in [(m.difference>0,'#a9510c','Higher weekday'),(m.difference<0,'#644c85','Higher weekend')]:
  v=m[mask];axs[2].scatter(v.x/1000,v.y/1000,c=c,s=5+np.minimum(np.abs(v.difference),3000)/100,lw=0,label=label)
 axs[2].set_title('Direction of the paired difference');axs[2].legend(loc='lower left',fontsize=9)
 fig.suptitle('Singapore bus-stop boardings · September 2026',fontsize=17)
 save(fig,'bus/maps.png',f'LTA files supplied by instructor; URA MP2019 planning areas. {len(m):,} mapped paired stops. Differences: weekday minus weekend daily averages; larger markers = larger absolute difference.')
 fig,axs=plt.subplots(1,3,figsize=(15,4.8),layout='constrained')
 for col,c,label in [('weekday_daily','#b45a0a','Weekday'),('weekend_daily','#74608d','Weekend')]:axs[0].hist(np.log1p(p[col]),bins=40,histtype='step',lw=2,color=c,label=label)
 axs[0].set(xlabel='log(1 + daily boardings)',ylabel='Paired stops',title='Skewed distributions across stops');axs[0].legend()
 axs[1].scatter(p.weekend_daily,p.weekday_daily,s=5,alpha=.3,c='#ac5c19');lims=[1,max(p.weekday_daily.max(),p.weekend_daily.max())*1.1];axs[1].plot(lims,lims,c='#777',ls='--');axs[1].set(xscale='symlog',yscale='symlog',xlabel='Weekend daily boardings',ylabel='Weekday daily boardings',title='Same stops, paired observations')
 for dt,c,label in [('WEEKDAY','#b45a0a','Weekday'),('WEEKENDS/HOLIDAY','#74608d','Weekend')]:
  v=h[(h.DAY_TYPE==dt)&h.TIME_PER_HOUR.notna()];axs[2].plot(v.TIME_PER_HOUR,v.daily_boardings/1000,c=c,label=label,lw=2)
 axs[2].set(xlabel='Hour of day',ylabel='Network boardings per day (thousands)',title='Hourly profile across all reported stops',xticks=[0,6,12,18,23]);axs[2].legend()
 save(fig,'bus/distributions.png','Monthly day-type aggregates are not daily observations. Missing stop/day-type combinations remain missing; no artificial zero-filled records. No September public holidays.')
if __name__=='__main__':bus_maps()
