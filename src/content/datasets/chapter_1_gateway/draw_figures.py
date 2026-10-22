"""Original Chapter 1 illustrations. Python + pandas, numpy, matplotlib. Offline."""
from pathlib import Path
import json
import numpy as np,pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Circle,Rectangle
from matplotlib import font_manager
P=Path(__file__).resolve().parent;F=P.parents[1]/'resources/chapter_1_original';F.mkdir(parents=True,exist_ok=True)
font=P.parents[3]/'_static/css/fonts/ComicNeue-Regular.ttf'
if font.exists():font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']=['Comic Neue','DejaVu Sans']
plt.rcParams.update({'font.size':12,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
def save(fig,name,foot):
 fig.text(.02,.015,foot,fontsize=10,color='#6a5b49');fig.savefig(F/(name+'.png'),dpi=160,bbox_inches='tight');fig.savefig(F/(name+'.svg'),bbox_inches='tight');plt.close(fig)
c='#a85d1d';pale='#efc889';gray='#c5bcac'
# Actual directed counts for one selected pair, reused without implying route, speed or demand explanation.
d=pd.read_csv(P/'data/mrt_pair.csv');assert d.TOTAL_TRIPS.tolist()==[256,50]
fig,axs=plt.subplots(2,2,figsize=(13,8));fig.subplots_adjust(top=.86,bottom=.16,wspace=.68,hspace=.48)
ax=axs[0,0];ax.axis('off');t=ax.table(cellText=[['Bishan','Marymount','256'],['Marymount','Bishan','50']],colLabels=['Origin','Destination','Trips'],loc='center',cellLoc='left');t.auto_set_font_size(False);t.set_fontsize(12);t.scale(1,2);ax.set_title('Table: which records and values?')
ax=axs[0,1];ax.barh([1,0],[256,50],color=[c,pale]);ax.set(yticks=[1,0],yticklabels=['Bishan → Marymount','Marymount → Bishan'],xlabel='Reported trips',xlim=(0,315),title='Chart: how do the counts compare?')
for yy,v in [(1,256),(0,50)]:ax.text(v+5,yy,str(v),va='center')
ax=axs[1,0];ax.set(xlim=(0,1),ylim=(0,1),title='Location sketch: where are the endpoints?');ax.axis('off')
ax.scatter([.2,.75],[.32,.65],c=c,s=90);ax.text(.2,.18,'Marymount',ha='center');ax.text(.75,.78,'Bishan',ha='center');ax.text(.5,.01,'Illustrative layout; no distance scale',ha='center',fontsize=10)
ax=axs[1,1];ax.set(xlim=(0,1),ylim=(0,1),title='Flow diagram: which direction carries more?');ax.axis('off')
for x,name in [(.18,'Bishan'),(.82,'Marymount')]:ax.scatter([x],[.5],c=c,s=110);ax.text(x,.13,name,ha='center')
for xy,xy2,rad,lw,lab,yy in [((.21,.53),(.79,.53),-.3,4,'256',.78),((.79,.46),(.21,.46),-.3,1.3,'50',.20)]:ax.add_patch(FancyArrowPatch(xy,xy2,connectionstyle=f'arc3,rad={rad}',arrowstyle='-|>',mutation_scale=16,lw=lw,color=c));ax.text(.5,yy,lab,ha='center')
fig.suptitle('The same observations can answer different visual questions',fontsize=20)
save(fig,'01_several_views','Real counts: supplied LTA Sep 2026 WEEKDAY, hour category 08; monthly aggregates, not one morning. Sketches are schematic; arrows represent OD relationships, not railway routes.')
# Explicit invented comparison; proportions make the reference quantity visible.
fig,axs=plt.subplots(1,2,figsize=(12,5.5));fig.subplots_adjust(top=.79,bottom=.2,wspace=.35)
axs[0].bar(['Area A','Area B'],[20,10],color=c);axs[0].set(ylabel='Upper-price-group sales',title='First view: A has more selected sales',ylim=(0,25))
for i,v in enumerate([20,10]):axs[0].text(i,v+.5,str(v),ha='center')
axs[1].bar(['Area A','Area B'],[20,50],color=pale);axs[1].set(ylabel='Upper-group share of all sales (%)',title='Second view: B has a larger share',ylim=(0,60))
for i,(v,lab) in enumerate([(20,'20 / 100 = 20%'),(50,'10 / 20 = 50%')]):axs[1].text(i,v+1,lab,ha='center')
fig.suptitle('An observation becomes more informative when we ask “compared with what?”',fontsize=17)
save(fig,'02_denominator','Invented teaching example, not HDB findings. “Upper-price group” uses one common illustrative threshold. Counts and shares answer different questions; neither establishes causation.')
# Four complementary geographical perspectives; all geometry/links/perception cues invented.
fig,axs=plt.subplots(2,2,figsize=(12,8));fig.subplots_adjust(top=.85,bottom=.16,hspace=.35,wspace=.24)
pts=np.array([[.25,.4],[.48,.64],[.76,.38],[.78,.78]])
for ax in axs.flat:
 ax.set(xlim=(-.2,1.1),ylim=(-.15,1),aspect='equal');ax.axis('off');ax.scatter(pts[:,0],pts[:,1],c=gray,s=65)
 ax.scatter([pts[0,0]],[pts[0,1]],s=130,c=c)
axs[0,0].plot([.25,.25],[.08,.4],ls=':',c='#7b7061');axs[0,0].plot([.06,.25],[.4,.4],ls=':',c='#7b7061');axs[0,0].text(.25,.12,'reference location',ha='center',fontsize=10);axs[0,0].set_title('Absolute: where is the place?')
axs[0,1].add_patch(Circle(pts[0],.36,fill=False,ec=c,lw=2));axs[0,1].text(.5,-.1,'nearby under a chosen distance',ha='center',fontsize=10);axs[0,1].set_title('Relative: what is near, and by which measure?')
for idx in [2,3]:axs[1,0].plot(pts[[0,idx],0],pts[[0,idx],1],c=c,lw=2)
axs[1,0].text(.5,-.1,'selected social or movement ties',ha='center',fontsize=10);axs[1,0].set_title('Relational: what is connected?')
axs[1,1].add_patch(Circle(pts[2],.13,fc=pale,alpha=.7,ec=c));axs[1,1].text(.77,.39,'familiar',ha='center',fontsize=10);axs[1,1].text(.5,-.1,'a hypothetical person’s experience',ha='center',fontsize=10);axs[1,1].set_title('Mental: what does the place mean to someone?')
fig.suptitle('One setting, several geographical perspectives',fontsize=20)
save(fig,'03_spatial_perspectives','Original conceptual illustration informed by space–place scholarship. Points, links and familiarity are invented; a point’s size is not a measurement of actual perceptions.')
print('Wrote three original plates, PNG + SVG')
