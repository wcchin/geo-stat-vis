"""Reproduce original book diagrams from synthetic data (no external artwork).

Run from the repository root: python scripts/draw_spatial_figures.py
Requires NumPy and Matplotlib. SVG text remains editable.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.colors import BoundaryNorm, ListedColormap

OUT = Path(__file__).resolve().parents[1] / 'src/content/resources/original'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'svg.fonttype': 'none', 'svg.hashsalt': 'ge5230-original'})
BLUE = '#2166ac'
INK = '#223247'

def save(fig, name):
    path = OUT / f'{name}.svg'
    fig.savefig(path, bbox_inches='tight', metadata={'Date': None})
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines()) + '\n')
    plt.close(fig)

values = np.repeat(np.arange(1, 5), 16).reshape(8, 8)
colors = ListedColormap(['#eff3ff', '#bdd7e7', '#6baed6', '#2171b5'])
norm = BoundaryNorm(np.arange(.5, 5), colors.N)
rng = np.random.default_rng(5230)

def grid(ax, data, title):
    ax.imshow(data, cmap=colors, norm=norm, interpolation='nearest')
    ax.set_xticks(np.arange(-.5, 8), minor=True)
    ax.set_yticks(np.arange(-.5, 8), minor=True)
    ax.grid(which='minor', color='white', linewidth=1.5)
    ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    ax.set_title(title, color=INK, pad=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for (y, x), value in np.ndenumerate(data):
        ax.text(x, y, str(value), ha='center', va='center',
                color='white' if value == 4 else INK, fontsize=10)

fig, ax = plt.subplots(figsize=(6, 6))
grid(ax, values, 'A structured arrangement of synthetic values')
fig.text(.5, .02, '64 fixed cells · 16 values in each category (1–4)', ha='center', color=INK)
save(fig, 'spatial-values-structured')

shuffled = rng.permutation(values.ravel()).reshape(values.shape)
assert sorted(shuffled.ravel()) == sorted(values.ravel())
fig, axs = plt.subplots(1, 2, figsize=(11, 5.5))
grid(axs[0], values, 'Before permutation')
grid(axs[1], shuffled, 'One random permutation')
fig.text(.5, .02, 'Same cells and values; only the assignment of values to cells changes.',
         ha='center', color=INK)
save(fig, 'spatial-values-permutation')

fig, axs = plt.subplots(1, 3, figsize=(13, 4.7))
for i, ax in enumerate(axs, 1):
    perm = rng.permutation(values.ravel()).reshape(values.shape)
    assert sorted(perm.ravel()) == sorted(values.ravel())
    grid(ax, perm, f'Permutation {i}')
fig.text(.5, .02, 'Independent reshuffles of the same 64 values; chance can produce local groupings.',
         ha='center', color=INK)
save(fig, 'spatial-values-three-permutations')

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
print('Generated five original SVG figures; permutation and adjacency checks passed.')
