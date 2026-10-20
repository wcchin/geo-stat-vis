"""Reproduce course artwork: Milwaukee Census data and synthetic rook diagrams.

Run from the repository root: python scripts/draw_spatial_figures.py
Requires NumPy and Matplotlib. See docs/milwaukee-map-source.md for data provenance.
"""
from pathlib import Path
import argparse
import hashlib
import io
import json
import tempfile
import urllib.request
import zipfile
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib import font_manager
from matplotlib.collections import PatchCollection
from matplotlib.patches import Patch
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

OUT = Path(__file__).resolve().parents[1] / 'src/content/resources/original'
OUT.mkdir(parents=True, exist_ok=True)
# xkcd styling with a bundled, openly licensed handwriting font.
plt.xkcd(scale=0.5, length=100, randomness=1)
font_manager.fontManager.addfont(Path(__file__).resolve().parents[1] / '_static/css/fonts/ComicNeue-Regular.ttf')
plt.rcParams.update({'font.family': 'Comic Neue', 'font.size': 12,
                     'svg.fonttype': 'path', 'svg.hashsalt': 'ge5230-original'})
# Stabilize sketch rendering independently of the data permutation generator.
np.random.seed(5230)
BLUE = '#2166ac'
INK = '#223247'

def save(fig, name):
    path = OUT / f'{name}.svg'
    fig.savefig(path, bbox_inches='tight', metadata={'Date': None})
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines()) + '\n')
    plt.close(fig)

# Keep upstream data outside git; verify the precise source archive before use.
SOURCE_URL = 'https://geodacenter.github.io/data-and-lab/data/MilwaukeeMSA.zip'
SOURCE_SHA256 = 'bf3c9617c872db26ea56f20e82a449f18bb04d8fb76a653a2d3842d465bc122c'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--data-archive', type=Path,
                    default=Path(tempfile.gettempdir()) / 'ge5230-data/MilwaukeeMSA.zip')
archive = parser.parse_args().data_archive
if not archive.exists():
    archive.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(SOURCE_URL, timeout=60) as response:
        payload = response.read()
    if hashlib.sha256(payload).hexdigest() != SOURCE_SHA256:
        raise ValueError('Upstream data changed; review before updating the checksum.')
    archive.write_bytes(payload)
payload = archive.read_bytes()
assert hashlib.sha256(payload).hexdigest() == SOURCE_SHA256
with zipfile.ZipFile(io.BytesIO(payload)) as source:
    data = json.loads(source.read('MilwaukeeMSA/wi_final_census2_random4.geojson'))
features = data['features']
assert len(features) == 417
assert {f['properties']['MSA'] for f in features} == {'Milwaukee'}
assert len({f['properties']['FIPS'] for f in features}) == 417
values = np.array([f['properties']['HH_INC'] for f in features], dtype=float)
valid = np.isfinite(values) & (values > 0)
assert valid.sum() == 413
colors = ListedColormap(['#eff3ff', '#bdd7e7', '#6baed6', '#3182bd', '#08519c'])
breaks = np.array([0, 25000, 40000, 55000, 75000, 200000])
norm = BoundaryNorm(breaks, colors.N)
rng = np.random.default_rng(5230)

# Coordinates are longitude/latitude; use a local equirectangular display.
# Preserve every polygon vertex and hole. No distances are analysed here.
lat0 = 43.1
def project(ring):
    a = np.asarray(ring)
    return np.column_stack(((a[:, 0] + 88) * np.cos(np.deg2rad(lat0)), a[:, 1] - lat0))

def ring_area(a):
    return np.sum(a[:-1,0]*a[1:,1] - a[1:,0]*a[:-1,1]) / 2

patches, owners = [], []
for i, feature in enumerate(features):
    assert feature['geometry']['type'] == 'MultiPolygon'
    for polygon in feature['geometry']['coordinates']:
        vertices, codes = [], []
        for k, ring in enumerate(polygon):
            a = project(ring)
            # Opposite winding for outer/inner rings preserves holes.
            if (ring_area(a) > 0) != (k == 0):
                a = a[::-1]
            vertices.extend(a)
            codes.extend([MplPath.MOVETO] + [MplPath.LINETO]*(len(a)-2) + [MplPath.CLOSEPOLY])
        patches.append(PathPatch(MplPath(vertices, codes)))
        owners.append(i)
all_vertices = np.concatenate([p.get_path().vertices for p in patches])
lo, hi = all_vertices.min(axis=0), all_vertices.max(axis=0)

def shuffle():
    result = values.copy()
    result[valid] = rng.permutation(values[valid])
    assert np.array_equal(np.sort(result[valid]), np.sort(values[valid]))
    assert np.array_equal(result[~valid], values[~valid])
    return result

