import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	det_t = np.linalg.det(T)
	det_s = np.linalg.det(S)
	if not (det_t and det_s):
		return -1
	t_inv = np.linalg.inv(T)
	transformed_matrix = t_inv @ A @ S
	return transformed_matrix