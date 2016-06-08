n, d = map(int, raw_input().split())

edges = []
for _ in range(0, d):
	v1, v2 = map(int, raw_input().split())
	edges.append((v1, v2))

if len(set([i for e in edges for i in e])) < n:		# some friends don't have a dependency, so, they won't be in the edge list
	print 1

elif len([v2 for v1, v2 in edges if not v2 in [v1 for v1, _ in edges]]) > 0:	# friends only appearing on the right side of the edges don't have any
	print 1									# dependency either

else:							# find smallest dependency tree
	min_friends = 1001

	def find_edges_starting_with(v):
		return [e for e in edges if e[0] == v]

	def uniq(t):
		return len(set([i for e in t for i in e]))			# count of unique vertices in a tree

	for e in edges:		# form dependency tree for each edge
		v1, v2 = e
		tree = [e]
		visit = [v1, v2]

		while len(visit) > 0:
			deps = find_edges_starting_with(visit.pop())
		
			for dep in deps:
				if not dep in tree:
					tree.append(dep)
					if not dep[1] in visit:
						visit.append(dep[1])

		min_friends = min(min_friends, uniq(tree))
		
	print min_friends

