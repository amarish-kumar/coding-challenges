t = input()

for _ in range(0, t):
	n, m = map(int, raw_input().split())
	l = map(int, raw_input().split())

	for _ in range(0, m):
		sit = []

		for i in range(0, n):
			if i == 0 and l[1] == 1:
				sit.append(i)
			elif i == n-1 and l[n-2] == 1:
				sit.append(i)
			elif l[i-1] == 1 and l[i+1] == 1:
				sit.append(i)

		l = map(lambda x : 1 if (x in sit) else 0, range(0, n))
		if max(l) == 0:
			break

	print ' '.join(map(str,l))

