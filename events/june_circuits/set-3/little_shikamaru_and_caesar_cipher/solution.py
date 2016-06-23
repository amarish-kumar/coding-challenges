
def move(input, target, max_k, start=0, count=0):
	if start >= len(input):
		return True, count

	diff = sub(target[start : start + k], input[start : start + k])
	if all([d == 0 for d in diff]):
		return move(input, target, max_k, start + k, count)

	options = []
	for k in range(max_k, 0, -1):
		if input[start + k - 1] == target[start + k - 1]:
			continue
		if start + k > len(input):
			break

		for s in range(1, len(input) - (start + k) + 1):
			sh = get_rshifted_in_range(input, k, start, s)
			count += 1
			subs = input[start : start + k]
			diff = sub(target[start : start + k], add(subs, sh))

			if all([d == 0 for d in diff]):
				n_input = list(input)
				n_input[start : start + k] = target[start : start + k]
				return move(n_input, target, max_k, start + k, count)
			elif any([d < 0 for d in diff]):
				continue
			else:
				options.append((k, s, sum(diff))

	s_options = sorted(options, key=lambda i : i[2])
	for o in s_options:
		k = i[0]
		s = i[1]
		sh = get_rshifted_in_range(input, k, start, s)
		n_input = list(input)
		n_input[start : start + k] = add(input[start : start + k], sh)

		success, count = move(n_input, target, max_k, start, count)
		
		if success:
			return success, count
						
	return False, count


	# max shift first
	# opt k size, start from end of window, if elements same, reduce window size

	# for k from max to 1, -1
	# for s from 1 to max_possible_shifts, +1
	#  calc. diff
	#  if any elem greater, abort, move to next k
	#  if diff for all 0, accept, jump to end of window + 1, call move(changed input, k, start= end of w + 1, count), break for loop
	#  if diff less for some, add it to list, (changed range, diff total)
	# end for, s
	# end for, k

	# we have the list, sort it in asc. order of diff total
	# for each item in list
	#  call move(changed range, k, start= location of first diff elem, count)

	
	# how to detect failure
	# you reach the end (?), return False at the end and check for it in every call

	# success ?
	# if last window and diff = 0, return True, count


def add(a, b):
	return map(lambda i, j : i + j, zip(a, b))
	

def sub(a, b):
	return map(lambda i, j : i - j, zip(a, b))


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

	count = move(initial, target)
	print count


if __name__ == '__main__':
	main()

