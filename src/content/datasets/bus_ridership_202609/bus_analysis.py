from pathlib import Path
import json
import numpy as np,pandas as pd, matplotlib.pyplot as plt
from scipy import stats
import plots
P=Path(__file__).resolve().parent
s=pd.read_csv(P/'bus/stops.csv.xz',dtype={'PT_CODE':str});p=s.dropna(subset=['weekday_daily','weekend_daily']).copy();d=p.difference.to_numpy();n=len(p)
# Classifications use labels, never ridership. They are a transparent teaching proxy.
p['stop_group']=np.select([p.Description.str.contains(r'\bInt$',case=False,regex=True,na=False),p.Description.str.contains(r'\bTer$',case=False,regex=True,na=False)],['Interchange label','Terminal label'],default='Other stop labels')
p.to_csv(P/'bus/paired_stops.csv.xz',index=False)
r=stats.ttest_rel(p.weekday_daily,p.weekend_daily);ci=r.confidence_interval();num=(p.TOTAL_TAP_IN_VOLUME_WEEKDAY*4-p['TOTAL_TAP_IN_VOLUME_WEEKENDS/HOLIDAY']*11).round().astype('int64');exactd=num/88;assert np.allclose(exactd,d);nz=num[num!=0]
w=stats.wilcoxon(exactd,zero_method='wilcox',method='asymptotic');groups=[g.weekday_daily.to_numpy() for _,g in p.groupby('stop_group')];f=stats.f_oneway(*groups);fw=stats.f_oneway(*groups,equal_var=False);kw=stats.kruskal(*groups)
a={'paired_n':n,'mean_weekday':p.weekday_daily.mean(),'mean_weekend':p.weekend_daily.mean(),'median_weekday':p.weekday_daily.median(),'median_weekend':p.weekend_daily.median(),'mean_difference':d.mean(),'median_difference':float(np.median(d)),'sd_difference':d.std(ddof=1),'se_iid':stats.sem(d),'t_iid':float(r.statistic),'p_t_iid':float(r.pvalue),'ci_iid':[float(ci.low),float(ci.high)],'positive':int((num>0).sum()),'negative':int((num<0).sum()),'ties':int((num==0).sum()),'wilcoxon_statistic':float(w.statistic),'wilcoxon_p_iid':float(w.pvalue),'sign_p_iid':float(stats.binomtest(int((num>0).sum()),len(nz),.5).pvalue),'anova_F_iid':float(f.statistic),'anova_p_iid':float(f.pvalue),'welch_F_iid':float(fw.statistic),'welch_p_iid':float(fw.pvalue),'kruskal_H_iid':float(kw.statistic),'kruskal_p_iid':float(kw.pvalue),'groups':p.groupby('stop_group').weekday_daily.agg(['count','mean','median','std']).to_dict('index')}
(P/'bus/analysis_results.json').write_text(json.dumps(a,indent=2));print(json.dumps(a,indent=2),flush=True)
plots.bus_maps()
def save(fig,name):
 fig.get_layout_engine().set(rect=(0,.05,1,.95));fig.savefig(P/'bus'/name,dpi=170);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
for col,c,label in [('weekday_daily','#ad5e18','Weekday'),('weekend_daily','#715a8c','Weekend')]:
 v=np.sort(p[col]);axs[0].hist(v,bins=np.linspace(0,5000,41),histtype='step',lw=1.8,color=c,label=label);axs[1].plot(v,np.arange(1,n+1)/n,c=c,label=label)
axs[0].set(xlabel='Daily-average boardings (0–5,000 view)',ylabel='Stops',title='Central range; larger values extend beyond this panel');axs[1].set(xscale='symlog',xlabel='Daily-average boardings (symlog scale)',ylabel='Cumulative fraction of stops',title='ECDF includes every paired stop')
for ax in axs:ax.legend()
save(fig,'distribution_details.png')
fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
axs[0].hist(d,bins=np.linspace(-2000,4000,61),color='#d89550',ec='white');axs[0].axvline(0,c='#555');axs[0].set(xlabel='Weekday minus weekend daily boardings',ylabel='Stops',title='Differences (−2,000 to 4,000 view; tails omitted)')
q=stats.probplot(d,dist='norm');axs[1].scatter(q[0][0],q[0][1],s=7,c='#a65e23');axs[1].plot(q[0][0],q[1][0]*q[0][0]+q[1][1],c='#777',ls='--');axs[1].set(xlabel='Theoretical normal quantile',ylabel='Observed paired difference',title='Q–Q plot includes every paired stop');save(fig,'paired_differences.png')
fig,axs=plt.subplots(1,2,figsize=(12,4.8),layout='constrained');order=['Interchange label','Terminal label','Other stop labels'];v=[p.loc[p.stop_group==g,'weekday_daily'] for g in order]
for ax,log in zip(axs,[False,True]):
 vals=[np.log1p(a) if log else a for a in v];ax.boxplot(vals,tick_labels=[f'{g}\n(n={len(a):,})' for g,a in zip(order,v)],showfliers=True,flierprops={'markersize':2,'alpha':.35},medianprops={'color':'#a45e19'});ax.set(ylabel='log(1 + daily-average boardings)' if log else 'Daily-average boardings',title='Weekday distributions on '+('log-transformed scale' if log else 'original scale'))
save(fig,'group_comparison.png')
fig,ax=plt.subplots(figsize=(8,3.6),layout='constrained');ax.barh(['Weekday higher','Weekend higher','Equal'],[a['positive'],a['negative'],a['ties']],color=['#b86c26','#76608b','#aaa']);ax.set(xlabel='Paired stops',title='Direction of the within-stop difference');ax.invert_yaxis()
for i,v in enumerate([a['positive'],a['negative'],a['ties']]):ax.text(v+20,i,f'{v:,}',va='center')
ax.set_xlim(0,a['positive']*1.15);save(fig,'signs.png')
