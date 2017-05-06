t = input()

for _ in range(0, t):
	n = input()

	c = n / 2
	le = s = n % 2
	e = n % 2

	for _ in range(0, c):
		s += (4 * le) + 10 * (e + 1)
		le += 4 * (e + 1)
		e += 2

	print s % (10 ** 9 + 9)
