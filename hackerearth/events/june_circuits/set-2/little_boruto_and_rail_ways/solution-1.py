def main():
	n, m = map(int, raw_input().split())
	roads = map(lambda _ : map(int, raw_input().split()), range(0, m))

	print 0 if n <= 2 else n


if __name__ == '__main__':
	main()


# notes:
# extremely simple approach
# for n = 1, obviously, design score = 0
# for n = 2, only one path possivle, so design score = 0
# forn n >= 3, always at least 2 or more paths, so design score = n
# (assumption: all nodes are connected; as stated in constraint 4 in the problem)
#
# score: 24 (failures: errors)

