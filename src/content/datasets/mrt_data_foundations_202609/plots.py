"""Original Chapter 2 figure plates and numerical audit. Offline Python + numpy/pandas/scipy/matplotlib."""
from pathlib import Path
import json,itertools
import numpy as np,pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from scipy.stats import norm,poisson,binom
P=Path(__file__).resolve().parent;F=P/'figures';F.mkdir(exist_ok=True)
font=P.parents[3]/'_static/css/fonts/ComicNeue-Regular.ttf'
if font.exists():font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']=['Comic Neue','DejaVu Sans']
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
j=pd.read_csv(P/'data/od_joined.csv').sort_values('TOTAL_TRIPS').reset_index(drop=True);x=j.TOTAL_TRIPS.to_numpy(dtype=float);n=len(x);assert n==12
colors=['#f1ca8a','#cf8a40','#904814']
def save(fig,name,foot):
 fig.text(.02,.015,foot,fontsize=9,color='#64594b');fig.savefig(F/name,dpi=165,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(1,3,figsize=(15,5.3));fig.subplots_adjust(left=.06,right=.98,top=.8,bottom=.22,wspace=.33)
edges=np.arange(0,4501,500);axs[0].hist(x,bins=edges,color=colors[1],ec='white');axs[0].plot(x,np.zeros(n)-.15,'|',c=colors[2]);axs[0].set(xlabel='Reported trips per OD pair',ylabel='OD-pair records',title='Histogram: counts of records',ylim=(-.3,6),yticks=range(0,7,2))
axs[1].step(np.r_[0,x,4500],np.r_[0,np.arange(1,n+1)/n,1],where='post',c=colors[2],lw=2);axs[1].scatter([538],[8/12],c=colors[2]);axs[1].annotate('F(538) = 8/12',(538,8/12),(1450,.53),arrowprops={'arrowstyle':'-','color':'#777'},fontsize=11);axs[1].set(xlabel='Reported trips per OD pair',ylabel='Fraction of OD-pair records',title='Empirical cumulative distribution',ylim=(0,1.05))
axs[2].boxplot(x,vert=False,patch_artist=True,boxprops={'facecolor':colors[0]},medianprops={'color':colors[2]},flierprops={'marker':'o','markerfacecolor':'white','markeredgecolor':colors[2]});axs[2].set(xlabel='Reported trips per OD pair',title='Box plot: flags are not errors',yticks=[])
for ax in axs:ax.set_xlim(0,4500)
fig.suptitle('One small sample, three descriptive views',fontsize=19)
save(fig,'05_empirical_distribution.png','LTA supplied Sep 2026 WEEKDAY, hour category 08; only pairs between the four selected stations. n=12; quartiles use linear interpolation. No full-network distribution is inferred.')
fig,axs=plt.subplots(1,3,figsize=(14,5));fig.subplots_adjust(left=.07,right=.98,top=.78,bottom=.23,wspace=.35)
z=np.linspace(-4,4,400);axs[0].plot(z,norm.pdf(z),c=colors[2],lw=2);axs[0].fill_between(z,norm.pdf(z),color=colors[0]);axs[0].set(title='Normal: mean 0, SD 1',xlabel='Continuous outcome',ylabel='Probability density')
for ax,dist,title in [(axs[1],poisson(4),'Poisson: expected count 4'),(axs[2],binom(10,.5),'Binomial: 10 trials, p=0.5')]:
 k=np.arange(0,13 if ax==axs[1] else 11);ax.vlines(k,0,dist.pmf(k),color=colors[2],lw=2);ax.scatter(k,dist.pmf(k),c=colors[1]);ax.set(title=title,xlabel='Discrete outcome',ylabel='Probability mass',ylim=(0,.3))
fig.suptitle('Probability models: conceptual illustrations, not MRT fits',fontsize=18)
save(fig,'06_probability_models.png','Parameters are chosen for illustration. Normal density integrates to one; probability masses sum to one over their full support. The Poisson plot shows outcomes 0–12, truncating a small upper tail.')
fig,axs=plt.subplots(2,2,figsize=(12,7));fig.subplots_adjust(left=.08,right=.98,top=.85,bottom=.14,hspace=.45,wspace=.25)
trans=[(x,'Original counts','Reported trips'),((x-x.min())/(x.max()-x.min()),'Min–max scaling','Scaled value (0–1)'),((x-x.mean())/x.std(ddof=1),'Standardisation','Sample z-score'),(np.log1p(x),'Natural log of (1 + count)','Transformed value')]
for ax,(v,title,ylabel) in zip(axs.flat,trans):ax.bar(np.arange(1,n+1),v,color=colors[1]);ax.axhline(0,c='#776c5d',lw=.7);ax.set(title=title,xlabel='Same records in ascending original-count order',ylabel=ylabel,xticks=[1,4,8,12])
fig.suptitle('Change the scale deliberately; preserve the original observations',fontsize=18)
save(fig,'07_transformations.png','All panels use the same 12 OD records. Standardisation uses sample SD (ddof=1). These are transformed values, not separately re-estimated observations or claims of normality.')
# Exact contiguous, non-empty three-class SSE partition; exhaustive search is sufficient for twelve records.
best=min((sum(float(((g-g.mean())**2).sum()) for g in [x[:i],x[i:k],x[k:]]),i,k) for i in range(1,n-1) for k in range(i+1,n))
eq=np.linspace(x.min(),x.max(),4)[1:-1];qt=np.quantile(x,[1/3,2/3],method='linear');nb=np.array([x[best[1]-1],x[best[2]-1]])
classes={name:np.searchsorted(br,x,side='left') for name,br in [('Equal intervals',eq),('Quantiles',qt),('Natural breaks',nb)]}
fig,axs=plt.subplots(1,3,figsize=(16,7));fig.subplots_adjust(left=.16,right=.98,top=.82,bottom=.18,wspace=.12)
labels=(j.origin_name+' → '+j.destination_name).tolist()
for ax,(name,cl) in zip(axs,classes.items()):
 ax.barh(np.arange(n),x,color=[colors[i] for i in cl],height=.65);ax.set(yticks=np.arange(n),yticklabels=labels if ax==axs[0] else ['']*n,xlim=(0,4700),xlabel='Reported trips (same scale)',title=name+'\nclass sizes '+ '/'.join(str(int((cl==i).sum())) for i in range(3)));ax.invert_yaxis()
 for i,val in enumerate(x):ax.text(val+35,i,f'{val:,.0f}',va='center',fontsize=9)
from matplotlib.patches import Patch
fig.legend(handles=[Patch(fc=c,label=l) for c,l in zip(colors,['Lower class','Middle class','Upper class'])],loc='lower center',bbox_to_anchor=(.6,.075),ncol=3,frameon=False)
fig.suptitle('Classification changes grouping, not the trip observations',fontsize=19)
save(fig,'08_classification.png','Three classes, same selected sample. Interior breaks are right-closed (a value on a break enters the lower class). Quantiles use linear interpolation; natural breaks minimise within-class SSE exactly.')
a={'n':n,'sorted_counts':x.astype(int).tolist(),'sum':int(x.sum()),'mean':float(x.mean()),'median':float(np.median(x)),'sample_sd':float(x.std(ddof=1)),'quartiles_linear':np.quantile(x,[.25,.75],method='linear').tolist(),'histogram_edges':edges.tolist(),'histogram_frequencies':np.histogram(x,edges)[0].tolist(),'classifications':{name:{'interior_breaks':br.tolist(),'counts':[int((classes[name]==i).sum()) for i in range(3)]} for name,br in [('Equal intervals',eq),('Quantiles',qt),('Natural breaks',nb)]},'natural_breaks_within_sse':best[0],'first_head_tail_mean':float(x.mean()),'head_count':int((x>x.mean()).sum()),'transformation_examples':{str(int(v)):{'minmax':float((v-x.min())/(x.max()-x.min())),'sample_z':float((v-x.mean())/x.std(ddof=1)),'log1p':float(np.log1p(v))} for v in [50,500,4294]}}
(P/'data/descriptive_audit.json').write_text(json.dumps(a,indent=2));assert [int((classes['Equal intervals']==i).sum()) for i in range(3)]==[10,0,2];assert [int((classes['Quantiles']==i).sum()) for i in range(3)]==[4,4,4];assert [int((classes['Natural breaks']==i).sum()) for i in range(3)]==[8,2,2]
print('Wrote 4 original plates and descriptive_audit.json')
