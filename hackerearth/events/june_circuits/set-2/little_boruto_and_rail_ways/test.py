from unittest import TestCase, main as ut_main

import solution as sol


class TestSolution(TestCase):

	def test_detect_disjoint_graph(self):
		n = 3
		edges = [[1, 2], [2, 3]]

		graph, nodes = self.make_graph_and_node_list(n, edges)
		self.assertEqual(self.start1(sol.detect_disjoint_graph(nodes, graph, n)), [1, 2, 3])


	def make_graph_and_node_list(self, n, edges):
		graph = sol.make_graph_from_edges(n, edges)
		nodes = map(lambda i : i, range(0, n))

		return graph, nodes


	def start1(self, nodes):
		return map(lambda i : i + 1, nodes)


	def test_get_all_disjoint_graphs(self):

		def test(n, edges, result):
			graph, _ = self.make_graph_and_node_list(n, edges)
			graphs = map(self.start1, sol.get_all_disjoint_graphs(graph, n))
			self.assertEqual(graphs, result)

		test(3, [[1, 2]], [[1, 2], [3]])
		test(3, [[1, 2], [2, 3]], [[1, 2, 3]])
		test(5, [[1, 2], [2, 3]], [[1, 2, 3], [4], [5]])
		test(5, [[1, 2], [2, 3], [4, 5]], [[1, 2, 3], [4, 5]])
		test(5, [], map(lambda i : [i], range(1, 6)))


if __name__ == '__main__':
	ut_main()
		
