import numpy as np
import random
import sklearn.metrics.pairwise
import scipy.spatial.distance

r = np.array([random.randrange(1, 1000) for _ in range(0, 1000)])
c = r[:, None]

def option1(r):
    dists = np.abs(r - r[:, None])

def option2(r):  # fastest
    dists = scipy.spatial.distance.pdist(r, 'cityblock')

def option3(r):
    dists = sklearn.metrics.pairwise.manhattan_distances(r)

# option 2 is fastest

# ------------------ Calculate pairwise distances (for example for kmeans (k-means))
from scipy.spatial.distance import cdist
XA = np.random.rand(10000, 1000)
XB = np.random.rand(10, 1000)

# option 1 (best=fastest)
cdist(XA, XB, metric='euclidean')

# option 2
cdist(XA, XB, lambda u, v: np.sqrt(((u-v)**2).sum()))

# option 3 (same as option 2 in terms of speed)
def calc_dist(XA, XB):
    all_dist = []
    for xb in XB:
        all_dist.append(np.sqrt(np.sum((XA - xb)**2, axis=1)))
    return np.array(all_dist)
calc_dist(XA, XB)


