"""Run the Peninsula self-study notebook offline and check its teaching examples.

python scripts/check_autocorrelation_pilot.py
Add --write-figures to regenerate the four chapter illustrations.
"""
import argparse
import json
from pathlib import Path
import shutil
import tempfile
import os
import numpy as np
import nbformat
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--write-figures', action='store_true')
args = parser.parse_args()
book = nbformat.read(root/'src/content/notebooks/lab-08-autocorrelation-self-study.ipynb', as_version=4)
nbformat.validate(book)
expected = {'KOTA BHARU':4330,'KUALA TERENGGANU':5872,'TIMOR LAUT':6714,'JOHOR BAHRU':8232,
            'SABAK BERNAM':5533,'SEPANG':12608,'KUALA LUMPUR':10234}
ns = {'BOOK_DATA_DIR': root/'src/content/datasets/peninsula_income_2022',
      'BOOK_FONT_PATH': root/'_static/css/fonts/ComicNeue-Regular.ttf'}
original_show = plt.show
plt.show = lambda *a, **k: plt.close('all')
original_cwd = Path.cwd()
out = root/'src/content/resources/original'
try:
    with tempfile.TemporaryDirectory(prefix='peninsula-book-check-') as temp:
        os.chdir(temp)
        for cell in book.cells:
            if cell.cell_type == 'code':
                ns['display'] = lambda *a, **k: None
                exec(compile(cell.source, 'autocorrelation-notebook', 'exec'), ns)
        assert ns['data_route'].startswith('book snapshot')
        assert len(ns['df']) == 92 and ns['df']['kod_daerah'].is_unique
        assert all(dict(zip(ns['df']['daerah'],ns['values']))[area] == value for area,value in expected.items())
        assert ns['CMAP'] == 'OrRd' and list(ns['breaks']) == [0,3000,5000,7000,9000,15000]
        assert ns['layer']['spatialReference']['wkid'] == 3375
        assert len(ns['permutations']) == 4
        # Verify the values in the chapter's source table, not only the notebook.
        chapter = (root/'src/content/chapter_6/sec_06-01-Spatial-Autocorrelation.md').read_text()
        for value in expected.values():
            assert f'{value:,}' in chapter
        if args.write_figures:
            out.mkdir(parents=True, exist_ok=True)
            for suffix, target in [('01_observed','peninsula-income-observed'),
                                   ('02_observed_vs_permuted','peninsula-income-permutation'),
                                   ('03_three_permutations','peninsula-income-three-permutations')]:
                shutil.copyfile(Path('peninsula_figures')/f'2022_income_median_{suffix}.png', out/f'{target}.png')
        processing = next(c.source for c in book.cells if c.cell_type == 'code' and c.source.startswith('if VARIABLE not in'))
        ns['VARIABLE'] = 'income_mean'
        exec(processing, ns)
        assert len(ns['values']) == 92 and np.all(ns['values'] > 0)
        ns['YEAR'] = 2024
        try:
            exec(processing, ns)
        except ValueError as exc:
            assert 'Missing 2024 income' in str(exc)
        else:
            raise AssertionError('An incomplete year must not be silently plotted.')
finally:
    os.chdir(original_cwd)
    plt.show = original_show

if args.write_figures:
    font_manager.fontManager.addfont(root/'_static/css/fonts/ComicNeue-Regular.ttf')
    with plt.rc_context():
        plt.xkcd(scale=.5, length=100, randomness=1)
        plt.rcParams.update({'font.family':'Comic Neue','svg.fonttype':'path','svg.hashsalt':'ge5230-patterns'})
        np.random.seed(5230)
        grouped = np.tile([0,0,0,1,1,1], (6,1))
        alternating = np.indices((6,6)).sum(axis=0) % 2
        shuffled = np.random.default_rng(5230).permutation(grouped.ravel()).reshape(6,6)
        for a in [grouped,alternating,shuffled]:
            assert np.array_equal(np.sort(a.ravel()),np.sort(grouped.ravel()))
        from matplotlib.colors import ListedColormap
        fig,axs = plt.subplots(1,3,figsize=(12,4.5))
        for ax,a,title in zip(axs,[grouped,shuffled,alternating],['Similar neighbours','One random assignment','Dissimilar neighbours']):
            ax.imshow(a,cmap=ListedColormap(['#fee8c8','#b30000']),vmin=0,vmax=1)
            ax.set_xticks(np.arange(-.5,6), minor=True);ax.set_yticks(np.arange(-.5,6), minor=True)
            ax.grid(which='minor',color='white',linewidth=1.5)
            ax.tick_params(which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
            ax.set_title(title,fontsize=14)
            for spine in ax.spines.values():spine.set_visible(False)
        fig.text(.5,.03,'Synthetic values: pale = low; dark = high. Each panel has 18 of each.',ha='center',fontsize=12)
        fig.subplots_adjust(bottom=.16,wspace=.16)
        path = out/'autocorrelation-patterns.svg'
        fig.savefig(path,bbox_inches='tight',metadata={'Date':None})
        path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
        plt.close(fig)
print('Offline peninsula notebook, source table, permutations, chain arithmetic and incomplete-year checks passed.')
