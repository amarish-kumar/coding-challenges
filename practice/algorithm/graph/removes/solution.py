def remove(b, sorted_edge_list):
	removed_edges = []
	i = 0
	while b > 0 and i < len(sorted_edge_list):
		e = sorted_edge_list[i]
		removed_edges.append((e[0], e[1]))
		b -= e[2]
		i += 1

	return removed_edges


def sort_edges_by_cost(n, graph):
	edge_list = []
	for i in range(0, n):
		for j in range(0, n):
			if i != j:
				edge_list.append((i, j, graph[i][j]))

	return sorted(edge_list, key=lambda i : i[2])


def read_input():
	t, n, b = map(int, raw_input().split())

	graph = []
	for _ in range(0, n):
		row = map(int, raw_input().split())
		graph.append(row)

	return t, n, b, graph


def main():
	t, n, b, graph = read_input()

	removed_edges = remove(b, sort_edges_by_cost(n, graph))

	print len(removed_edges)
	print '\n'.join(['%d %d'%(n1, n2) for n1, n2 in removed_edges])


if __name__ == '__main__':
	main()

