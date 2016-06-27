
def make_zoo(n, q):
	# read request
	# if req = SEPARATE, update constraint list
	# if req = ASK, make / update zoo, print zoo
	# if req = CANCEL, find matching req and delete and add removed constraint pairs to removal list

	rem_q = empty_lol(n)	# removal queue (for removed constraints after a SEPARATE request is deleted)
	req_q = []		# (k, cons_c, cons list)
	zoo = []		# zoo partitions
	zoo_map = []		# map from animal index to partition index

	for r in range(0, q):
		req_type, k, terrs = read_next_request()

		if req_type == 'SEPARATE':
			cons_c, cons = make_cons_pairs(terrs, k, n)
			req_q.append((k, cons_c, cons))

		elif req_type == 'CANCEL':
			cons_c, cons = make_cons_pairs(terrs, k, n)

			i = 0
			found_req = False
			for r_k, r_cons_c, r_cons in req_q:
				found_req = True
				if k == r_k and cons_c == r_cons_c:	# speed up matching request lookup by comparing no. of territories 
					for l in range(0, n):		# and no. of constraints first
						found_req = found_req and set(cons[l]) == set(r_cons[l])	# compare constraints
						if not found_req:
							break
				else:
					found_req = False
				if found_req:
					break
				i += 1
				
			if not found_req:	# no matching SEPARATE request found
				continue

			del req_q[i]		# delete matched SEPARATE request

			for _, _, r_cons in req_q:	# delete constraint pairs that are not unique in the deleted request
				for i in range(0, n):
					for j in r_cons[i]:
						if j in cons[i]:
							cons[i].remove(j)

			for i in range(0, n):	# add unique constraint pairs to removal list
				rem_q[i].extend(cons[i])
			

		else:	# 'ASK'
			if len(zoo) == 0:
				rem_q = empty_lol(n)	# if zoo is not made yet, removal list does not matter

				p = 1
				zoo.append([])
				for i in range(0, n):
					added = False
					for cp in range(0, p):			# check all existing partitions
						if check_constraints(i, zoo[cp], req_q):
							zoo[cp].append(i + 1)	# append to an existing partition if not conflicting with existing members
							added = True
							zoo_map.append(cp)
							break
					if not added:				# can't go into any existing partition
						zoo.append([i + 1])		# add new partition
						zoo_map.append(p)
						p += 1

			else:	# merge
				# for each constraint pair in removal queue, since, it is now removed,
				# try to merge the members in that pair into a single partition
				# merge only if no conflict occurs with existing members in a partition
				# if conflict occurs in partition of member 1, then try merging into partition of member 2
				# if merged, sort the partition in ascending order

				# after all removed pairs are processed, sort partitions by first elememnt

				if any([len(i) > 0 for i in rem_q]):
					for i in range(0, n):
						if len(rem_q[i]) > 0:
							i_part = zoo_map[i]
							ip = list(zoo[i_part])
							ip.remove(i + 1)
							for j in rem_q[i]:
								j_part = zoo_map[j - 1]
								if check_constraints(j - 1, ip, req_q):		# move member 2 to partition of member 1
									zoo[i_part] = sorted(zoo[i_part] + [j])
									zoo[j_part].remove(j)
									zoo_map[j - 1] = i_part
								else:						# move member 1 to partition of member 2
									jp = list(zoo[j_part])
									jp.remove(j)
									if check_constraints(i, jp, req_q):
										zoo[j_part] = sorted(zoo[j_part] + [i + 1])
										zoo[i_part].remove(i + 1)
										zoo_map[i] = j_part

					rem_q = empty_lol(n)	# empty the removal queue

					d = []
					for i in range(0, len(zoo)):	# find the 0 length partitions and mark them for deletion
						if len(zoo[i]) == 0:	# and update zoo_map according to deletions
							d.append(i)
							for j in range(0, n):
								if zoo_map[j] > i:
									zoo_map[j] -= 1	

					for i in sorted(d, reverse=True):
						del zoo[i]

					zoo = sorted(zoo, key=lambda i : i[0])
				
			print_zoo(zoo)
						
def print_zoo(zoo):
	print len(zoo)
	print '\n'.join([' '.join([str(i) for i in p]) for p in zoo])


def check_constraints(i, arr, req_q):
	if len(arr) == 0:
		return True

	for _, _, r_cons in req_q:
		for a in arr:
			idx = min(a - 1, i)	# note the index adjustment as list has 0 based index
			ch = max(a, i + 1)	# so, to find constraints for member 1, we access r_cons[0] and so on
						# a bucket at index i always contains members >i
			if ch in r_cons[idx]:
				return False
	return True


def empty_lol(n):
	return list([] for i in range(0, n))


def make_cons_pairs(terrs, k, n):		# make constraint pairs for a SEPARATE or CANCEL request
	cons = empty_lol(n)			# a constraint pair: i, j means that i and j cannot be in same territory
	cons_c = 0

	for i in range(0, k):			# basically, cross product of each territory with other territories
		for j in range(i + 1, k):
			for l in terrs[i][1]:
				for m in terrs[j][1]:
					c = cons[min(l, m) - 1]
					mx = max(l, m)
					if not mx in c:
						c.append(mx) 	
						cons_c += 1

	return cons_c, cons


def read_next_request():
	line_1 = raw_input().split()
	req_type = line_1[0]

	if req_type == 'ASK':
		return req_type, None, None

	k = int(line_1[1])
	terrs = []

	for _ in range(0, k):
		line = map(int, raw_input().split())
		m = line[0]
		e = line[1:]
		terrs.append((m, e))

	return req_type, k, terrs


def main():
	n, q = map(int, raw_input().split())
	make_zoo(n, q)


if __name__ == '__main__':
	main()

