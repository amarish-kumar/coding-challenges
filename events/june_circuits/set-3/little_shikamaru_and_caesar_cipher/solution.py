
def move(input, k, start=0, count=0):
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
	
	pass
	
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

def cmp(a, b):
	return reduce(zip(a, b), lambda s, i, j : s + (i - j))


def rshift(input, k, start):
	pass




def main():
	k = input()
	initial = map(lambda i : int(i), raw_input())
	target = map(lambda i : int(i), raw_input())

	count = move(initial, target)
	print count


if __name__ == '__main__':
	main()




	# for each diff window
	#  if window size > k
	#   start at the beginning of window, with string of size k (sk)
	#   get rshifted contents for this sk
	#   add it to sk, and check (cmp)
	#    if diff == 0, accept the shift
	#    if diff > 0, reject
	#    else, go forward with sk as initial
	#
	#   shift sk to right

	# if window size < k
	#  detect sk's for which items otehr than window size are 0's


	# shift

	# detect diff windows
	# 2 passes ??


	# calc. diff, adjust k, get diff's with all shifts, stop at 0, o/w sort by diff and start with least diff 

	# start at 0
	#  if sk is diff
	#   shift
	#   calc diff
	#   if diff == 0, ok, move sk to right
	#   if diff > 0, abort, return false, if init > targt, it should return false
	#   if diff < 0, don't move sk, try rshift again
	#    or move by 1 if first element matches and shifted content's first element is not 0

