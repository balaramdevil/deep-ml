import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	y = y.reshape(m,-1)
	while(iterations>0):
		h = X @ theta
		gradient = (h-y)
		gradient = X.T @ gradient
		theta = theta - alpha*(gradient/m)
		iterations -= 1
	return np.round(theta,decimals=4)