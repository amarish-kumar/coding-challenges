t = input()

for _ in range(0, t):
	n, m = map(int, raw_input().split())
	l = map(lambda (i, v) : i, filter(lambda (i, v) : v == 1, enumerate(map(int, raw_input().split()))))	# read in the list of 1's and 0's
												# and convert it into a list of indexes	of 1's
	t = []
	for c in range(0, m):
		for i in range(0, len(l)):
			if l[i] == 1:
				t.append(0)
			elif i>0 and l[i] - l[i-1] == 2:	# e.g. when 0, 2; append 1
				t.append(l[i]-1)
			elif i>1 and l[i] - l[i-2] == 2:	# e.g. when 0, 1, 2; append 1
				t.append(l[i]-1)
			if l[i] == n-2:
				t.append(n-1)

		l = sorted(t)
		t = []
		if len(l) == 0 or len(l) == n:			# all 0's or all 1's will never change
			break

		alt_c = n / 2	# count of 1's (people sitting down) for alternate pattern of "1 0 1 0..." or "0 1 0 1 0..." to be present
				# it could be 1 extra for odd n (handled by the next if condition)
		alt = False
		if 0 <= (len(l) - alt_c) <= 1:
			alt = True
			for i in range(0, len(l)-1):	# check if alternate pattern exists
				if l[i+1] - l[i] != 2:
					alt = False
					break

		if alt:		# if alterenate pattern exists, flip it if necessary and break the loop
			rem = m - (c + 1)		# get count of remaining hours and flip alt pattern if it is odd
			if rem % 2 == 1:
				if l[0] == 0:
					l = map(lambda x : x+1, l)
					if n % 2 == 1: del l[-1]
				else:
					l = map(lambda x : x-1, l)
					if n % 2 == 1: 
						l.append(n-1)
			break

	print ' '.join(map(lambda i : '1' if i in l else '0', range(0, n)))

