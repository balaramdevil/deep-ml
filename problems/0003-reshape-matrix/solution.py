import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a = np.array(a)
	jj = a.shape
	# old_elem = jj[0]*jj[1]
	# print(old_elem)
	# new_elem = new_shape[0]*new_shape[1]
	# print(new_elem)
	if((jj[0]*jj[1]) != (new_shape[0]*new_shape[1])):
		return []
	return a.reshape(new_shape).tolist()