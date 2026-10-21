"""Observed FIRMS areal example: explicit NumPy statistics and randomisation.
Run from the repository root; --check verifies saved outputs without rewriting them.
No esda defaults or version-specific categorical labels are used.
"""
from pathlib import Path
import argparse, hashlib, json, platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Patch

B=9999
SEED=5230
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'src/content/datasets/firms_sumatra'
OUT=ROOT/'src/content/datasets/firms_areal'
FIG=ROOT/'src/content/resources/original'

def bh(p):
    p=np.asarray(p);order=np.argsort(p);rank=np.arange(1,len(p)+1)
    q=np.minimum.accumulate((p[order]*len(p)/rank)[::-1])[::-1]
    out=np.empty(len(p));out[order]=np.minimum(q,1);return out

def tails(observed,simulated):
    ties=np.isclose(simulated,observed,rtol=1e-12,atol=1e-12)
    lo=(1+np.count_nonzero((simulated<observed)|ties,axis=0))/(len(simulated)+1)
    hi=(1+np.count_nonzero((simulated>observed)|ties,axis=0))/(len(simulated)+1)
    return lo,hi,np.minimum(1,2*np.minimum(lo,hi))

def graph(cells,queen=False):
    dc=abs(cells.col.to_numpy()[:,None]-cells.col.to_numpy()[None,:])
    dr=abs(cells.row.to_numpy()[:,None]-cells.row.to_numpy()[None,:])
    return (((np.maximum(dc,dr)==1) if queen else (dc+dr==1))).astype(float)

def global_stats(x,A):
    W=A/A.sum(1)[:,None];n=len(x);d=x-x.mean();Q=d@d;S=W.sum()
    I=n/S*(d@(W@d))/Q
    C=(n-1)/(2*S)*np.sum(W*(x[:,None]-x[None,:])**2)/Q
    G=np.sum(A*x[:,None]*x[None,:])/(x.sum()**2-x@x)
    return np.array([I,C,G])

def analyse(cells,A,B=B,seed=SEED):
    n=len(cells);x=cells['count'].to_numpy(float);d=x-x.mean();m2=np.mean(d*d);z=d/np.sqrt(m2)
    W=A/A.sum(1)[:,None];lag=W@z
    localI=z*lag
    localC=np.sum(W*(z[:,None]-z[None,:])**2,axis=1)
    star=A+np.eye(n);gstar=star@x/x.sum()
    gi=(A@x)/(x.sum()-x)
    observed=global_stats(x,A)
    rng=np.random.default_rng(seed)
    global_sim=np.array([global_stats(rng.permutation(x),A) for _ in range(B)])
    result=cells.copy();result['neighbours']=A.sum(1).astype(int);result['z']=z;result['lag_z']=lag
    result['local_I']=localI;result['local_C']=localC;result['Gi']=gi;result['Gi_star']=gstar
    quadrant=np.where((z>0)&(lag>0),'HH',np.where((z<0)&(lag<0),'LL',np.where((z>0)&(lag<0),'HL',np.where((z<0)&(lag>0),'LH','Axis'))))
    result['quadrant']=quadrant
    directions={};all_sims={}
    for stat in ['I','C','Gstar']:all_sims[stat]=np.empty((B,n))
    for i in range(n):
        others=np.delete(np.arange(n),i);k=int(A[i].sum())
        # IID random-key rankings give uniform subsets without replacement per row.
        chosen=np.argpartition(rng.random((B,n-1)),k-1,axis=1)[:,:k]
        neighbours=others[chosen]
        all_sims['I'][:,i]=z[i]*z[neighbours].mean(1)
        all_sims['C'][:,i]=np.mean((z[i]-z[neighbours])**2,axis=1)
        all_sims['Gstar'][:,i]=(x[i]+x[neighbours].sum(1))/x.sum()
    for name,obs in [('I',localI),('C',localC),('Gstar',gstar)]:
        sim=all_sims[name];lo,hi,p=tails(obs,sim);q=bh(p)
        result[name+'_p_lower']=lo;result[name+'_p_upper']=hi;result[name+'_p_two']=p;result[name+'_q_bh']=q
        mu=sim.mean(0);sd=sim.std(0,ddof=1)
        result[name+'_conditional_mean']=mu
        result[name+'_z_perm']=(obs-mu)/sd
        directions[name]=np.where(obs<mu,'Below','Above')
    result['geary_direction']=np.where(localC<result.C_conditional_mean,'Similar','Dissimilar')
    result['gstar_direction']=np.where(gstar<result.Gstar_conditional_mean,'Cold','Hot')
    assert np.isclose(localI.sum(),W.sum()*observed[0])
    assert np.isclose(localC.sum()*(n-1)/(2*W.sum()*n),observed[1])
    assert np.allclose(global_stats(3*x+7,A)[:2],observed[:2])
    assert np.allclose(global_stats(3*x,A),observed)
    assert np.array_equal(np.diag(A),np.zeros(n)) and np.all(A.sum(1)>0)
    from scipy.sparse.csgraph import connected_components
    components=connected_components(A,directed=False)[0]
    assert components==1
    stats={}
    for j,name in enumerate(['Moran_I','Geary_C','General_G']):
        lo,hi,p=tails(observed[j],global_sim[:,j]);stats[name]={'observed':float(observed[j]),'p_lower':float(lo),'p_upper':float(hi),'p_two':float(p)}
    stats.update(n=n,detections=int(x.sum()),mean=float(x.mean()),B=B,seed=seed,components=int(components),isolates=0,undirected_edges=int(A.sum()/2),min_neighbours=int(A.sum(1).min()),max_neighbours=int(A.sum(1).max()),local={name:{'unadjusted_005':int((result[name+'_p_two']<=.05).sum()),'BH_005':int((result[name+'_q_bh']<=.05).sum()),'Bonferroni_005':int((result[name+'_p_two']<=.05/n).sum())} for name in ['I','C','Gstar']})
    return result,stats,global_sim

