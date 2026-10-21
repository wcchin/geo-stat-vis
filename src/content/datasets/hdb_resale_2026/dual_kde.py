"""Dual KDE: normalized densities, local shares and explicit support masks.
Same fixed isotropic Gaussian kernel, 700 m SD, 300 m grid in EPSG:3414.
Use co-located block counts as weights: algebraically identical to individual sales.
"""
from pathlib import Path
import json
import numpy as np,pandas as pd,matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from shapely.geometry import shape
from shapely.ops import unary_union,transform
from shapely import contains_xy
import plots
P=Path(__file__).resolve().parent;b=pd.read_csv(P/'hdb/blocks.csv.xz');xy=b[['x','y']].to_numpy();weights=b[['transactions','lower','upper']].to_numpy();counts=weights.sum(axis=0)
gx=np.arange(0,58001,300);gy=np.arange(14000,54001,300);xx,yy=np.meshgrid(gx,gy);grid=np.c_[xx.ravel(),yy.ravel()];bw=700.
intensity=np.empty((len(grid),3))
for i in range(0,len(grid),256):
 delta=grid[i:i+256,None,:]-xy[None,:,:];d2=np.sum(delta*delta,axis=2);kernel=np.exp(-d2/(2*bw*bw))/(2*np.pi*bw*bw)*1e6;intensity[i:i+256]=kernel@weights
all_,low,high=[intensity[:,i].reshape(xx.shape) for i in range(3)]
land=transform(plots.T.transform,unary_union([shape(f['geometry']) for f in plots.CONTEXT['features']]));mask=contains_xy(land,xx,yy)
support=mask&(all_>=5);both=support&(low>=1)&(high>=1)
# No pseudocounts: evaluate ratios only where their denominators have support.
rh=np.divide(high,all_,out=np.full_like(all_,np.nan),where=support)/(counts[2]/counts[0]);rl=np.divide(low,all_,out=np.full_like(all_,np.nan),where=support)/(counts[1]/counts[0]);rhl=np.divide(high/counts[2],low/counts[1],out=np.full_like(all_,np.nan),where=both)
assert np.allclose(rh[support]*(counts[2]/counts[0]),(high/all_)[support])
assert np.nanmax(rh)<=counts[0]/counts[2]+1e-8
assert np.nanmax(rl)<=counts[0]/counts[1]+1e-8
fig,axs=plt.subplots(1,3,figsize=(15,5.6),layout='constrained');norm=TwoSlopeNorm(vmin=-2,vcenter=0,vmax=2)
for ax,r,valid,title in zip(axs,[rh,rl,rhl],[support,support,both],['High / all','Low / all','High / low']):
 plots.background(ax)
 # Grey indicates insufficient support, distinct from the near-white neutral ratio.
 im=ax.pcolormesh(xx/1000,yy/1000,np.ma.masked_where(~valid,np.log2(r)),cmap='PuOr_r',norm=norm,shading='auto',zorder=1)
 from matplotlib.patches import PathPatch
 for patch in list(ax.patches):ax.add_patch(PathPatch(patch.get_path(),fc='none',ec='#aaa697',lw=.3,zorder=2))
 ax.set_title(title+'\nSeparately normalized probability densities')
cb=fig.colorbar(im,ax=axs,label='Density ratio (log₂-spaced scale)',shrink=.65,extend='both');cb.set_ticks([-2,-1,0,1,2],labels=['1/4','1/2','1','2','4'])
fig.suptitle('Dual KDE: relative representation of price groups · h = 700 m',fontsize=16)
fig.get_layout_engine().set(rect=(0,.09,1,.91));fig.text(.015,.02,'Masked cells retain the grey basemap. High/all and low/all: all-sales intensity ≥5/km². High/low additionally requires each group ≥1/km². Scale saturates beyond 1/4–4.',fontsize=9)
fig.savefig(P/'figures/dual_kde.png',dpi=180);plt.close(fig)
np.savez_compressed(P/'data/dual_kde_surfaces.npz',x=gx,y=gy,all_intensity=all_,low_intensity=low,high_intensity=high,land_mask=mask,support_mask=support,both_mask=both,high_all=rh,low_all=rl,high_low=rhl)
report={'bandwidth_m':bw,'grid_m':300,'all_support_per_km2':5,'each_group_support_per_km2_for_high_low':1,'counts_all_low_high':counts.tolist(),'retained_grid_cells_high_all_low_all':int(support.sum()),'retained_grid_cells_high_low':int(both.sum()),'land_grid_cells':int(mask.sum()),'display_log2_limits':[-2,2]};(P/'data/dual_kde_audit.json').write_text(json.dumps(report,indent=2));print(report)
