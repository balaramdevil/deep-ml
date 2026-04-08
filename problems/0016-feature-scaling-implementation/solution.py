import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	maxi = np.amax(data,axis=0)
	mini = np.amin(data,axis=0)
	std_dev = np.std(data,axis=0)
	mean = np.mean(data,axis=0)
	standardized_data = np.round((data-mean)/std_dev,decimals=4)
	normalized_data = np.round((data-mini)/(maxi-mini),decimals=4)
	return standardized_data, normalized_data