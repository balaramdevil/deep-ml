import numpy as np

def accuracy_score(y_true, y_pred):
	total_val = y_true.shape[0]
	correct = (y_true == y_pred).sum()
	return correct/total_val
	pass