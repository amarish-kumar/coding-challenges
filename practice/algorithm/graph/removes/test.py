from unittest import TestCase, main as ut_main

import solution as sol


class RemovesTest(TestCase):

	def test_get_reachable_nodes(self):
		gr1 = [	[0, 1, 0, 0, 0],
			[0, 0, 1, 1, 0],
			[1, 0, 0, 0, 0],
			[0, 0, 0, 0, 1],
			[0, 0, 0, 1, 0]]

		self.assertListEqual([0, 1, 2, 3, 4], sorted(sol.get_reachable_nodes(0, 5, gr1)))
		self.assertListEqual([0, 1, 2, 3, 4], sorted(sol.get_reachable_nodes(1, 5, gr1)))
		self.assertListEqual([3, 4], sorted(sol.get_reachable_nodes(3, 5, gr1)))
		self.assertListEqual([3, 4], sorted(sol.get_reachable_nodes(4, 5, gr1)))



if __name__ == '__main__':
	ut_main()

