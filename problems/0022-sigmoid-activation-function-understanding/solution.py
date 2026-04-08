import math

def sigmoid(z: float) -> float:
	denom = 1 + math.exp(-1*z)
	result = 1/denom
	return result