"""Reproduce the original hypothetical Moran figures and verify their calculations.

Run with --write to regenerate the SVGs. Default: verify the worked example only.
The values are pedagogical, not observed Indonesian fire data.
"""
from pathlib import Path
import argparse
import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parents[1]/'src/content/resources/original'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'svg.fonttype':'path','svg.hashsalt':'morans-four-cell'})
A=np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]],float)
W=A/A.sum(1)[:,None]
x=np.array([2,2,8,8.]); d=x-x.mean(); z=d/d.std(); lag=W@z
def moran(v,w=W):
    a=v-v.mean();return len(v)/w.sum()*(a@w@a)/(a@a)
assignments=np.array(sorted(set(itertools.permutations(x))))
ivals=np.array([moran(v) for v in assignments])
assert np.isclose(moran(x),.5)
assert np.isclose(moran(np.array([2,8,2,8.])), -1)
assert np.isclose(ivals.mean(),-1/3)
assert sum(ivals>=.5-1e-12)==2

assert np.isclose(moran(x,A),1/3)
assert np.isclose((z @ lag)/(z @ z),moran(x))
assert np.isclose(np.mean(ivals >= moran(x)-1e-12),1/3)
for v in assignments:
    assert np.array_equal(np.sort(v),np.sort(x))
    assert np.isclose(moran(v),moran(v+100))
    assert np.isclose(moran(v),moran(v*10))
assert np.isclose((19+1)/(999+1),.020)

def draw_figures():
    OUT.mkdir(parents=True,exist_ok=True)
    fig,axes=plt.subplots(2,1,figsize=(7.1,2.5))
    for ax,v,title in zip(axes,[x,np.array([2,8,2,8])],['Similar neighbours: I = 0.50','Alternating neighbours: I = -1.00']):
        for i in range(3): ax.plot([i,i+1],[0,0],color='#777777',zorder=0)
        for i,value in enumerate(v):
            ax.scatter(i,0,s=700,color=plt.cm.OrRd(.25 if value==2 else .8),edgecolors='#343434')
            ax.text(i,0,str(int(value)),ha='center',va='center',color='black' if value==2 else 'white',weight='bold')
            ax.text(i,-.75,'ABCD'[i],ha='center',fontsize=9)
        ax.text(-.6,.65,title,fontsize=11,weight='bold');ax.set(xlim=(-.7,3.6),ylim=(-1.1,1));ax.axis('off')
    fig.tight_layout();fig.savefig(OUT/'morans-chain.svg',bbox_inches='tight',metadata={'Date':None});plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,3.05))
    ax.axhline(0,color='#888',lw=.8);ax.axvline(0,color='#888',lw=.8)
    ax.plot([-1.5,1.5],[-.75,.75],color='#bd4b08',label='Slope = 0.50')
    ax.scatter(z,lag,s=45,color='#9c3209',zorder=3)
    for a,b,n in zip(z,lag,'ABCD'):ax.annotate(n,(a,b),xytext=(6,6),textcoords='offset points')
    for a,b,t in [(-1.35,1.1,'LH'),(1.1,1.1,'HH'),(-1.35,-1.1,'LL'),(1.1,-1.1,'HL')]:ax.text(a,b,t,color='#777')
    ax.set(xlim=(-1.6,1.6),ylim=(-1.4,1.4),xlabel='Cell value, standardised (z)',ylabel='Neighbour average (Wz)')
    ax.legend(frameon=False,loc='upper center');fig.tight_layout();fig.savefig(OUT/'morans-scatter.svg',metadata={'Date':None});plt.close(fig)
    fig,ax=plt.subplots(figsize=(6.6,2.6))
    u,c=np.unique(ivals,return_counts=True)
    ax.bar(u,c,width=.14,color='#f9b47b',edgecolor='#744126')
    ax.axvline(.5,color='#a13206',lw=2,label='Observed I = 0.50')
    ax.axvline(-1/3,color='#555',ls='--',label='Null expectation = -1/3')
    ax.set(xlabel="Moran's I",ylabel='Distinct assignments',ylim=(0,3),xticks=[-1,-.5,0,.5]);ax.legend(frameon=False,fontsize=8)
    fig.tight_layout();fig.savefig(OUT/'morans-exact-permutations.svg',metadata={'Date':None});plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    if args.write:draw_figures()
    print('Moran four-cell checks passed: I=0.5, binary I=1/3, alternating I=-1; exact right-tail p=1/3; expected I=-1/3.')
