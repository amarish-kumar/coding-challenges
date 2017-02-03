n = int(input())

read_n_sort = lambda : sorted(map(int, input().split()), reverse=True)
v = read_n_sort()
p = read_n_sort()

r = 'Yes' if all([vi >= pi for vi, pi in zip(v, p)]) else 'No'
print(r)
