"""Shared Chapter 6 income analysis. Offline snapshots; --check reproduces saved outputs."""
from pathlib import Path
import argparse,gzip,hashlib,json
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch,Patch
from matplotlib.colors import BoundaryNorm,ListedColormap
from areal_statistics import analyse,global_stats,bh
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'src/content/datasets/malaysia_income_areal'
DISPLAY=ROOT/'src/content/datasets/peninsula_income_2022'
FIG=ROOT/'src/content/resources/original'

def build_graph(cells,k):
    xy=cells[['x_m','y_m']].to_numpy();dist=cdist(xy,xy);np.fill_diagonal(dist,np.inf)
    selected=np.argsort(dist,axis=1,kind='stable')[:,:k]
    A=np.zeros((len(cells),len(cells)));A[np.arange(len(cells))[:,None],selected]=1
    return np.maximum(A,A.T)

def display_geometries():
    layer=json.loads(gzip.decompress((DISPLAY/'boundaries_rso_display.json.gz').read_bytes()))
    return {str(f['attributes']['kod_daerah']):f['geometry']['rings'] for f in layer['features']}

COLOURS={'HH':'#b65b13','LL':'#6656a6','HL':'#dcae36','LH':'#4d8d99','Axis':'#777777','Similar':'#b78b45','Dissimilar':'#6656a6','Hot':'#b65b13','Cold':'#6656a6','NS':'#e5e5e5'}
def map_panel(ax,cells,geometries,values,categorical=False):
    cmap=ListedColormap(plt.get_cmap('OrRd')(np.linspace(.05,.95,5)));norm=BoundaryNorm([0,3000,5000,7000,9000,15000],5)
    for code,value in zip(cells.cell,values):
        verts=[];codes=[]
        for ring in geometries[code]:
            arr=np.asarray(ring)/1000;verts.extend(arr.tolist());codes.extend([MplPath.MOVETO]+[MplPath.LINETO]*(len(arr)-2)+[MplPath.CLOSEPOLY])
        colour=COLOURS[value] if categorical else cmap(norm(value))
        ax.add_patch(PathPatch(MplPath(verts,codes),facecolor=colour,edgecolor='#777777',lw=.35))
    ax.autoscale_view();ax.set_aspect('equal');ax.axis('off')
    return cmap,norm

def figures(cells,r,stats,sim,A):
    geometries=display_geometries();assert set(geometries)==set(cells.cell)
    font=ROOT/'_static/css/fonts/ComicNeue-Regular.ttf'
    if font.exists():font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']='Comic Neue'
    plt.rcParams['svg.hashsalt']='malaysia-income-5230'
    def save(fig,name):
        if name!='malaysia-income-moran.svg':
            name=name.replace('.svg','.png');fig.savefig(FIG/name,dpi=200)
        else:fig.savefig(FIG/name,metadata={'Date':None})
        plt.close(fig)
    fig,axs=plt.subplots(1,2,figsize=(9,6),layout='constrained')
    cmap,norm=map_panel(axs[0],cells,geometries,cells.value);axs[0].set_title('Median household income\n2022 · RM per month')
    fig.colorbar(plt.cm.ScalarMappable(norm=norm,cmap=cmap),ax=axs[0],shrink=.5,label='RM per month',ticks=[0,3000,5000,7000,9000,15000])
    map_panel(axs[1],cells,geometries,['NS']*len(cells),categorical=True)
    xy=cells[['x_m','y_m']].to_numpy()/1000
    for i,j in zip(*np.where(np.triu(A,1))):axs[1].plot(xy[[i,j],0],xy[[i,j],1],color='#9d6b36',alpha=.5,lw=.5)
    axs[1].scatter(xy[:,0],xy[:,1],s=4,c='#6e4928');axs[1].set_title('Symmetric union 4NN graph\n92 areas · one component')
    fig.suptitle('Peninsular Malaysia · income: DOSM · boundaries: PLANMalaysia',fontsize=14);save(fig,'malaysia-income-support.svg')
    fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained');axs[0].scatter(r.z,r.lag_z,c='#b65b13',s=23);axs[0].axhline(0,c='#999999',lw=.6);axs[0].axvline(0,c='#999999',lw=.6);xs=np.array([r.z.min(),r.z.max()]);axs[0].plot(xs,stats['Moran_I']['observed']*xs,c='#6656a6');axs[0].set(xlabel='Standardised district income z',ylabel='Row-standardised lag Wz',title=f"Observed Moran I = {stats['Moran_I']['observed']:.3f}")
    axs[1].hist(sim[:,0],bins=40,color='#d7bb8b',edgecolor='white');axs[1].axvline(stats['Moran_I']['observed'],color='#b65b13',lw=2,label='Observed I');axs[1].set(xlabel="Moran's I",ylabel='Frequency',title='9,999 unrestricted permutations');axs[1].legend();save(fig,'malaysia-income-moran.svg')
    for name,types,title,filename in [('I',r.quadrant,"Local Moran's I",'malaysia-income-local-moran.svg'),('C',r.geary_direction,'Local Geary','malaysia-income-local-geary.svg'),('Gstar',r.gstar_direction,'Conditional Gi*','malaysia-income-local-gstar.svg')]:
        fig,axs=plt.subplots(1,2,figsize=(9,6.3),layout='constrained')
        for ax,col,label in zip(axs,[name+'_p_two',name+'_q_bh'],['Unadjusted p <= 0.05','BH-adjusted q <= 0.05']):
            types_shown=np.where(r[col]<=.05,types,'NS');map_panel(ax,cells,geometries,types_shown,categorical=True);ax.set_title(label)
        labels={'I':['HH','LL','HL','LH'],'C':['Similar','Dissimilar'],'Gstar':['Hot','Cold']}[name]
        handles=[Patch(facecolor=COLOURS[k],label=k) for k in labels]+[Patch(facecolor=COLOURS['NS'],label='Not selected')]
        fig.legend(handles=handles,loc='outside lower center',ncol=len(handles),frameon=False)
        fig.suptitle(title+' · 2022 Malaysian household income\nSame 92 areas and union 4NN graph; fixed-focal permutations',fontsize=14);save(fig,filename)

