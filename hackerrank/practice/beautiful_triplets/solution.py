
n, d = list(map(int, input().split()))
a = list(map(int, input().split()))

count = 0

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        diff = a[j] - a[i]
        if diff > d:
            break

        if diff == d:
            for k in range(j + 1, n):
                diff = a[k] -a[j]
                if diff > d:
                    break

                if diff == d:
                    count += 1
                    break
            break

print(count)

