"""Original point-pattern examples: synthetic coordinates in a 2000 m square.

Run --write to regenerate book SVGs, the coordinate CSV and result record.
Default invocation verifies the calculations. No empirical lightning data are used.
"""
from pathlib import Path
import argparse
import json
import numpy as np
from scipy.spatial import distance
from scipy.stats import chi2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'src/content/resources/original'
DATA=ROOT/'src/content/datasets/point_pattern_teaching'
WINDOW=(0.,0.,2000.,2000.)
SEED=5230

def validate(points,window=WINDOW):
    p=np.asarray(points,dtype=float)
    x0,y0,x1,y1=window
    if p.ndim!=2 or p.shape[1]!=2 or len(p)<2 or not np.isfinite(p).all():
        raise ValueError('At least two finite x/y coordinates are required.')
    if not x1>x0 or not y1>y0:raise ValueError('Window must have positive area.')
    if ((p[:,0]<x0)|(p[:,0]>x1)|(p[:,1]<y0)|(p[:,1]>y1)).any():
        raise ValueError('Points fall outside the fixed observation window.')
    return p

def examples():
    rng=np.random.default_rng(SEED)
    csr=rng.uniform(0,2000,(96,2))
    centres=np.array([[700,700],[1300,1300],[700,1300],[1300,700]])
    clustered=np.vstack([c+rng.normal(0,85,(24,2)) for c in centres])
    xx,yy=np.meshgrid((np.arange(12)+.5)*2000/12,(np.arange(8)+.5)*250)
    regular=np.c_[xx.ravel(),yy.ravel()]+rng.uniform(-10,10,(96,2))
    return {'CSR realisation':csr,'Clustered construction':clustered,'Spaced construction':regular}

def quadrat(points,xedges,yedges,window=WINDOW):
    p=validate(points,window)
    if not np.allclose([xedges[0],yedges[0],xedges[-1],yedges[-1]],window):
        raise ValueError('Grid must partition the complete fixed window.')
    counts=np.histogram2d(p[:,0],p[:,1],bins=(xedges,yedges))[0].T
    area=np.outer(np.diff(yedges),np.diff(xedges))
    expected=len(p)*area/area.sum()
    stat=float(np.sum((counts-expected)**2/expected))
    return counts,expected,stat

def nna(points,window=WINDOW):
    p=validate(points,window);dist=distance.cdist(p,p);np.fill_diagonal(dist,np.inf)
    observed=float(dist.min(1).mean());x0,y0,x1,y1=window
    expected=.5/np.sqrt(len(p)/((x1-x0)*(y1-y0)))
    return observed,float(expected),float(observed/expected)

def k_translation(points,radii,window=WINDOW):
    """Rectangular translation-corrected, ordered-pair K estimator.

    Unordered pairs are multiplied by two. The overlap area for displacement
    h is (width-|h_x|)(height-|h_y|); coefficient is A^2/[n(n-1)].
    """
    p=validate(points,window);x0,y0,x1,y1=window
    width,height=x1-x0,y1-y0;area=width*height
    i,j=np.triu_indices(len(p),1);delta=np.abs(p[i]-p[j]);d=np.sqrt((delta**2).sum(1))
    overlap=(width-delta[:,0])*(height-delta[:,1])
    if np.any(overlap<=0):raise ValueError('Zero-overlap displacement; check boundary points.')
    return np.array([2*area**2/(len(p)*(len(p)-1))*np.sum(1/overlap[d<=r]) for r in radii])

def analysis(patterns,simulations=999):
    edges=np.linspace(0,2000,5);radii=np.linspace(25,500,40)
    rng=np.random.default_rng(SEED+1)
    null_t=np.empty(simulations);null_k=np.empty((simulations,len(radii)))
    for b in range(simulations):
        p=rng.uniform(0,2000,(96,2));null_t[b]=quadrat(p,edges,edges)[2]
        null_k[b]=k_translation(p,radii)
    result={}
    for name,p in patterns.items():
        c,e,t=quadrat(p,edges,edges);obs,exp,ratio=nna(p);k=k_translation(p,radii)
        result[name]={'n':len(p),'quadrat_T':t,'quadrat_df':15,
          'quadrat_p_chi2_upper':float(chi2.sf(t,15)),
          'quadrat_p_mc_upper':float((1+np.sum(null_t>=t))/(simulations+1)),
          'mean_nn_m':obs,'theoretical_nn_m':exp,'R':ratio,
          'K_translation':k.tolist()}
    return radii,null_t,null_k,result

