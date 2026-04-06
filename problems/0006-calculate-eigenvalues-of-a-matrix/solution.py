import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	solution = np.linalg.eig(np.array(matrix))
	return solution.eigenvalues.tolist()