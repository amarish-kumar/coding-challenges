
md = 10 ** 9 + 7


def bitcount(n):
	n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
	n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
	n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
	n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
	n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
	n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32)
	return n


def compute(n, items, f, i=0, nv=~0, cost=1):
	for j in range(i, n):
		j_nv = nv & items[j][1]
		j_cost = cost * items[j][0]
		c_nv = bitcount(j_nv)
		fv = f[c_nv]
		f[c_nv] = (fv + j_cost) % md

		compute(n, items, f, j + 1, j_nv, j_cost)


def solve(n, m, items):
	f = [0] * (m + 1)
	compute(n, items, f)

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

