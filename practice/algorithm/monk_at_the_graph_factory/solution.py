c = input()
vlist = map(int, raw_input().split())

def walk(c, vlist):
	for i in range(0, c):
		v = vlist[i]
		if (v == 1 and (i == 0 or any([k == 1 for k in vlist[0:i]])) and not (i == (c-2) and vlist[c-1] == 1)) or v == 0:
			continue

		for j in range(0, c):
			if j != i and vlist[j] > 0:
				vlist[j] -= 1
				v -= 1
			if v == 0:
				break
		vlist[i] = v

walk(c, vlist)

if any([i > 0 for i in vlist]):
	print 'No'
else:
	print 'Yes'
