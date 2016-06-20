import getopt
import sys
from random import choice, randint


def generate(n, min_d):
	akatsuki = map(lambda i : i, range(0, n))
	leaf = list(akatsuki)

	a_xy = map(lambda i : [], range(0, n))
	l_xy = list(a_xy)

	last_a = None
	used_d = min_d
	last_d = None

	for i in range(0, n):
		if used_d <= 0:
			print 'error'
			raise Exception()

		l = choice(leaf)
		leaf.remove(l)

		lx = ly = None
		if last_a is not None:
			lx = last_d + randint(10, 100) + last_a[0]
			ly = randint(10, 100) + last_a[1]
		else:
			lx = ly = 0

		a = choice(akatsuki)
		akatsuki.remove(a)

		d = None
		if i < (n - 1):
			d = randint(2, min_d / 2)
			while not ((used_d - d) >= ((n - i - 1) * 2)):
				d = randint(2, min_d / 2)
		else:
			d = used_d

		used_d -= d
		last_d = d

		dx = randint(1, d - 1)
		dy = d - dx

		ax = lx + dx
		ay = ly + dy

		a_xy[a] = (ax, ay)
		l_xy[l] = (lx, ly)

		last_a = (ax, ay)
	
	return a_xy, l_xy


if __name__ == '__main__':
	optlist, _ = getopt.getopt(sys.argv[1:], None, ['n=', 'min-distance='])

	n = 10
	min_d = 10

	for o in optlist:
		if o[0] == '--n':
			n = int(o[1])
		elif o[0] == '--min-distance':
			min_d = int(o[1])


	a_xy, l_xy = generate(n, min_d)

	print n
	print '\n'.join(['%d %d'%(x, y) for x, y in a_xy])
	print '\n'.join(['%d %d'%(x, y) for x, y in l_xy])

