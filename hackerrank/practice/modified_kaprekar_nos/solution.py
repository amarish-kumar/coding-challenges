
p = int(input())
q = int(input())

def cd(n):
    c = 0
    while n > 0:
        n = int(n / 10)
        c += 1
    return c


found = False

for i in range(p, q + 1):
    sq = i * i
    c = cd(i)
    #print('cd', c)
    #print('sq', sq)

    l = int(sq / (10 ** c))
    r = sq - (l * (10 ** c))

    #print(l, r)

    if (l + r == i):
        print(i, end=' ')
        found = True

if not found:
    print('INVALID RANGE')

