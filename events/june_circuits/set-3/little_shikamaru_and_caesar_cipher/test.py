from unittest import TestCase, main as ut_main

import solution as sol


class TestSolution(TestCase):

	def test_get_rshifted_in_range(self):

		def test(input, k, s, start, exp_output):
			i = map(lambda j : int(j), input)
			output = ''.join(map(lambda j : str(j), sol.get_rshifted_in_range(i, k, start, s)))
			self.assertEqual(output, exp_output)


		test('0011', 2, 1, 0, '10')
		test('0011', 2, 2, 0, '11')
		test('0011', 2, 1, 1, '00')
		test('0011', 2, 1, 2, '01')

		test('1111', 2, 1, 2, '11')
		test('00110', 3, 1, 0, '000')
		test('00110', 3, 2, 0, '100')
		test('00110', 4, 2, 0, '1000')

		test('1221', 1, 1, 3, '2')


	def test_move(self):

		def test(initial, target, k, exp):
			i = map(lambda i : int(i), initial)
			t = map(lambda i : int(i), target)
			c = sol.move(i, t, k)

			self.assertEqual(c, exp)

		test('0011', '1221', 2, 2)
		test('0011', '1321', 2, 3)
		test('0014', '1521', 2, -1)
		test('0011', '1011', 2, 1)
		test('0011', '0111', 3, 1)

		test('0000000111', '0000000121', 4, 1) 

		test('0011', '1228', 0, -1)
		test('0022', '2250', 2, -1)

if __name__ == '__main__':
	ut_main()

