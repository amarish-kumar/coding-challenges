n = Integer(gets)
s = gets

min = max = n
i = 0
v = false

while i < n
	if s[i] == 'w'
		max += 1
		if v && s[i+1] == 'v'	# detect 'vwv', if first v hasn't already been consumed
			min -= 1
			i += 1
			v = false
		end
	elsif i < n-1 && s[i] == 'v'
		if s[i+1] == 'v'	# detect 'vv', mark the next (second) v as consumed
			min -= 1
			v = false
			i += 1
		else
			v = true
		end
	else
		v = false
	end
	i += 1
end

print min, " ", max, "\n"

