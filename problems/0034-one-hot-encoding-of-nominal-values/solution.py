import numpy as np
def to_categorical(x, n_col=None):
	if n_col == None:
		n_col = np.max(x) + 1
	one_hot = np.eye(n_col)[x]
	return one_hot