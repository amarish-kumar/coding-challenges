def main():
	n, m = map(int, raw_input().split())
	roads = map(lambda _ : map(int, raw_input().split()), range(0, m))

	v = [0] * n

	for i, j in roads:
		if i != j: 
			v[i - 1] = 1
			v[j - 1] = 1

	design_score = reduce(lambda x, y : x + y, v)
	print design_score


if __name__ == '__main__':
	main()


# notes:
# very simple approach
# make a single pass through the road list and detect all nodes that have edges (roads) from it
# those nodes (stations) will have a path going another node and coming back (hence, length of at least 2)
# count those nodes
#
# score: 24 (failures: errors)

