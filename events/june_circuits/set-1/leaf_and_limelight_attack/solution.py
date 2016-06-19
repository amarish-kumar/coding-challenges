t = input()

mem = {}

for _ in range(0, t):
	n = input()

	c = n / 2
	le = s = n % 2
	e = n % 2

	nearest_n = n - min([n - i for i in mem.keys() if i <= n and i % 2 == e] + [n])

	if nearest_n == n:
		s = m[nearest_n][0]
		
	else: 
		if nearest_n > 0:
			m = mem[nearest_n]
			s = m[0]
			le = m[1]
			c -= nearest_n / 2
			e += nearest_n

		for _ in range(0, c):
			s += (4 * le) + 10 * (e + 1)
			le += 4 * (e + 1)
			e += 2

		s = s % (10 ** 9 + 9)
		
		if  n % 10 == 0:
			mem[n] = (s, le)

	print s

