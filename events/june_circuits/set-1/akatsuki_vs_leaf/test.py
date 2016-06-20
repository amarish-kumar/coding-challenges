from unittest import TestCase, main as ut_main
from random import randint

import solution as sol
import gen


class TestSolution(TestCase):

	def test_random(self):
		for i in range(0, 1000):
			n = randint(1, 40)
			min_d = randint(2 * n, 100 * n)

			a, l = gen.generate(n, min_d)
			md = sol.compute_min_distance(n, a, l)
			self.assertEqual(md, min_d)


if __name__ == '__main__':
	ut_main()

