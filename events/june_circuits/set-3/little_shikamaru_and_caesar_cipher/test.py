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


if __name__ == '__main__':
	ut_main()