def draw(patterns,radii,null_t,null_k,result):
    from matplotlib import font_manager
    font=ROOT/'_static/css/fonts/ComicNeue-Regular.ttf'
    if font.exists():font_manager.fontManager.addfont(str(font));family='Comic Neue'
    else:family='DejaVu Sans'
    plt.rcParams.update({'font.family':family,'font.size':11,'svg.fonttype':'path',
                         'svg.hashsalt':'ge5230-point-patterns','axes.spines.top':False,'axes.spines.right':False})
    OUT.mkdir(parents=True,exist_ok=True)
    def save(fig,name):
        fig.savefig(OUT/name,bbox_inches='tight',metadata={'Date':None})
        plt.close(fig)
    edges=np.linspace(0,2000,5)
    fig,axes=plt.subplots(1,3,figsize=(12,4))
    for ax,(name,p) in zip(axes,patterns.items()):
        ax.scatter(*p.T,s=9,color='#633609');c,e,t=quadrat(p,edges,edges)
        for edge in edges:ax.axhline(edge,color='#aaa',lw=.5);ax.axvline(edge,color='#aaa',lw=.5)
        for row in range(4):
            for col in range(4):ax.text((col+.5)*500,(row+.5)*500,str(int(c[row,col])),ha='center',va='center',fontsize=11,bbox={'facecolor':'white','alpha':.8,'edgecolor':'none'})
        ax.set(xlim=(0,2000),ylim=(0,2000),aspect='equal',title=f'{name}\nT = {t:.2f}',xlabel='x (m)',ylabel='y (m)')
    fig.suptitle('Synthetic examples: same window, n = 96, sixteen quadrats, E = 6',fontsize=13)
    fig.tight_layout();save(fig,'quadrat-three-patterns.svg')
    fig,axes=plt.subplots(1,3,figsize=(12,4));p=patterns['Clustered construction']
    for ax,ed,title in zip(axes,[np.linspace(0,2000,3),edges,np.array([0,250,750,1250,1750,2000])],['1000 m cells','500 m cells','Shifted 500 m grid; clipped edges']):
        c,e,t=quadrat(p,ed,ed)
        ax.pcolormesh(ed,ed,c,cmap='OrRd',vmin=0,vmax=25,edgecolors='grey',linewidth=.6)
        for i in range(len(ed)-1):
            for j in range(len(ed)-1):ax.text((ed[j]+ed[j+1])/2,(ed[i]+ed[i+1])/2,str(int(c[i,j])),ha='center',va='center',fontsize=10,color='black',bbox={'facecolor':'white','alpha':.65,'edgecolor':'none'})
        ax.set(xlim=(0,2000),ylim=(0,2000),aspect='equal',title=f'{title}\nT = {t:.2f}',xlabel='x (m)',ylabel='y (m)')
    fig.suptitle('Same synthetic points; different partitions. Expected counts use cell area.',fontsize=13)
    fig.tight_layout();save(fig,'quadrat-grid-sensitivity.svg')
    fig,ax=plt.subplots(figsize=(7,3.5));ax.hist(null_t,bins=25,color='#f6b56c',edgecolor='white')
    obs=result['Clustered construction']['quadrat_T'];ax.axvline(obs,color='#8b2900',label=f'Constructed clustered T = {obs:.2f}')
    ax.set(xlabel='Quadrat statistic T',ylabel='Simulated patterns',title='999 conditional CSR simulations; fixed n, window and 4 x 4 grid');ax.legend(frameon=False)
    fig.tight_layout();save(fig,'quadrat-csr-reference.svg')
    # Bus-stop-inspired construction: one pair at each regularly spaced site.
    xx,yy=np.meshgrid([400,800,1200,1600],[400,800,1200,1600]);sites=np.c_[xx.ravel(),yy.ravel()]
    paired=np.vstack([sites+[-15,0],sites+[15,0]])
    fig,axes=plt.subplots(1,2,figsize=(10,4.5));ax=axes[0]
    ax.scatter(*paired.T,color='#93400c',s=15)
    for site in sites:ax.plot([site[0]-15,site[0]+15],[site[1],site[1]],color='#555',lw=1)
    for radius in [100,400,650]:ax.add_patch(plt.Circle(paired[0],radius,fill=False,alpha=.7,lw=1))
    ax.set(xlim=(0,2000),ylim=(0,2000),aspect='equal',xlabel='x (m)',ylabel='y (m)',title='Synthetic paired sites; circles centred on one point')
    radii2=np.linspace(5,500,100);k=k_translation(paired,radii2)
    axes[1].plot(radii2,np.sqrt(k/np.pi)-radii2,color='#963609');axes[1].axhline(0,color='#666',ls='--')
    axes[1].set(xlabel='Radius r (m)',ylabel='L(r) - r (m)',title='Translation-corrected, cumulative summary')
    fig.tight_layout();save(fig,'k-paired-sites.svg')
    fig,axes=plt.subplots(1,3,figsize=(12,4),sharey=True)
    null_l=np.sqrt(null_k/np.pi)-radii
    low,high=np.quantile(null_l,[.025,.975],axis=0)
    for ax,(name,p) in zip(axes,patterns.items()):
        ax.fill_between(radii,low,high,color='#f9d6a3',label='Pointwise 2.5–97.5% quantiles')
        ax.plot(radii,np.sqrt(np.asarray(result[name]['K_translation'])/np.pi)-radii,color='#923600',label='Observed construction')
        ax.axhline(0,color='#555',ls='--',lw=.8);ax.set(xlabel='Radius r (m)',title=name)
    axes[0].set_ylabel('L(r) - r (m)');axes[1].legend(fontsize=8,loc='lower left',frameon=False)
    fig.suptitle('Synthetic patterns; 999 fixed-n CSR simulations; translation correction',fontsize=13)
    fig.tight_layout();save(fig,'k-three-patterns-envelope.svg')

