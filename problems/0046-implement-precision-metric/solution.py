import numpy as np
def precision(y_true, y_pred):
	correct = np.sum((y_true == y_pred) & (y_true == 1) & (y_pred == 1))
	predicted = (y_pred == 1).sum()

	return correct / predicted 
