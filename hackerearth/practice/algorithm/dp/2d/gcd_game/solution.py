MAX_DEPTH = 40

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def play(a, b, turn_a, depth):
    if depth == 0 or  (a == 1 or b == 1):
        if a == 1 and b == 1:
            return 0
        else:
            if a == 1:
                r = 2
            elif b == 1:
                r = 1
            else:
                r = -1
            return r

    g = gcd(a, b)

    if turn_a:
        if g == 1:
            b -= 1
        else:
            p1, p2 = b / g, b - 1
            b = None
            for p in p1, p2:
                r = play(a, p, False, depth - 1)
                if r == -1:
                    b = p1
                elif r == 1:
                    b = p
                    break
            if b is None:
                return 2
    else:
        if g == 1:
            a -= 1
        else:
            p1, p2 = a / g, a - 1
            a = None
            for p in p1, p2:
                r = play(p, b, True, depth - 1)
                if r == -1:
                    a = p1
                if r == 2:
                    a = p
                    break
            if a is None:
                return 1

    return play(a, b, not turn_a, depth - 1)

def main():
    m = ['Draw', 'Arjit', 'Chandu Don']
    t = int(input())

    while t > 0:
        a, b = map(int, input().split())
        print(m[play(a, b, True, MAX_DEPTH)])
        t -= 1

main()
