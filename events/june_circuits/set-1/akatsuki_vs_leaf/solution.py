n = input()
akatsuki = map(lambda _ : map(int, raw_input().split()), range(0, n))
leaf = map(lambda _ : map(int, raw_input().split()), range(0, n))

distance = []
for a in range(0, n):
	for l in range(0, n):
		d = abs(akatsuki[a][0] - leaf[l][0]) + abs(akatsuki[a][1] - leaf[l][1])
		distance.append((a, l, d))

distance = sorted(distance, key=lambda i : i[2])

pa = []
pl = []
min_distance = 0
for i in distance:
	if not i[0] in pa and not i[1] in pl:
		min_distance += i[2]
		pa.append(i[0])
		pl.append(i[1])

print min_distance