def main(check=False):
    cells=pd.read_csv(DATA/'observations.csv',dtype={'cell':str});assert len(cells)==92 and cells.cell.is_unique and cells.value.notna().all()
    geometry=json.loads((DATA/'geometry_audit.json').read_text());assert hashlib.sha256((DISPLAY/'hh_income_district.csv').read_bytes()).hexdigest()==geometry['income_sha256']
    income=pd.read_csv(DISPLAY/'hh_income_district.csv')
    income=income[income.date.str.startswith('2022')]
    joined=cells.merge(income,on=['state','district'],how='left',validate='one_to_one')
    assert len(joined)==92 and np.array_equal(joined.value,joined.income_median)
    A=build_graph(cells,4)
    saved_edges=pd.read_csv(DATA/'edges.csv',dtype={'i':str,'j':str})
    expected_pairs={tuple(sorted((cells.cell.iloc[i],cells.cell.iloc[j]))) for i,j in zip(*np.where(np.triu(A,1)))}
    recorded_pairs={tuple(sorted((e.i,e.j))) for e in saved_edges[saved_edges.graph=='union_knn_4'].itertuples()}
    assert expected_pairs==recorded_pairs
    r,stats,sim=analyse(cells,A)
    _,sensitivity,_=analyse(cells,build_graph(cells,6))
    meta={'variable':'2022 median gross monthly household income, nominal RM, by residence','support':'92 matched mapped areas; most administrative districts; Perlis, Kuala Lumpur and Putrajaya each contribute one unit; includes Kecil Lojing. Equal observation weight, not household population weighting.','primary_weights':'Symmetric union of 4 nearest interior representative points, then row-standardise for I/C. Binary graph for General G and Gi*, plus diagonal 1 for Gi*.','sensitivity_weights':'Symmetric union 6NN; all other inputs unchanged.','B':9999,'seed':5230,'local_null':'Hold focal value fixed; sample k distinct other indices without replacement. Shared draws per focal unit across methods.','tails':'Inclusive plus-one tails; local two-sided=min(1,2*min(lower,upper)); equality tolerance 1e-12. Global I/G upper, C lower.','adjustment':'Separate 92-test BH families; exploratory under spatial dependence. Bonferroni comparison also reported.','source_geometry_audit':'geometry_audit.json','primary':stats,'sensitivity':sensitivity}
    if check:
        old=pd.read_csv(DATA/'cell_results.csv',dtype={'cell':str});assert old.cell.tolist()==r.cell.tolist();assert np.allclose(old.select_dtypes('number'),r.select_dtypes('number'),rtol=1e-10,atol=1e-10)
        assert np.array_equal(r.I_p_two,r.Gstar_p_two)
        import itertools
        chain=np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]],float);sample=np.array([2.,2.,8.,8.]);assert np.allclose(global_stats(sample,chain)[:2],[.5,.375]);exact=np.array([global_stats(np.array(p),chain) for p in itertools.permutations(sample)]);assert np.allclose(exact.mean(0)[:2],[-1/3,1]);assert np.allclose(bh([.001,.01,.04,.2]),[.004,.02,.16/3,.2])
        print('Malaysian counts, weights, local/global results, tails and adjustments reproduced.')
    else:
        r.to_csv(DATA/'cell_results.csv',index=False);(DATA/'analysis.json').write_text(json.dumps(meta,indent=2)+'\n');figures(cells,r,stats,sim,A)
    print(json.dumps({'primary':stats,'sensitivity':sensitivity},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');main(p.parse_args().check)
