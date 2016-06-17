# !!! incomplete !!!

def find_sccs(n, graph):
	sccs = []
	visit = map(lambda i : i, range(0, n))

	while len(visit) > 1:
		start = visit[0]

		reachable = get_reachable_nodes(start, n, graph)
		#print 'reachable:', reachable

		j = 1
		while len(reachable) > 1 and j < len(reachable):
			nr = get_reachable_nodes(reachable[j], n, graph)
			#print 'nr:', nr
			k = len(reachable) - len(nr)
			if k > 0:
				map(reachable.remove, nr)

			j += 1 if k == 0 else 0

		if len(reachable) > 1: 		# we found an SCC
			print 'found scc:', reachable
			scc = get_edges(reachable, n, graph)
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
	return sorted(r)


def get_edges(nodes, n, graph):		# get edges for an scc
	edges = []
	for nd in nodes:
		edges += [(nd, nd2) for nd2 in filter(lambda i : graph[nd][i] != 0 and i in nodes, range(0, n))]
	return edges


def remove(b, n, graph, sccs):
	uniq_sccs_edges = list(set([e for scc in sccs for e in scc]))
	removed_edges = []

	for i in range(0, n):
		for j in range (0, n):
			if  i != j and (not (i, j) in uniq_sccs_edges) and (0 < graph[i][j] <= b):
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

	sccs = find_sccs(n, graph)

	edges = remove(b, n, graph, sccs)

	print len(edges)
	print '\n'.join(['%d %d'%(n1, n2) for n1, n2 in edges])


if __name__ == '__main__':
	main()


# unit tests pass
# but it is not a solution

# next
# find all possible scc combos (so that max. no. of nodes are covered)
# prefer to get the combo with max. no. of sccs (or min. size / scc) so as to maximize score

# e.g.
# [0 1 2 3 4]
# [0 1] [2 3] [4]
# [1] [2] [3] [4] [5] - preferred

# note: edges with len 0 can also be present

