n = input()
raw_input()

def mod(a, b, m):
	i = 1
	while 1:
		d = i * m + a
		if d % b == 0:
			return d / b
		i += 1

t = (n * (n + 1)) / 2
ev = 0.0
att = 0
c = n

for i in range(1, n + 1):
	att = (i * (i - 1)) / 2
	ev += float(c) / t * att
	c -= 1

print mod(int(ev * t), t, 10 ** 9 + 7)

