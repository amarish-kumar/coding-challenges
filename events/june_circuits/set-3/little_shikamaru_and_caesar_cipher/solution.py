
def move(input, target, max_k, start=0, count=0):
	if start >= len(input):
		return count

	diff = sub(target[start : len(input)], input[start : len(input)])
	if any([d < 0 for d in diff]):
		return -1
	else:
		for d in diff:
			if d == 0:
				start += 1
			else:
				break

		if start == len(input):
			return count

	for k in range(max_k, 0, -1):
		options = []
		if start + k > len(input):
			continue
		if input[start + k - 1] == target[start + k - 1]:
			continue

		for s in range(1, len(input)):			# allowing substrings to shift and wrap around
			sh = get_rshifted_in_range(input, k, start, s)
			subs = input[start : start + k]
			diff = sub(target[start : start + k], add(subs, sh))

			if all([d == 0 for d in diff]):
				n_input = list(input)
				n_input[start : start + k] = target[start : start + k]
				return move(n_input, target, max_k, start + k, count + 1)
			elif any([d < 0 for d in diff]):
				continue
			else:
				options.append((k, s, sum(diff)))

		s_options = sorted(options, key=lambda i : i[2])
		for o in s_options:
			k = o[0]
			s = o[1]
			sh = get_rshifted_in_range(input, k, start, s)
			n_input = list(input)
			n_input[start : start + k] = add(input[start : start + k], sh)
			count = move(n_input, target, max_k, start, count + 1)
			
			if count > -1:
				return count
						
	return -1


def add(a, b):
	return map(lambda (i, j) : i + j, zip(a, b))
	

def sub(a, b):
	return map(lambda (i, j) : i - j, zip(a, b))


def get_rshifted_in_range(input, k, start, s=1):
	l = len(input)
	nstart = (start - s) + l
	if nstart > l:
		nstart %= l

	shifted = []
	shifted += input[nstart : nstart + k]	# check k against len(input) later
	r = k - (l - nstart)
	if r > 0:
		shifted += input[0 : r]

	return shifted


def main():
	k = input()
	initial = map(lambda i : int(i), raw_input())
	target = map(lambda i : int(i), raw_input())

	count = move(initial, target, k)
	print count


if __name__ == '__main__':
	main()

