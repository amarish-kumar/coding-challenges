t = input()

for _ in range(0, t):
	n = input()

	c = n / 2
	le = s = n % 2
	e = n % 2

	s = (4 * le) + \
		(16 * (1 - (4 ** (c - 1))) / (1 - 4)) + \
		((16 - (16 + (c - 2) * 2) * (4 ** (c - 1))) / (1 - 4)) + ((2 * 4 * (1 - 4 ** (c - 2))) / ((1 - 4) ** 2)) + \
		(10 * e * c) + ((c * (10 + (10 + 20 * (c - 1)))) / 2)


	s = s % (10 ** 9 + 9)
		
	print s

# note: tried to convert the summing in for loop in a summation formula
# using arithmetic, geometric and arithmetico-geometric progression formulae
# not getting the right output, something wrong with the formula
# and it's not that fast anyway

# possible solution: fix the formula and cache the results so 
# that sum can be calculated for greater numbers by just adding
# the additional terms

