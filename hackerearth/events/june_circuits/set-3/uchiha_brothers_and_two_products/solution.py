
md = 10 ** 9 + 7
bitcount = lambda n, m : sum(map(lambda i : (n >> i) & 1, range(0, m)))


def compute(n, m, items, f, i=0, nv=~0, cost=1):
	for j in range(i, n):
		j_nv = nv & items[j][1]
		j_cost = cost * items[j][0]
		c_nv = bitcount(j_nv, m)
		fv = f[c_nv]
		f[c_nv] = (fv + j_cost) % md

		compute(n, m, items, f, j + 1, j_nv, j_cost)


def solve(n, m, items):
	f = [0] * (m + 1)
	compute(n, m, items, f)

	return f


def main():
	n, m = map(int, raw_input().split())

	def read_cost_nv_pair(_):
		c, nv = raw_input().split()
		return int(c), int(nv, base=2)

	items = map(read_cost_nv_pair, range(0, n))

	f = solve(n, m, items)
	print ' '.join([str(i) for i in f])


if __name__ == '__main__':
	main()

