import numpy as np

def shuffle_data(X, y, seed=None):
	rng = np.random.seed(seed)
	perm = np.random.permutation(y.shape[0])
	X[:] = X[perm]
	y[:] = y[perm]
	return X , y