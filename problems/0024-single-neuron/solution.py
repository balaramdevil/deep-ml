import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	features_array = np.array(features)
	weights_array = np.array(weights)
	prod_1 = weights_array @ features_array.T
	prod_1 = prod_1 + bias
	prod_1 = np.round(1 / (1+np.exp(-1*prod_1)),decimals=4)
	labels = np.array(labels)
	mse = np.mean((prod_1 - labels)**2)
	# Your code here
	return prod_1, mse