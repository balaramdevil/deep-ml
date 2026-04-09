import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	b_arr = np.array(B)
	c_arr = np.array(C)
	c_inv = np.linalg.inv(c_arr)
	P = c_inv @ b_arr
	return P