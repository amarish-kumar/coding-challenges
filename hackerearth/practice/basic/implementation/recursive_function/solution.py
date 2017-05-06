import math

x, y = map(int, input().split())

cs = lambda i : 10 ** int(math.log10(i))	# compute step
sx = cs(x)	# step for x
sy = 10		# step for y

m = []

def ms(x, y, r):	# store partial results in memory
	global sx, sy
	
	if (x % sx == 0) and (y % sy == 0):
		m.append((x, y, r))
		
	if x >= 10 * sx:
		sx *= 10
		
	'''if (y >= 10 * sy):
		sy *= 10'''
		
	return r
	
def ml(x, y):	# lookup memory
	for i, j, r in m:
		if i == x and j == y:
			return r
	return None
	
def f(x, y):
	mr = ml(x, y)
	if mr is not None:
		return mr
			
	if x == 0:
		return ms(x, y, y + 1 % 1000)
	elif x > 0 and y == 0:
		return ms(x, y, f(x - 1, 1) % 1000)
	else:
		return ms(x, y, f(x - 1, f(x, y - 1)) % 1000)
		
print("%03d"%f(x, y))
