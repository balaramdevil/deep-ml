import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	term_1 = np.mean(np.square((w @ X.T)-y_true))
	term_2 = np.sum(np.square(w))*alpha
	return term_1 + term_2
