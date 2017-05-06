n = input()
raw_input()

t = (n * (n + 1)) / 2
ev = 0.0
att = 0
c = n

for i in range(1, n + 1):
	att = (i * (i - 1)) / 2
	ev += float(c) / t * att
	c -= 1

m = 10 ** 9 + 7
print pow(t, m - 2, m) * int(ev * t)