def verify():
    edges=np.array([0,1,2.]);p=np.array([[0,0],[1,0],[2,2],[.5,1.5]])
    c,e,t=quadrat(p,edges,edges,(0,0,2,2));assert c.sum()==4 and e.sum()==4
    # Explicit inclusion of points on internal and outer boundaries, once each.
    assert np.array_equal(c,[[1,1],[1,1]])
    p=np.array([[500,500],[1500,500]])
    assert np.isclose(nna(p)[0],1000)
    assert np.isclose(k_translation(p,[999])[0],0)
    # A=4e6, overlap=2e6, one unordered pair counted twice.
    assert np.isclose(k_translation(p,[1000])[0],8e6)
    counts=np.array([4,8,12,16]);assert np.isclose(np.sum((counts-10)**2/10),8)
    assert np.isclose(chi2.sf(8,3),.04601170568923136)
    patterns=examples()
    for name,p in patterns.items():
        assert len(p)==96;validate(p)
        assert quadrat(p,np.linspace(0,2000,5),np.linspace(0,2000,5))[0].sum()==96
    try:validate(np.array([[-1,0],[1,1]]))
    except ValueError:pass
    else:raise AssertionError('Outside-window input accepted')
    record=DATA/'results.json'
    if record.exists():
        stored=json.loads(record.read_text())
        radii=np.asarray(stored['radii_m'])
        for name,p in patterns.items():
            _,_,t=quadrat(p,np.linspace(0,2000,5),np.linspace(0,2000,5))
            assert np.isclose(t,stored['results'][name]['quadrat_T'])
            assert np.isclose(nna(p)[0],stored['results'][name]['mean_nn_m'])
            kvals=k_translation(p,radii)
            assert np.allclose(kvals,stored['results'][name]['K_translation'])
            assert np.all(np.diff(kvals)>=0)
    return patterns

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--write',action='store_true')
    args=parser.parse_args();patterns=verify()
    if args.write:
        radii,t,k,result=analysis(patterns);draw(patterns,radii,t,k,result)
        DATA.mkdir(parents=True,exist_ok=True)
        rows=['pattern,x_m,y_m']
        for name,p in patterns.items():rows += [f'{name},{x:.10f},{y:.10f}' for x,y in p]
        (DATA/'synthetic_points.csv').write_text('\n'.join(rows)+'\n')
        record={'synthetic':True,'seed':SEED,'simulation_seed':SEED+1,'simulations':999,
                'window_m':WINDOW,'radii_m':radii.tolist(),'results':result}
        (DATA/'results.json').write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({name:{k:v for k,v in values.items() if k!='K_translation'} for name,values in result.items()},indent=2))
    print('Point-pattern checks passed: cell boundaries, totals, quadrat arithmetic, NN distance and translation-corrected pair counting.')
