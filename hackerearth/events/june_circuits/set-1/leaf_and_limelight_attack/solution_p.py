from time import time

mem = [(None, None, None)] * 2
smem_hits = 0
mod = 10 ** 9 + 9
enable_sort_compute = False
smem = []
total_n = 0
smem_last = 0
lookup_time = 0


def strength(inn):
	global mem
	global smem
	global enable_sort_compute
	global smem_last

	n_start = inn if not enable_sort_compute else smem_last + 1
	smem_last = inn
	s = None

	for n in range(n_start, inn + 1):
		c = n / 2
		le = s = n % 2
		e = n % 2

		m = mem[n % 2]
		nearest_n = m[0]

		if nearest_n == n:
			s = m[1]
			
		else: 
			if n > nearest_n > 0:
				s = m[1]
				le = m[2]
				c -= nearest_n / 2
				e = nearest_n

			for _ in range(0, c):
				s += (4 * le) + 10 * (e + 1)
				s %= mod
				le += 4 * (e + 1)
				le %= mod
				e += 2

			if enable_sort_compute:
				smem.append(s)

			mem[n % 2] = (n, s, le)

	return s


def solve(n, t):
	global smem
	global enable_sort_compute
	global total_n
	global smem_hits
	global lookup_time

	total_n += 1
	if (not enable_sort_compute) and n > total_n and t > 100:
		enable_sort_compute = True

	if enable_sort_compute:
		if n > smem_last:
			strength(n)
		else:
			smem_hits += 1
		ts = time()
		r = smem[n - 1]
		lookup_time += time() - ts
		return r
	else:	
		s = strength(n)
		return s



def main():
	t = input()

	for _ in range(0, t):
		n = input()
		print solve(n, t)


if __name__ == '__main__':
	main()

