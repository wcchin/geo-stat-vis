
import pandas as pd 
import geopandas as gpd 
from shapely.geometry import Point, Polygon

import numpy as np
from sklearn.neighbors import KernelDensity  # for calculating KDE
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin

from scipy.spatial import Voronoi

from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

from scipy.spatial import ConvexHull

import shapely
#import shapely.geometry
#import shapely.ops



def run_convex_hull(pts_gdf, cluster_id_col):
    pts_gdf = pts_gdf.copy()
    pts_gdf['tmp_x'] = pts_gdf.geometry.x
    pts_gdf['tmp_y'] = pts_gdf.geometry.y
    geoms = []
    ks = []
    for k in sorted(pts_gdf[cluster_id_col].unique()):
        ks.append(k)
        tmp = pts_gdf[pts_gdf[cluster_id_col]==k]
        points = np.array([tmp['tmp_x'], tmp['tmp_y']]).T
        hull = ConvexHull(points)
        hull_vertices = points[hull.vertices]
        hull = Polygon(hull_vertices) 
        #print(hull)
        geoms.append(hull)
    hulls = pd.DataFrame.from_dict({'k': ks, 'geometry': geoms})
    hulls = gpd.GeoDataFrame(hulls, geometry=hulls['geometry'], crs=pts_gdf.crs)
    return hulls


def confidence_ellipse(x, y, n_std=3.0, **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The Axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      **kwargs)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf)
    
    vertices = ellipse.get_verts()     # get the vertices from the ellipse object
    ellipse = Polygon(vertices)        # Turn it into a polygon
    return ellipse


def run_std_ellipse(pts_gdf, cluster_id_col, n_std=3):
    pts_gdf = pts_gdf.copy()
    pts_gdf['tmp_x'] = pts_gdf.geometry.x
    pts_gdf['tmp_y'] = pts_gdf.geometry.y
    geoms = []
    ks = []
    for k in sorted(pts_gdf[cluster_id_col].unique()):
        ks.append(k)
        tmp = pts_gdf[pts_gdf[cluster_id_col]==k]
        xs = np.array(tmp['tmp_x'].tolist()).T
        ys = np.array(tmp['tmp_y'].tolist()).T
        elp = confidence_ellipse(xs, ys, n_std=n_std)
        geoms.append(elp)
    elps = pd.DataFrame.from_dict({'k': ks, 'geometry': geoms})
    elps = gpd.GeoDataFrame(elps, geometry=elps['geometry'], crs=pts_gdf.crs)
    return elps


    
def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.

    """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()*2

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all([v >= 0 for v in vertices]):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    return new_regions, np.asarray(new_vertices)


def run_voronoi(centers_gdf,  # the center points gdf
                x0, y0, x1, y1  # the total_bounds for cutting the polygons
               ): 
    points = np.array([centers_gdf.geometry.x, centers_gdf.geometry.y]).T 
    vor = Voronoi(points)
    regions, vertices = voronoi_finite_polygons_2d(vor)

    polys = []
    for a, region in enumerate(regions):
        polygon = vertices[region]
        polygon = Polygon(polygon)
        polygon = shapely.clip_by_rect(polygon, x0, y0, x1, y1)
        polys.append(polygon)
        #break
    polys = pd.DataFrame.from_dict({
        'k': list(range(len(polys))), 
        'geometry': polys, 
    })
    vor_gdf = gpd.GeoDataFrame(polys, geometry=polys['geometry'], crs=centers_gdf.crs)
    return vor_gdf


def run_kmeans(this_gdf, n_clusters):
    Xb = np.array([this_gdf.geometry.x, this_gdf.geometry.y]).T
    k_means = KMeans(init="k-means++", n_clusters=n_clusters, n_init=10)
    k_means.fit(Xb)
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels = pairwise_distances_argmin(Xb, k_means_cluster_centers)
    centers = pd.DataFrame(k_means_cluster_centers, columns=['x', 'y'])
    centers['k'] = list(range(len(k_means_cluster_centers)))
    centers = centers[['k', 'x', 'y']]
    centers = gpd.GeoDataFrame(centers, 
                               geometry=[Point(x, y) for i, (x, y) in centers[['x', 'y']].iterrows()], 
                               crs=this_gdf.crs)
    return k_means_labels, centers


def run_kde(this_gdf, grid_data, bandwidth=400):
    xs = this_gdf.geometry.x
    ys = this_gdf.geometry.y
    this_xys = np.array([xs, ys]).T
    #print(this_xys)
    this_kde = KernelDensity(kernel='exponential', bandwidth=bandwidth).fit(this_xys)
    zs = np.exp(this_kde.score_samples(grid_data))
    return zs
    