count = input()
for _ in range(0, count):
	print reduce(lambda x, y : y + x, raw_input(), '')