def load_cells():
    source=pd.read_csv(DATA/'detections.csv.gz');meta=json.loads((DATA/'assessment.json').read_text());west,south,_,_=meta['windows'][0]['bounds_m']
    cols=np.floor((source.easting_m-west)/20000).astype(int);rows=np.floor((source.northing_m-south)/20000).astype(int)
    grid=np.zeros((5,10),dtype=int);np.add.at(grid,(rows,cols),1)
    area=np.hstack([np.array(s['land_cell_area_km2']) for s in meta['windows']])
    records=[]
    for row in range(5):
        for col in range(10):
            records.append(dict(cell=f'R{row+1}C{col+1:02}',row=row,col=col,count=int(grid[row,col]),land_km2=float(area[row,col]),included=bool(abs(area[row,col]-400)<1e-6)))
    allcells=pd.DataFrame(records);cells=allcells[allcells.included].reset_index(drop=True)
    assert len(cells)==48 and cells['count'].sum()==6097
    return allcells,cells

PALETTE={'HH':'#b65b13','LL':'#6656a6','HL':'#dcae36','LH':'#4d8d99','Axis':'#777777','Similar':'#b78b45','Dissimilar':'#6656a6','Hot':'#b65b13','Cold':'#6656a6','NS':'#e5e5e5'}
def gridmap(ax,allcells,values,categorical=False,vmin=None,vmax=None,cmap='OrRd'):
    norm=plt.Normalize(vmin,vmax) if not categorical else None
    lookup={f'R{int(r.row)+1}C{int(r.col)+1:02}':v for r,v in zip(allcells[allcells.included].itertuples(),values)}
    for r in allcells.itertuples():
        v=lookup.get(r.cell)
        colour=PALETTE.get(v,'white') if categorical else (plt.get_cmap(cmap)(norm(v)) if v is not None else 'white')
        ax.add_patch(Rectangle((r.col*20,r.row*20),20,20,facecolor=colour,edgecolor='#777777',lw=.6,hatch='///' if not r.included else None))
    ax.axvline(100,color='#333333',lw=1.3);ax.set(xlim=(0,200),ylim=(0,100),aspect='equal',xlabel='km east of western origin',ylabel='km north of shared origin')

