
from shapely.geometry import Polygon, Point
import pandas as pd 
import geopandas as gpd 

from tqdm import tqdm



def gen_polygon(llx, lly, w, h):
    poly = Polygon([(llx, lly), 
                    (llx, lly+h), 
                    (llx+w, lly+h), 
                    (llx+w, lly), 
                    (llx, lly)
                ])
    return poly

def gen_grid(llx, lly, urx, ury, ncol=5, nrow=5, force_square=True, crs=None):
    total_w = urx - llx 
    total_h = ury - lly 

    spacing_w = total_w / ncol
    spacing_h = total_h / nrow

    if force_square:
        if spacing_w <= spacing_h:  # height > width, expand xs
            spacing_dif = spacing_h - spacing_w
            total_dif = spacing_dif * ncol
            #dif = total_h - total_w
            half_dif = total_dif / 2
            llx = llx - half_dif
            urx = urx + half_dif
        else:  # width > height, expand ys
            spacing_dif = spacing_w - spacing_h
            total_dif = spacing_dif * nrow
            half_dif = total_dif / 2
            lly = lly - half_dif
            ury = ury + half_dif
    
    length_w = urx - llx
    length_h = ury - lly
    spacing_w = length_w / ncol
    spacing_h = length_h / nrow

    polys = []
    box_id = []
    row_id = []
    col_id = []
    pbar = tqdm(total=nrow * ncol)
    for i in range(nrow):
        y0 = lly + (i * spacing_h)
        for j in range(ncol):
            x0 = llx + (j * spacing_w)
            this_poly = gen_polygon(x0, y0, spacing_w, spacing_h)
            polys.append(this_poly)
            row_id.append(i)
            col_id.append(j)
            box_id.append(i*ncol+j)
            pbar.update(1)
    pbar.close()
    tmp = pd.DataFrame.from_dict({
        'box_id': box_id, 
        'col_id': col_id, 
        'row_id': row_id, 
    })
    grid_gdf = gpd.GeoDataFrame(tmp, geometry=polys, crs=crs)
    return grid_gdf
