from random import randint

from redcmd.api import maincmd, execute_commandline


max_n = 100000
max_c = 100000


@maincmd
def gen(n=None, l=None, r=None, m=None):

    print(1)

    n = randint(1, max_n) if n is None else int(n)

    max_m = min(max_n, int((n * (n - 1)) / 2))
    m = randint(0, max_m) if m is None else int(m)

    l = randint(1, max_c) if l is None else int(l)
    r = randint(1, max_c) if r is None else int(r)

    print(n, m, l, r)

    graph = dict((i, []) for i in range(1, n + 1))

    for _ in range(0, m):
        new_road = False

        while not new_road:
            s = randint(1, n)
            d = randint(1, n)

            if s == d:
                continue

            if (d in graph[s]) or (s in graph[d]):
                continue

            new_road = True
            graph[s].append(d)

            print(s, d)


execute_commandline()

