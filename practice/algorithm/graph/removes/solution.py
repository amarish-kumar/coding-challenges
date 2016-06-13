t, n, b = map(int, raw_input().split())

graph = []
for _ in range(0, n):
	row = map(int, raw_input().split())
	graph.append(row)

def find_sccs(n, graph):
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


def get_reachable_nodes(start, graph):		# get all connected nodes (incl. start)
	pass


def get_edges(nodes):		# get edges for graph component
	pass



# first, remove all edges that do not appear in any of the SCC's
# if under budget: ok, quit
# else,
#  prefer to leave the edges connecting smallest of the SCC's



