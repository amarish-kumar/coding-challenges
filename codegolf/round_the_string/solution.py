def rnd(s,p):
	d=s.find('.')
	if d<0:
		if p>0:
			d=len(s)
			s+='.'
		else:
			return s
	e=(d+p+1)-len(s)
	if e>0:
		return s+'0'*e
	o=''
	c=0
	for i in range(len(s)-1,-1,-1):
		x=s[i]
		if i<=d+p:
			if i!=d:
				n=int(x)+c
				if n>9: n=0;c=1 
				else: c=0
				o+=str(n)
			else:
				if p>0: o+=x
		if i==d+p+1:
			c=int(x)>4
	if c: o+='1'
	return ''.join(reversed(o))
