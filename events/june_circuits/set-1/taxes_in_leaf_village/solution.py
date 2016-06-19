n, m, k = map(int, raw_input().split())
tax_change = map(lambda _ : map(int, raw_input().split()), range(0, m))

junction_tax = []

for i in range(1, n + 1):
	jt = 0

	for t in tax_change:
		if t[0] == i or t[1] == i:
			jt += t[2]

	if jt > 0:
		junction_tax.append((i, jt))

junction_tax = sorted(junction_tax, key=lambda i : i[1], reverse=True)

cams = min(k, len(junction_tax)) 

print cams
print ' '.join([str(i) for i, _ in junction_tax[0 : cams]])

