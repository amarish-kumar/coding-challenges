from math import sqrt, ceil

def factorize(n):
	f = []
	on = n
	
	while n % 2 == 0 and n > 1:
		f.append(2)
		n = int(n / 2)
		
	for i in range(3, ceil(sqrt(on)) + 2, 2):
		while n % i == 0 and n > 1:
			f.append(i)
			n = int(n / i)
			
		if n == 1:
			break
			
	if n > 1:
		f.append(n)
			
	return f
	
def get_single_digit_factors(x):
	m = 1000000007
	
	for _ in range(0, 10):
		f = factorize(x)
		if any([i > 9 for i in f]):
			x += m
		else:
			return f, x
			
	return []
	
def make_spi(f, x):
	for i in range(1, ceil(x/7) + 1):
		spi = []
		r = try_spi(f, 0, spi, i)
		if r:
			return ''.join([str(i) for i in sorted(spi)])
			
def try_spi(f, i, spi, d):
	if d == 1:
		digit = 1
		while i < len(f):
			digit *= f[i]
			i += 1
			if digit > 9:
				return False
		spi.append(digit)
		return True
	else:
		digit = f[i]
		idx = len(spi)
		spi.append(digit)
		while try_spi(f, i+1, spi, d-1) == False:
			i += 1
			digit *= f[i]
			if digit > 9:
				del spi[-1]
				return False
			spi[idx] = digit
		return True
		

def main():
	x = int(input())
	if x > 0:
		f, x = get_single_digit_factors(x)
		y = make_spi(f, x)
		print(y)
	else:
		print(10)
	
main()
