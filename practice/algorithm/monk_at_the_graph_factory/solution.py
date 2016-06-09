c = input()
vlist = sorted(map(int, raw_input().split()), reverse=True)	# read and sort the degrees in descending order

def walk(c, vlist):
	for i in range(0, c-1):
		v = vlist[i]

		if v == 0:
			return	

		if vlist[i+1] > 0:	# possibly connect to the vertex which will in turn connect to more vertices, thus, helping us walk the tree
			vlist[i+1] -= 1
			v -= 1

		for j in range(i+2, c):		# consume leaf vertices
			if vlist[j] == 1:
				vlist[j] = 0
				v -= 1
			if v == 0:
				break
	
		vlist[i] = v

walk(c, vlist)

if max(vlist) == 0: print 'Yes'
else: print 'No'