def map_panel(ax, data, title):
    facecolors = [colors(norm(data[i])) if valid[i] else '#d9d9d9' for i in owners]
    collection = PatchCollection(patches, facecolors=facecolors, edgecolors='#444444',
                                 linewidths=0.22, rasterized=True)
    # Keep real geographic boundaries exact; sketch the diagram annotations.
    collection.set_sketch_params(None)
    collection.set_path_effects([])
    ax.add_collection(collection)
    ax.set_xlim(lo[0]-.015, hi[0]+.015)
    ax.set_ylim(lo[1]-.015, hi[1]+.015)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, color=INK, fontsize=16, pad=12)
    ax.text(.97,.94,'N',transform=ax.transAxes,ha='center',fontsize=12)
    ax.annotate('',xy=(.97,.92),xytext=(.97,.84),xycoords='axes fraction',
                arrowprops={'arrowstyle':'->','color':INK,'lw':1.2})

labels = ['< $25,000', '$25,000–39,999', '$40,000–54,999', '$55,000–74,999', '$75,000+']
def finish_map(fig, name):
    handles = [Patch(facecolor=c, edgecolor='#444444', label=l) for c,l in zip(colors.colors, labels)]
    handles.append(Patch(facecolor='#d9d9d9', label='Unavailable (4 tracts)'))
    fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.075),ncol=3,
               frameon=False,fontsize=10,title='Median household income in 1999 (USD)')
    fig.text(.5,.025,'Source: US Census 2000, Summary File 3 · GeoDa Milwaukee sample data',
             ha='center',fontsize=10,color=INK)
    fig.subplots_adjust(bottom=.26, top=.88, wspace=.06)
    fig.set_dpi(150)
    save(fig,name)

fig, ax = plt.subplots(figsize=(8,8))
map_panel(ax,values,'Milwaukee metropolitan area: observed income')
finish_map(fig,'milwaukee-income-observed')
fig, axs = plt.subplots(1,2,figsize=(12,7.5))
map_panel(axs[0],values,'Observed values')
map_panel(axs[1],shuffle(),'One random permutation')
finish_map(fig,'milwaukee-income-permutation')
fig, axs = plt.subplots(1,3,figsize=(15,7.5))
for i, ax in enumerate(axs,1):
    map_panel(ax,shuffle(),f'Permutation {i}')
finish_map(fig,'milwaukee-income-three-permutations')

# A planar subdivision whose shared-edge adjacency matches the chapter matrix.
polygons = {
    1: [(0,0), (6,0), (3,1), (1,1)],
    2: [(6,0), (0,6), (1,3), (3,1)],
    3: [(-2,0), (0,0), (0,6), (-2,6)],
    4: [(1,1), (3,1), (1,3)],
    5: [(0,6), (0,0), (1,1), (1,3)],
    6: [(-4,0), (-2,0), (-2,6), (-4,6)],
}
positions = {1:(2.7,.4), 2:(2.7,2.7), 3:(-1,3), 4:(1.8,1.9), 5:(.4,2.7), 6:(-3,3)}
edges = [(1,2),(1,4),(1,5),(2,4),(2,5),(3,5),(3,6),(4,5)]
W = np.array([[0,1,0,1,1,0], [1,0,0,1,1,0], [0,0,0,0,1,1],
              [1,1,0,0,1,0], [1,1,1,1,0,0], [0,0,1,0,0,0]])

def shared_edge(a, b):
    # All shared edges in this construction are identical vertex pairs.
    def segments(p):
        return {frozenset((p[i], p[(i+1) % len(p)])) for i in range(len(p))}
    return bool(segments(a) & segments(b))

for i in range(1, 7):
    for j in range(1, 7):
        assert (i != j and shared_edge(polygons[i], polygons[j])) == bool(W[i-1,j-1])
assert {(i+1,j+1) for i,j in zip(*np.where(np.triu(W, 1)))} == set(edges)

def base(ax):
    ax.set_aspect('equal')
    ax.set_xlim(-4.5, 6.5)
    ax.set_ylim(-.6, 6.6)
    ax.axis('off')

fig, ax = plt.subplots(figsize=(9, 6))
for i, points in polygons.items():
    ax.add_patch(Polygon(points, facecolor='#e8f0f7', edgecolor=INK, linewidth=2))
    ax.text(*positions[i], str(i), ha='center', va='center', weight='bold', fontsize=17, color=INK)
base(ax)
ax.set_title('Six synthetic spatial units', color=INK)
fig.text(.5,.02,'Rook neighbours share an edge of non-zero length.', ha='center', color=INK)
save(fig, 'rook-polygons')

fig, ax = plt.subplots(figsize=(9, 6))
for points in polygons.values():
    ax.add_patch(Polygon(points, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1))
for i, j in edges:
    x1,y1 = positions[i]
    x2,y2 = positions[j]
    ax.plot([x1,x2],[y1,y2], color=BLUE, linewidth=2.5, zorder=2)
for i, (x,y) in positions.items():
    ax.scatter(x,y,s=650,color='white',edgecolor=BLUE,linewidth=2.5,zorder=3)
    ax.text(x,y,str(i),ha='center',va='center',fontsize=14,weight='bold',color=INK,zorder=4)
base(ax)
ax.set_title('The same units represented as a neighbour graph',color=INK)
fig.text(.5,.02,'One node per unit · One undirected link per shared edge',ha='center',color=INK)
save(fig, 'rook-neighbour-graph')
print('Generated five SVG figures: 417 Milwaukee tracts, 413 permuted incomes; adjacency checks passed.')
