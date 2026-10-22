"""Reproduce four original SVG diagrams from the selected pilot inputs. No network."""
from pathlib import Path
import pandas as pd,numpy as np,json,html,base64,zipfile,io,hashlib
P=Path(__file__).resolve().parent;D=P/'data';F=P/'figures';F.mkdir(exist_ok=True)
a=json.load(open(D/'audit.json'));j=pd.read_csv(D/'od_joined.csv');lookup=pd.read_csv(D/'station_lookup.csv');vol=pd.read_csv(D/'station_activity_selected.csv');order=lookup.station_code.tolist();names=lookup.station_name.tolist();m=j.pivot(index='ORIGIN_PT_CODE',columns='DESTINATION_PT_CODE',values='TOTAL_TRIPS').reindex(index=order,columns=order)
def table(df):return df.to_html(index=False,border=0,classes='dataframe',escape=True)
def svgdoc(w,h,body,title):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}"><style>text{{font-family:Arial,sans-serif;fill:#342a20}}.small{{font-size:14px}}.body{{font-size:17px}}.heading{{font-size:20px;font-weight:bold}}</style><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#9a5b20"/></marker></defs><rect width="100%" height="100%" fill="white"/>'+body+'</svg>'
def text(x,y,s,cls='body',**kw):return '<text x="%s" y="%s" class="%s" %s>%s</text>'%(x,y,cls,' '.join(k.replace('_','-')+'="'+str(v)+'"' for k,v in kw.items()),html.escape(s))
def box(x,y,w,h):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fffaf1" stroke="#d6c4a9"/>'
def line(x,y,x2,y2):return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="#9a5b20" stroke-width="2" marker-end="url(#arrow)"/>'
body=box(20,30,290,200)+box(355,30,290,200)+box(690,30,290,200)
for x,title,lines in [(40,'STATION LOOKUP',['One row per station complex','NS17/CC15 → Bishan','CC16 → Marymount','4 unique station keys']),(375,'OD OBSERVATIONS',['One row per directed pair,','month, day type and hour','Bishan → Marymount: 256','12 rows in the selected slice']),(710,'EXIT LOCATIONS',['One row per station exit','Bishan: 5 exit records','Marymount: 2 exit records','19 exit records for 4 stations'])]:
 body+=text(x,65,title,'heading')
 for k,s in enumerate(lines):body+=text(x,100+30*k,s,'body')
body+=text(20,270,'Repeated station codes in observations or exits are expected. The row meaning determines the key.','body')
(F/'01_row_meaning.svg').write_text(svgdoc(1000,300,body,'Three tables with different row meanings: stations, OD observations and exits'))
body=box(20,25,310,165)+box(380,25,250,165)+box(680,25,310,165)
body+=text(40,58,'LOOK UP THE ORIGIN','heading')+text(40,96,'NS17/CC15 → Bishan')+text(40,128,'many records : one station','small')
body+=text(400,58,'ONE OD RECORD','heading')+text(400,96,'NS17/CC15 → CC16')+text(400,128,'TOTAL_TRIPS = 256')
body+=text(700,58,'LOOK UP THE DESTINATION','heading')+text(700,96,'CC16 → Marymount')+text(700,128,'many records : one station','small')
body+=line(330,107,376,107)+line(680,107,634,107)+box(170,240,670,90)+text(195,274,'Bishan → Marymount | 256 trips','heading')+text(195,305,'The names are added; the observation and its trip count stay unchanged.','small')+line(505,193,505,234)
(F/'02_two_joins.svg').write_text(svgdoc(1010,355,body,'The same station lookup is joined twice to attach origin and destination names'))
body=''
for x,title,pts in [(20,'BISHAN',[(90,150,'Bishan'),(160,245,'Marymount')]),(355,'SERANGOON',[(420,180,'Serangoon')]),(690,'GEYLANG',[(755,180,'Paya Lebar')])]:
 body+=f'<path d="M{x+20},55 L{x+270},40 L{x+300},260 L{x+245},305 L{x},275 Z" fill="#f6ead5" stroke="#ab8855" stroke-width="2"/>'+text(x+35,95,title,'heading')
 for px,py,name in pts:body+=f'<circle cx="{px}" cy="{py}" r="7" fill="#ae5719"/>'+text(px+15,py+5,name)
body+=text(20,350,'SCHEMATIC ONLY — positions and boundaries are illustrative; area labels reflect the actual point-in-polygon results.','small')
(F/'03_spatial_join.svg').write_text(svgdoc(1010,375,body,'Schematic of actual reference-point assignments: Bishan and Marymount in Bishan, Serangoon in Serangoon, Paya Lebar in Geylang'))
# A static, fully labelled matrix is retained even when JavaScript is unavailable.
body=text(250,30,'DESTINATION →','heading')+text(15,135,'ORIGIN ↓','heading')
for k,name in enumerate(names):body+=text(270+k*145,70,name,'body',text_anchor='middle')+text(185,132+k*70,name,'body',text_anchor='end')
mx=float(j.TOTAL_TRIPS.max())
for i in range(4):
 for k in range(4):
  v=m.iloc[i,k];isna=pd.isna(v);alpha=0 if isna else float(v)/mx;col='#eee9e1' if isna else f'rgb({int(255-70*alpha)},{int(239-165*alpha)},{int(209-190*alpha)})'
  body+=f'<rect class="matrixcell" data-value="{str(v)}" x="{200+k*145}" y="{90+i*70}" width="140" height="65" fill="{col}" stroke="white"/>'
  body+=text(270+k*145,132+i*70,'—' if isna else f'{v:,.0f}','body',text_anchor='middle',style='fill:white' if alpha>.65 else 'fill:#342a20')
body+=text(200,405,'Cell values: reported trips, Sep 2026, WEEKDAY, hour category 08. Darker colour = larger count.','small')+text(200,430,'— = no record in this selected slice; retained as missing, not filled with zero.','small')
(F/'04_od_matrix.svg').write_text(svgdoc(1000,455,body,'Four by four directed OD matrix; rows are origins, columns destinations; absent diagonal records remain missing'))

print("Wrote four original SVG diagrams")
