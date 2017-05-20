
n = int(input())

grid = [[int(c) for c in input()] for i in range (0, n)]

cavities = []

for i in range(0, n):
    if i > 0 and i < n - 1:
        for j in range(0, n):
            if j > 0 and j < n - 1:
                v = grid[i][j]
                if grid[i - 1][j] < v and grid[i + 1][j] < v and grid[i][j - 1] < v and grid[i][j + 1] < v:
                    cavities.append((i, j))

for i, j in cavities:
    grid[i][j] = 'X'

print('\n'.join(''.join(str(i) for i in row) for row in grid))

