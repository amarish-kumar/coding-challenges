def detect_disjoint_graph(nodes, graph, n, start=None, visited=None):
	if visited is None:
		visited = []
	if start is None:
		start = nodes[0]
		visited.append(start)

	reachable = filter(lambda i : graph[start][i] != 0 and i in nodes, range(0, n))

	for r in reachable:
		if not r in visited:
			visited.append(r)
			detect_disjoint_graph(nodes, graph, n, r, visited)

	return sorted(visited)


def get_all_disjoint_graphs(graph, n):
	graphs = []

	nodes = map(lambda i : i, range(0, n))

	while len(nodes) > 0:
		g = detect_disjoint_graph(nodes, graph, n)
		graphs.append(g)
		map(lambda i : nodes.remove(i), g)

	return graphs


def make_graph_from_edges(n, roads):
	road_graph = map(lambda _ : [0] * n, range(0, n))

	for r in roads:
		road_graph[r[0] - 1][r[1] - 1] = 1

	return road_graph


def main():
	n, m = map(int, raw_input().split())
	roads = map(lambda _ : map(int, raw_input().split()), range(0, m))

	road_graph = make_graph_from_edges(n, roads)
	graphs = get_all_disjoint_graphs(road_graph, n)

	design_score = 0

	for g in graphs:
		l = len(g)
		design_score += l if l >= 3 else 0

	print design_score


if __name__ == '__main__':
	main()


# notes:
# approach:
#  discarding the assumption that there is at least one path between all pairs of train stations
#  (may be a mistake by problem setter?)
#  1. get all the disjoint graphs
#  2. for each such graph, if its length >= 3 (so that at least 2 different paths are possible for each train station), 
#   all stations are reachable within this graph with at least 2 diff paths, so add graph length to design score
#
# score: 22 (failures: errors, timeouts, exceptions) for condition: length >= 3 in step 2 above
# score: 22 (same failures) for condition: length >= 2 (assuming a different interpretation of the problem wherein one path with length of at least 2 is
#  possible for each station)

