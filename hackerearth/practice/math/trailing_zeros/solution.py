n = int(input())

def p(i, b, c=0):
	if i % b == 0 and i != 0:
		return p(i / b, b, c+1)
	else:
		return c

m2 = 0
m5 = 0

for i in range(1, n + 1):
	m2 += p(i, 2)
	m5 += p(i, 5)
	
mn = min(m2, m5)

print(mn)
