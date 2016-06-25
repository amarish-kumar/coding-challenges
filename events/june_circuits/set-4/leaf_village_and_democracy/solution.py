
def make_zoo(n, q):
	# read request
	# if req = SEP, update constraint list
	# if req = ASK, make / update zoo, print zoo
	# if req = CANCEL, update constraint list

	rem_q = [[]] * n	# removal queue (for removed constraints after a SEPARATE request is deleted)

	req_q = []		# (k, cons_c, cons list)
	zoo = []		# zoo partitions
	zoo_map = []		# map from animal index to partition index

	for r in range(0, q):
		req_type, k, terrs = read_next_request()

		if req_type == 'SEPARATE':
			# form cons pairs
			# add them to list, index = smaller item, add req id: r

			cons_c, cons = make_cons_pairs(terrs, k, n)
			req_q.append((k, cons_c, cons))

		elif req_type == 'CANCEL':
			# form cons pairs
			# count them
			# look up req q with k and cons_c
			# if match, check cons 1 by 1
			# if all match: remove req, for each cons pair that doesn't exist in other req's, add to rem_list

			cons_c, cons = make_cons_pairs(terrs, k, n)

			i = 0
			found_req = False
			for r_k, r_cons_c, r_cons in req_q:
				found_req = True
				if k == r_k and cons_c == r_cons_c:
					for l in range(0, cons):
						found_req = found_req and set(cons[l]) == set(r_cons[l])
						if not found_req:
							break
				if found_req:
					break
				i += 1
					
			del req_q[i]		# delete SEPARATE request

			for _, _, r_cons in req_q:	# delete constraint pairs that are unique in the deleted request
				for i in range(0, n):
					for j in r_cons[i]:
						if j in cons[i]:
							cons[i].remove(j)

			for i in range(0, n):
				rem_q[i].extend(cons[i])
			

		else:	# 'ASK'
			# if rem_list is not empty, merge according to it
			# make zoo if not already made
			# print zoo

			if len(zoo) == 0:
				rem_q = [[]] * n

				p = 1
				zoo.append([])
				for i in range(0, n):
					added = False
					for cp in range(0, p):			# check all existing partitions
						# check constraints
						if check_constraints(i, zoo[cp], req_q):
							zoo[cp].append(i + 1)
							added = True
							zoo_map.append(cp)
							break
					if not added:
						zoo.append([i + 1])			# add new partition
						zoo_map.append(p)
						p += 1

			else:
				# do merging
				# for each item in rem q, merge if no conflict with others, try both ways, sort
				# in the end, sort partitions by first elememnt

				for i in range(0, n):
					if len(rem_q[i]) > 0:
						i_part = zoo_map[i]
						ip = list(zoo[i_part])
						ip.remove(i)
						for j in rem_q[i]:
							j_part = zoo_map[j]
							if check_constraints(j, ip, req_q):
								zoo[i_part] = sorted(zoo[i_part] + [j])
								zoo[j_part].remove(j)
								zoo_map[j] = i_part
							else:
								jp = list(zoo[j_part])
								jp.remove(j)
								if check_constraints(i, jp, req_q):
									zoo[j_part] = sorted(zoo[j_part] + [i])
									zoo[i_part].remove(i)
									zoo_map[i] = j_part

				rem_q = [[]] * n	# empty the removal queue

				d = []
				for i in range(0, len(zoo)):	# find the 0 length partitions and mark them for deletion
					if len(zoo[i]) == 0:	# and update zoo_map according to deletions
						d.append(i)
						for j in range(0, n):
							if zoo_map[j] > i:
								zoo_map[j] -= 1	
				for i in d:
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
			idx = min(a - 1, i)
			ch = max(a, i + 1)

			if ch in r_cons[idx]:
				return False
		#if any(a in r_cons[i] for a in arr):
		#	return False
	return True


def empty_lol(n):
	return list([] for i in range(0, n))


def make_cons_pairs(terrs, k, n):
	cons = empty_lol(n)
	cons_c = 0

	for i in range(0, k):
		for j in range(i + 1, k):
			#if i != j:
			for l in terrs[i][1]:
				for m in terrs[j][1]:
					c = cons[min(l, m) - 1]
					#c = cons[min(l, m) - 1]
					#print 'c: ', min(l, m) - 1, c, cons
					mx = max(l, m)
					if not mx in c:
						c.append(mx) 	
						#print 'pair:', sorted((l, m))
						cons_c += 1

	print cons_c, cons
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

