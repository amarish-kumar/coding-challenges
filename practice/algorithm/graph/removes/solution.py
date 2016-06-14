# !!! incomplete !!!

def find_sccs(n, graph):
	sccs = []
	visit = map(lambda i : i, range(0, n))

	i = 0
	while len(visit) > 0:
		start = visit[0]

		reachable = get_reachable_nodes(start, graph)

		j = 0
		while len(reachable) > 0 and j < len(reachable):
			nr = get_reachable_nodes(reachable[j], graph)
			k = 0
			while len(reachable) > 0:
				if not reachable[k] in nr:
					del reachable[k]
					if k == j:
						j -= 1

			j += 1

		if len(reachable) > 1: 		# we found an SCC
			scc = get_edges(reachable)
			for r in reachable:
				visit.remove(r)
			sccs.append(scc)

	return sccs


def get_reachable_nodes(start, n, graph, r=None):		# get all reachable nodes (incl. start)
	if r is None:
		r = []
	elif start in r:
		return []

	r.append(start)
	dir_reachable = filter(lambda i : graph[start][i] != 0, range(0, n))
	for d in dir_reachable:
		if not d in r:
			get_reachable_nodes(d, n, graph, r)
	return r


def get_edges(nodes, edges=[], visited=[], path=[]):		# get edges for a graph component
	for n in nodes:
		path.append(n)
		visited.append(n)
		reachable = filter(lambda i : i != 0, graph[n])
		for r in reachable:
			if not r in visited:
				if r in nodes:
					edges_to_r = [(path[i], path[i+1]) for i in range(0, len(path) - 1)] + [(path[-1], r)]
					for e in edges_to_r:
						if not e in edges:
							edges.append(e)
				visited.append(r)
				get_edges(nodes, edges, visited, path + [r])
	return edges


def remove(b, graph, sccs):
	uniq_sccs_edges = list(set([e for scc in sccs for e in scc]))
	removed_edges = []

	for i in range(0, n):
		for j in range (0, n):
			if  i != j and not (i, j) in uniq_sccs_edges and graph[i][j] <= b:
				removed_edges.append((i, j))
				b -= graph[i][j]

	return removed_edges				


def read_input():
	t, n, b = map(int, raw_input().split())

	graph = []
	for _ in range(0, n):
		row = map(int, raw_input().split())
		graph.append(row)

	return t, n, b, graph


def main():
	t, n, b, graph = read_input()

	sccs = find_sccs()

	edges = remove(b, graph, sccs)

	print n
	print '\n'.join(['%d %d'%(n1, n2) for n1, n2 in edges])

if __name__ == '__main__':
	main()


# first, remove all edges that do not appear in any of the SCC's
# if under budget: ok, quit
# else,
#  prefer to leave the edges connecting smallest of the SCC's



