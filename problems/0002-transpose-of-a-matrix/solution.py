def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	answer = []
	n = len(a)
	m = len(a[0])
	for i in range(m):
		ans = []
		for j in range(n):
			ans.append(a[j][i])
		answer.append(ans)
	return answer