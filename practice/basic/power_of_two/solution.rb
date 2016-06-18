t = Integer(gets)

for _ in 1..t
	n = Integer(gets)
	a = gets.split(" ").map { |i| Integer(i) }

	max = a.max
	max_shift = 0
	while max > 0
		max_shift += 1		# find leftmost 1 in all of numbers
		max >>= 1
	end

	b = 1
	i = 0
	found = false

	while i < max_shift && !found	# check for a subset for each position of 1 (i.e. each power of 2) 
		t = []
		for j in 0..n-1
			if (a[j] & b) > 0	# found 1 in the right place
				t.push(a[j])
				if t.reduce(~0, :&) == b	# subset is found when there are more than one element in the list (t)
					puts "YES"		# and all of them "&" to the power of 2 (b)
					found = true		# we don't care for members of the subset, so, we just "&" all elements in t
					break
				end
			end
			found and break			
		end

		i += 1
		b <<= 1
	end

	!found and puts "NO"
end

