# unused / untested / removed code

def paths_exist(start, graph, n, paths=0, end=None):
	reachable = filter(lambda i : graph[start][i] != 0, range(0, n))
	if end is None:
		end = start

	for r in reachable:
		if r == end:
			paths += 1
			if paths == 2:
				return True, 2
			continue

		s, p = paths_exist(r, graph, n, paths, end)
		if s and p == 2:
			return True, 2
		

	return False, 0

