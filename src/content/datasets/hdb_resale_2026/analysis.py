"""Rebuild Chapter 5 review figures from prepared HDB transactions (no network)."""
from pathlib import Path
import sys,json
P=Path(__file__).resolve().parent;D=P/'data';F=P/'figures';F.mkdir(exist_ok=True)
sys.path.insert(0,str(P))
import plots
import numpy as np,pandas as pd, matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.cluster import KMeans,DBSCAN
from scipy.spatial import ConvexHull
from shapely.geometry import shape
from shapely.ops import unary_union,transform
from shapely import contains_xy
h=pd.read_csv(P/'hdb/transactions.csv.xz');xy=h[['x','y']].to_numpy();upper=h.price_group.eq('upper');lower=h.price_group.eq('lower')
land=unary_union([shape(f['geometry']) for f in plots.CONTEXT['features']]);land=transform(plots.T.transform,land)
gx=np.arange(0,58001,300);gy=np.arange(14000,54001,300);xx,yy=np.meshgrid(gx,gy);grid=np.c_[xx.ravel(),yy.ravel()];mask=contains_xy(land,xx,yy)
def kde(points,bw):return np.exp(KernelDensity(bandwidth=bw).fit(points).score_samples(grid)).reshape(xx.shape)*1e6
def outlines(ax):
 from matplotlib.patches import PathPatch
 for patch in list(ax.patches):
  ax.add_patch(PathPatch(patch.get_path(),fc='none',ec='#afa998',lw=.3,zorder=2))
def finish(fig,name):
 fig.get_layout_engine().set(rect=(0,.04,1,.96));fig.savefig(F/name,dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,4.4),layout='constrained');v=h.resale_price.to_numpy()/1000;u=np.linspace(300,1700,700)
ax.hist(v,bins=35,density=True,color='#eacbaa',ec='white',label='Histogram')
for bw,c in [(15,'#d89147'),(40,'#a44b0d'),(100,'#57496f')]:
 y=np.exp(KernelDensity(bandwidth=bw).fit(v[:,None]).score_samples(u[:,None]));ax.plot(u,y,label=f'h = S${bw:,},000',c=c,lw=2)
ax.set(xlabel='Resale price (S$ thousands)',ylabel='Probability density per S$1,000',title='Same prices, three degrees of smoothing');ax.legend();finish(fig,'price_kde.png')
fig,axs=plt.subplots(1,3,figsize=(15,5.4),layout='constrained');fields=[kde(xy,700)*len(xy),kde(xy[lower],700)*lower.sum(),kde(xy[upper],700)*upper.sum()];vmax=max(f.max() for f in fields)
for ax,f,title in zip(axs,fields,['All sales','Lower-price group','Upper-price group']):
 plots.background(ax);im=ax.pcolormesh(xx/1000,yy/1000,np.where(mask,f,np.nan),cmap=plots.ORRD,vmin=0,vmax=vmax,shading='auto',zorder=1,rasterized=True);outlines(ax);ax.set_title(title)
fig.colorbar(im,ax=axs,label='Smoothed transactions per km² over six months',shrink=.65);fig.suptitle('Fixed-bandwidth intensity · Gaussian h = 700 m');finish(fig,'spatial_kde.png')
fig,axs=plt.subplots(1,3,figsize=(15,5.4),layout='constrained');fs=[kde(xy[upper],b) for b in [350,700,1400]];vmax=max(f.max() for f in fs)
for ax,f,bw in zip(axs,fs,[350,700,1400]):
 plots.background(ax);im=ax.pcolormesh(xx/1000,yy/1000,np.where(mask,f,np.nan),cmap=plots.ORRD,vmin=0,vmax=vmax,shading='auto',zorder=1);outlines(ax);ax.set_title(f'h = {bw:,} m')
fig.colorbar(im,ax=axs,label='Upper-group probability density per km²',shrink=.65);fig.suptitle('Bandwidth changes the apparent size and separation of concentrations');finish(fig,'bandwidth.png')
colors=['#b45b19','#6a5685','#31948b','#cfaa35','#ab6488','#5682a0','#777777']
fig,axs=plt.subplots(1,2,figsize=(12,5.6),layout='constrained');x=xy[upper];summary={'kmeans':{},'dbscan':{}}
for ax,k in zip(axs,[3,5]):
 model=KMeans(n_clusters=k,n_init=20,random_state=5230).fit(x);plots.background(ax)
 for c in range(k):
  v=x[model.labels_==c];ax.scatter(v[:,0]/1000,v[:,1]/1000,s=10,color=colors[c],lw=0)
 ax.scatter(model.cluster_centers_[:,0]/1000,model.cluster_centers_[:,1]/1000,c='#222',marker='x',s=55);ax.set_title(f'k = {k}: every transaction assigned');summary['kmeans'][str(k)]={'inertia_m2':float(model.inertia_),'sizes':np.bincount(model.labels_).tolist()}
fig.suptitle('K-means on upper-group transaction locations');finish(fig,'kmeans.png')
fig,axs=plt.subplots(1,3,figsize=(15,5.4),layout='constrained');chosen=None
for ax,eps in zip(axs,[300,600,1000]):
 model=DBSCAN(eps=eps,min_samples=20).fit(x);lab=model.labels_;plots.background(ax);ax.scatter(x[:,0]/1000,x[:,1]/1000,c='#c8c8c8',s=7,lw=0)
 for c in sorted(set(lab)-{-1}):
  v=x[lab==c];ax.scatter(v[:,0]/1000,v[:,1]/1000,s=9,color=colors[c%len(colors)],lw=0)
 n=len(set(lab)-{-1});noise=int((lab==-1).sum());ax.set_title(f'ε = {eps:,} m\n{n} clusters; {noise} noise transactions');summary['dbscan'][str(eps)]={'clusters':n,'noise':noise}
 if eps==600:chosen=lab
fig.suptitle('DBSCAN sensitivity · min_samples = 20 transactions (including self)');finish(fig,'dbscan.png')
fig,axs=plt.subplots(1,2,figsize=(12,5.6),layout='constrained')
for ax in axs:plots.background(ax)
for c in sorted(set(chosen)-{-1}):
 v=np.unique(x[chosen==c],axis=0);color=colors[c%len(colors)]
 for ax in axs:ax.scatter(v[:,0]/1000,v[:,1]/1000,s=9,color=color,lw=0)
 if len(v)>=3:
  try:
   hull=ConvexHull(v);q=v[hull.vertices]/1000;axs[1].fill(q[:,0],q[:,1],fc=color,alpha=.15,ec=color,lw=1)
  except Exception:pass
noise=x[chosen==-1]
for ax in axs:ax.scatter(noise[:,0]/1000,noise[:,1]/1000,s=6,color='#aaa',lw=0)
axs[0].set_title('Observed block locations, coloured by cluster');axs[1].set_title('The same clusters with convex hulls');fig.suptitle('A cluster envelope summarises members; it is not a housing-market boundary');finish(fig,'hulls.png')
(P/'results.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary),flush=True)
