trees = []
n, d = map(int, raw_input().split())

for _ in range(0, d):
	d1, d2 = map(int, raw_input().split())

	found = False
	for t in trees:
		if (d1 in t and d2 in t):
			continue
		if (d1 in t):
			t.append(d2)
			found = True
		elif (d2 in t):
			t.append(d1)
			found = True

	if not found:
		trees.append([d1, d2])

	

def intersect(t1, t2):
	return any([i in t1 for i in t2])

def merge(t1, t2):
	return list(set(t1 + t2))


for i in range(0, len(trees) - 1):
	for j in range(i+1, len(trees)):
		if intersect(trees[i], trees[j]):
			trees[i] = merge(trees[i], trees[j])
			trees[j] = []

print min([len(t) for t in trees if len(t) > 0])

