import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
    Y = np.array(y)
    Y = Y.reshape(1,-1)
    Y= Y.T
    sub = X.T @ X
    sub = np.linalg.inv(sub)
    sub2 = X.T @ Y
    theta = sub @ sub2
    theta = np.round(theta,decimals = 4).ravel()
    theta = theta.tolist()
    # theta = np.linalg.inv((X.T) @ (X))@(Y @ X.T)
	return theta