from unittest import TestCase, main as ut_main

import solution as sol


class TestRemoves(TestCase):
	gr1 = [	[0, 1, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 1, 0]]


	def test_get_reachable_nodes(self):
		self.assertListEqual([0, 1, 2, 3, 4], sorted(sol.get_reachable_nodes(0, 5, self.gr1)))
		self.assertListEqual([0, 1, 2, 3, 4], sorted(sol.get_reachable_nodes(1, 5, self.gr1)))
		self.assertListEqual([3, 4], sorted(sol.get_reachable_nodes(3, 5, self.gr1)))
		self.assertListEqual([3, 4], sorted(sol.get_reachable_nodes(4, 5, self.gr1)))


	def test_get_edges(self):
		self.assertListEqual([(0, 1), (1, 2), (2, 0)], sol.get_edges([0, 1, 2], 5, self.gr1))
		self.assertListEqual([(3, 4), (4, 3)], sol.get_edges([3, 4], 5, self.gr1))


	def test_find_sccs(self):
		self.assertListEqual([[(0, 1), (1, 2), (2, 0)], [(3, 4), (4, 3)]], sol.find_sccs(5, self.gr1))


	def test_remove(self):
		self.assertListEqual([(1, 3)], sol.remove(100, 5, self.gr1, sol.find_sccs(5, self.gr1)))


if __name__ == '__main__':
	ut_main()