def figures(allcells,r,stats,sim):
    font=ROOT/'_static/css/fonts/ComicNeue-Regular.ttf'
    if font.exists():font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']='Comic Neue'
    plt.rcParams['svg.hashsalt']='firms-areal-5230'
    def save(fig,name):
        fig.savefig(FIG/name,metadata={'Date':None});plt.close(fig)
    fig,axs=plt.subplots(1,2,figsize=(13,4.3),layout='constrained')
    gridmap(axs[0],allcells,r['count'],vmin=0,vmax=1207);axs[0].set_title('Observed satellite detections\n48 full-land cells; 20 km grid')
    gridmap(axs[1],allcells,r.neighbours,vmin=1,vmax=4,cmap='YlOrBr');axs[1].set_title('Rook neighbour counts\nOne component; no isolates')
    fig.colorbar(plt.cm.ScalarMappable(norm=plt.Normalize(0,1207),cmap='OrRd'),ax=axs[0],label='Detections',shrink=.65)
    fig.colorbar(plt.cm.ScalarMappable(norm=plt.Normalize(1,4),cmap='YlOrBr'),ax=axs[1],label='Neighbours',shrink=.65)
    fig.suptitle('South Sumatra · 1–30 September 2026 · hatched cells excluded',fontsize=15);save(fig,'firms-areal-support.svg')
    fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
    axs[0].scatter(r.z,r.lag_z,c='#b65b13',s=28);axs[0].axhline(0,c='#999999',lw=.7);axs[0].axvline(0,c='#999999',lw=.7)
    xs=np.array([r.z.min(),r.z.max()]);axs[0].plot(xs,stats['Moran_I']['observed']*xs,c='#6656a6');axs[0].set(xlabel='Standardised cell count z',ylabel='Row-standardised spatial lag Wz',title=f"Moran scatterplot: I = {stats['Moran_I']['observed']:.3f}")
    axs[1].hist(sim[:,0],bins=40,color='#d7bb8b',edgecolor='white');axs[1].axvline(stats['Moran_I']['observed'],color='#b65b13',lw=2,label='Observed I');axs[1].set(xlabel="Moran's I",ylabel='Permutation frequency',title='9,999 unrestricted permutations');axs[1].legend();save(fig,'firms-moran-observed.svg')
    for name,types,title,filename in [('I',r.quadrant,'Local Moran: similarity and contrast','firms-local-moran.svg'),('C',r.geary_direction,'Local Geary: conditional departure','firms-local-geary.svg'),('Gstar',r.gstar_direction,'Gi*: conditional high/low concentration','firms-local-gstar.svg')]:
        fig,axs=plt.subplots(1,2,figsize=(13,4.5),layout='constrained')
        for ax,col,label in zip(axs,[name+'_p_two',name+'_q_bh'],['Unadjusted two-sided p <= 0.05','BH-adjusted q <= 0.05']):
            categories=np.where(r[col]<=.05,types,'NS');gridmap(ax,allcells,categories,categorical=True);ax.set_title(label)
        labels=list(dict.fromkeys(types));handles=[Patch(facecolor=PALETTE[k],label=k) for k in labels]+[Patch(facecolor=PALETTE['NS'],label='Not selected'),Patch(facecolor='white',hatch='///',label='Excluded coastal cell')]
        fig.legend(handles=handles,loc='outside lower center',ncol=min(len(handles),6),frameon=False)
        fig.suptitle(title+' · fixed-focal-value permutations',fontsize=15);save(fig,filename)

def main(check=False):
    allcells,cells=load_cells();r,stats,sim=analyse(cells,graph(cells))
    queen_result,queen_stats,_=analyse(cells,graph(cells,True),B=B,seed=SEED)
    meta={'source':'../firms_sumatra/README.md','support':'Two adjoining 100 km squares; 20 km cells. Retain only cells with 400 km² land in the saved Natural Earth main-island mask; exclude R5C07 and R5C08, 104 detections. No zero-count cells deliberately removed.','land_area_caveat':'Full-land classification is relative to the generalized source boundary, not a claim of survey-accurate coastal geometry.','crs':'EPSG:32748','variable':'Raw nominal/high-confidence S-NPP VIIRS detections, 1–30 September 2026 UTC','global_weights':'I and C: row-standardised rook; General G: binary rook; same graph','local_weights':'I and C: row-standardised rook. Gi*: binary rook plus self weight 1. This difference is explicit and required by the selected definitions.','local_null':'Hold focal value fixed; sample k distinct indices from the other n-1 values without replacement. Same random draws for all three local statistics at a focal cell.','local_p':'Inclusive lower/upper Monte Carlo tails, add one; two-sided=min(1,2*min(p_lower,p_upper)). B=9999; seed=5230. Each method has a separate 48-test BH family.','BH_caveat':'BH is shown as an exploratory FDR adjustment, not guaranteed control under arbitrary spatial dependence. Bonferroni counts are provided as a dependence-robust family-wise comparison.','global_null':'Unrestricted permutation of the same counts on fixed cells/weights. I and General G upper-tail; C lower-tail for the stated alternatives.','versions':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__},'input_sha256':hashlib.sha256((DATA/'detections.csv.gz').read_bytes()).hexdigest(),'rook':stats,'queen_sensitivity':queen_stats}
    if check:
        # Independent hand-worked chain and exhaustive permutation expectations.
        import itertools
        chain=np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]],float)
        sample=np.array([2.,2.,8.,8.])
        assert np.allclose(global_stats(sample,chain)[:2],[.5,.375])
        exact=np.array([global_stats(np.array(p),chain) for p in itertools.permutations(sample)])
        assert np.allclose(exact.mean(0)[:2],[-1/3,1])
        assert np.isclose(exact[:,2].mean(),chain.sum()/12)
        assert np.allclose(bh([.001,.01,.04,.2]),[.004,.02,.16/3,.2])
        assert np.array_equal(r.I_p_two,r.Gstar_p_two)
        old=pd.read_csv(OUT/'cell_results.csv');assert old.cell.tolist()==r.cell.tolist()
        assert np.allclose(old.select_dtypes('number'),r.select_dtypes('number'),rtol=1e-10,atol=1e-10)
        print('Saved counts, statistics, permutation tails and BH outputs reproduced.')
    else:
        OUT.mkdir(exist_ok=True);r.to_csv(OUT/'cell_results.csv',index=False);allcells.to_csv(OUT/'grid_support.csv',index=False);(OUT/'analysis.json').write_text(json.dumps(meta,indent=2)+'\n');figures(allcells,r,stats,sim)
    print(json.dumps({'rook':stats,'queen':queen_stats},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');main(parser.parse_args().check)
