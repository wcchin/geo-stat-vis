"""Explicit shared areal statistics. Local population moments and conditional tails.
Nonnegative attributes, binary symmetric graph, row-standardised I/C.
"""
import numpy as np
B=9999
SEED=5230
def bh(p):
    p=np.asarray(p);order=np.argsort(p);rank=np.arange(1,len(p)+1)
    q=np.minimum.accumulate((p[order]*len(p)/rank)[::-1])[::-1]
    out=np.empty(len(p));out[order]=np.minimum(q,1);return out

def tails(observed,simulated):
    ties=np.isclose(simulated,observed,rtol=1e-12,atol=1e-12)
    lo=(1+np.count_nonzero((simulated<observed)|ties,axis=0))/(len(simulated)+1)
    hi=(1+np.count_nonzero((simulated>observed)|ties,axis=0))/(len(simulated)+1)
    return lo,hi,np.minimum(1,2*np.minimum(lo,hi))

def global_stats(x,A):
    W=A/A.sum(1)[:,None];n=len(x);d=x-x.mean();Q=d@d;S=W.sum()
    I=n/S*(d@(W@d))/Q
    C=(n-1)/(2*S)*np.sum(W*(x[:,None]-x[None,:])**2)/Q
    G=np.sum(A*x[:,None]*x[None,:])/(x.sum()**2-x@x)
    return np.array([I,C,G])

def analyse(cells,A,B=B,seed=SEED):
    n=len(cells);x=cells['value'].to_numpy(float);d=x-x.mean();m2=np.mean(d*d);z=d/np.sqrt(m2)
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
    stats.update(n=n,value_sum=float(x.sum()),mean=float(x.mean()),B=B,seed=seed,components=int(components),isolates=0,undirected_edges=int(A.sum()/2),min_neighbours=int(A.sum(1).min()),max_neighbours=int(A.sum(1).max()),local={name:{'unadjusted_005':int((result[name+'_p_two']<=.05).sum()),'BH_005':int((result[name+'_q_bh']<=.05).sum()),'Bonferroni_005':int((result[name+'_p_two']<=.05/n).sum())} for name in ['I','C','Gstar']})
    return result,stats,global_sim
