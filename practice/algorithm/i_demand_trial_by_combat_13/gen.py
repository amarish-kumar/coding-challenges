# random input generator
# usage: gen.py [n] [no. of zeroes randomly inserted in it]

import sys
from random import randint

n = int(sys.argv[1])
z = int(sys.argv[2])

print 1
print n, 1000
rz = map(lambda _ : randint(0, n-1), range(0, z))
print ' '.join(map(str, map(lambda i : 0 if i in rz else 1, range(0, n))))

