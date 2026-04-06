import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros_like(b)
	D = np.diag(A)
	D_sq = np.diag(D)
	A_new = A-D_sq
	for j in range(n):
		summation = A_new @ x
		first_term = b - summation
		x = first_term/D
	return x