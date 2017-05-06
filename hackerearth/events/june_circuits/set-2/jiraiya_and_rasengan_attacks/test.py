from unittest import TestCase, main as ut_main
from random import choice


class TestSolution(TestCase):

	def test_swap_count(self):
		for i in range(2, 1001):
			o = map(lambda i : i, range(0, i))
			a = []
			for j in range(0, i):
				k = choice(o)
				o.remove(k)
				a.append(k)

			est = 0
			e = 0
			c = 0
			for j in range(i - 1, -1, -1):
				if a[j] < j:
					d = j - a[j]
					est += d
					e += d + 1
					c += 1

				if a[j] > j:
					est += a[j] - j - e

				if e > 0: e -= 1
					

			cp = list(a)
			sc = self.bubble_sort(cp, i)
			self.assertEqual(sc, est, 'est: %d, actual: %d'%(est, sc) + str(a))


	def bubble_sort(self, a, n):
		s = 0
		for i in range(0, n):
			for j in range(0, n - i - 1):
				if a[j] > a[j + 1]:
					t = a[j]
					a[j] = a[j + 1]
					a[j + 1] = t
					s += 1
		return s


if __name__ == '__main__':
	ut_main()

