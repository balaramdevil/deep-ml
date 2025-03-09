def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	answer = []
	for j in a:
		if(len(j)!=len(b)):
			return -1
		else:
			ans = sum([i[0]*i[1] for i in zip(j,b)])
			answer.append(ans)
	return answer