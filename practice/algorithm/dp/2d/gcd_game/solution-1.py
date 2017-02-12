
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t

    return a

m = []

def ms(a, b, ta, r):
    m.append((a, b, ta, r))

def ml(a, b, ta):
    for sa, sb, sta, sr in m:
        if a == sa and b == sb and ta == sta:
            return sr
    return None

def choose(x, y1, y2):
    r1 = gcd(x, y1)
    r2 = gcd(x, y2)
    return y1 if r1 < r2 else y2

def predict(x, y1, y2, exp, ta, d):
    if d == 0:
        return y1 if y1 < y2 else y2
    else:
        #print("pr depth:", 1000 - d)
        pass


    if Prediction.in_progress == False:
        Prediction.in_progress = True
        Prediction.end = False
        Prediction.exp = exp

    #Prediction.in_progress = True

    if ta:
        r1 = play(y1, x, ta=ta, d=d-1, prdct=True)
        if Prediction.end == True:
            return y1
        #Prediction.in_progress = False
        #print("no win")
        return y2
        #r2 = play(y2, x, ta=ta, d=d-1, predict=True)
        #return pr(y1, y2, r1, r2, exp)
    else:
        r1 = play(x, y1, ta=ta, d=d-1, prdct=True)
        if Prediction.end == True:
            return y1
        #r2 = play(x, y2, ta=ta, d=d-1, predict=True)
        #return pr(y1, y2, r1, r2, exp)
        return y2

    #return y1 if r1 == exp else y2

def pr(v1, v2, r1, r2, exp):
    if r2 == exp:
        return v2
    elif r1 == 0:
        return v1
    elif r2 == 0:
        return v2
    else:
        return v1 if v1 < v2 else v2

class Prediction:
    result = 0
    end = False
    in_progress = False
    exp = None


def play(a, b, ta=True, d=1000, prdct=False):
    #ta = True   # turn of player a (Arjit)
    sr = ml(a, b, ta)
    if sr is not None:
        return sr
    
    while a > 1 and b > 1:
        g = gcd(a, b)
        #print("g =", g)
        if g > 1:
            if ta:
                #b = choose(a, b - 1, int(b / g))
                #b = b / g
                b = predict(a, b - 1, int(b / g), 1, False, d=d)
            else:
                #a = choose(b, a - 1, int(a / g))
                #a = a / g
                a = predict(b, a - 1, int(a / g), 2, True, d=d)
        else:
            if ta:
                b -= 1
            else:
                a -= 1

        if prdct and Prediction.end == True:
            return

        if prdct == False:
            Prediction.in_progress = False
            Prediction.end = False
            print("a =", a, "b =", b)

        ta = not ta
        

    if a == 1 and b == 1:
        r = 0
    elif a == 1:
        r = 2
    else:
        r = 1

    ms(a, b, ta, r)
    if Prediction.in_progress:
        if Prediction.exp == r:
            Prediction.end = True
        else:
            print("no win")
    return r

#print(gcd(a, b))

def main():
    m = ['Draw', 'Arjit', 'Chandu Don']
    t = int(input())

    while t > 0:
        a, b = map(int, input().split())
        print(m[play(a, b)])
        t -= 1

main()
