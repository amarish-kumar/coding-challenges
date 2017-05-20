from math import floor, ceil


plain = input()

l = len(plain)
sqrt = l ** 0.5
f = floor(sqrt)
c = ceil(sqrt)

for i in range(0, c):
    for j in range(i, l, c):
        print(plain[j], end='')
    print(' ', end='')
print()

