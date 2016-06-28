from unittest import TestCase, main as ut_main
from time import time
from random import randint
import sys

import solution_p as sol


class TestSolution(TestCase):

	def gen(self, random=False):
	
		n = 10000
		max_n = 10000000
		sel = []
		if random:
			sel = map(lambda _ : randint(1, max_n), range(0, n))

		tstart = time()
		for i in range(0, n):
			inn = None
			if random:
				inn = sel[i]
			else:
				inn = i + 1

			sol.solve(inn, n)
			print i, '\r',
			sys.stdout.flush()
		tend = time()

		print 'time:', tend - tstart
		print 'stored result hits:', sol.smem_hits
		print 'total lookup time:', sol.lookup_time


	def test_time(self):
		self.gen()


	def test_random(self):
		self.gen(random=True)


	def test_input_file(self, filename):
		tstart = time()
		with open('io/' + filename, 'r') as f:
			t = int(f.readline().strip())
			for _ in range(0, t):
				n = int(f.readline().strip())
				sol.solve(n, t)
		tend = time()

		print 'time:', tend - tstart
		print 'total lookup time:', sol.lookup_time


	def test_input8(self):
		self.test_input_file('input8.txt')


if __name__ == '__main__':
	ut_main()

