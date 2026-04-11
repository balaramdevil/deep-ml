def distance(point_a,point_b):
	dist = 0
	for j in range(len(point_a)):
		dist += ((point_a[j]-point_b[j])**2)
	return dist
def min_square_points(point,centroids):
	dist = [distance(x,point) for x in centroids]
	return dist.index(min(dist))

def mean_centroid(points):
	return tuple([sum(j)/len(points) for j in zip(*points)])

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	final_centroids = []
	for i in range(max_iterations):
		centroids_list = [[] for i in range(k)]
		new_centroids = []
		for p in points:
			id = min_square_points(p,initial_centroids)
			centroids_list[id].append(p)
		for l in centroids_list:
			new_centroids.append(mean_centroid(l))
		final_centroids = new_centroids
	return final_centroids