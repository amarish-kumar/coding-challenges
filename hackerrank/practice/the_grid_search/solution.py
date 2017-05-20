import re


def solve():
    rg, cg = list(map(int, input().split()))

    grid = ''.join(input().strip() for _ in range(0, rg)) if (rg > 0 and cg > 0) else ''

    rp, cp = list(map(int, input().split()))

    if (rp == 0 or cp == 0):
        return False

    d = cg - cp

    re_expr = ('\d{%d}'%d).join(input().strip() for _ in range(0, rp))

    match = re.search(re_expr, grid)

    while True:
        if match is not None:
            if (match.start() % cg) + cp <= cg:
                return True
            else:
                next_row_start = (int(match.start() / cg) + 1) * cg
                if next_row_start >= (rg * cg):
                    break
                match = re.search(re_expr, grid[next_row_start : ])
        else:
            break
    return False
    

def main():
    t = int(input())
    for _ in range(0, t):
        r = solve()
        print('YES' if r else 'NO')


main()

