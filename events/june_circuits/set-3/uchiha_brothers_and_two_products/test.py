from unittest import TestCase, main as ut_main
from random import randint
import sys

import solution as sol


class TestSolution(TestCase):

	def test_large_n(self):

		def test(n):
			m = randint(1, 20)
			items = []
			max_nv = int('1' * m, base=2)
			for i in range(0, n):
				cost = randint(1, 1000000)
				nv = randint(0, max_nv)
				items.append((cost, nv))

			sol.solve(n, m, items)
			print '.',
			sys.stdout.flush()

		for i in range(0, 1):
			n = randint(1, 2)
			test(100)

		print


	def test_sample(self):

		def test(n, m, items, exp_f):
			items = map(lambda j : (j[0], int(j[1], base=2)), items)
			f = sol.solve(n, m, items)
			self.assertEqual(f, exp_f)

		test(3, 3, [(2, '101'), (3, '111'), (5, '010')], [40, 20, 8, 3])
		test(2, 3, [(2, '101'), (3, '111')], [0, 0, 8, 3])


if __name__ == '__main__':
	ut_main()

