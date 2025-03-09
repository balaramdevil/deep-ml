
import numpy as np

def cosine_similarity(v1, v2):
	res = np.dot(v1,v2)
	denom = np.linalg.norm(v1)*np.linalg.norm(v2)
	return np.round(res/denom,decimals=3)
