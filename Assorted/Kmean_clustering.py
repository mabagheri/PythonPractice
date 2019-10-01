import numpy as np
from scipy.spatial.distance import cdist


def calculated_dist_centroid(X, centroids, dist_function="euclidean"):
    all_dists = []
    n_centroids = centroids.shape[0]

    for i in range(n_centroids):
        c = centroids[i, :].reshape(1, 100)
        # c_dists = []
        if dist_function == "euclidean":
            # d = np.sum((X-c)**2,axis=1)
            d = cdist(X, c, "euclidean")
            all_dists.append(d)

    all_dists = np.array(all_dists)
    return all_dists


def find_centroids(all_dists):
    n_centroids = all_dists.shape[0]
    centroid_of_each_sample = np.argmin(all_dists, axis=0)

    my_dict = {i: np.where(centroid_of_each_sample == i) for i in range(n_centroids)}
    return my_dict


random_X = np.random.rand(10000, 100)
random_centroids = np.random.rand(5, 100)

all_distances = calculated_dist_centroid(random_X, random_centroids, dist_function="euclidean")
print(all_distances.shape)
