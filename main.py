import numpy as np
from numpy.linalg import inv
pi = [0,0,0,0,.00751,.00938,.00953,.04184,.12628,.15273,.1502,.18764,.19055,.08575,.03859]

def main(q=None, r = None):
    if q <= r:
        return None
    rate = .0003365384615
    fixed_cost = 3500
    penalty_cost = 23000
    cost = []
    pi = prob(q,r)
    for i in range((r-5), q+1):
        if i < 0:
            cost.append(pi[q][i] * ((q-i) * 16000 + fixed_cost + penalty_cost * (0 - i)))
        if i <= r:
            cost.append(pi[q][i] * (i * rate * 16000 + (q-i) * 16000 + fixed_cost))
        else:
            cost.append(pi[q][i] * (i * rate * 16000))
    expected_cost = sum(cost)
    return expected_cost

def prob(q,r):
    matrix = []
    base = []
    for t in range(q+1):
        if t <= (q-7):
            base.append(0)
        elif t == (q-6):
            base.append(.05)
        elif t == (q-5):
            base.append(0)
        elif t == (q-4):
            base.append(0)
        elif t == (q-3):
            base.append(.25)
        elif t == (q-2):
            base.append(.4)
        elif t == (q-1):
            base.append(.2)
        elif t == q:
            base.append(.1)
    for w in range(r+1):
        matrix.append(base)


    for k in range(r+1,q+1):
        lit = []
        for l in range(0,q+1):
            if k > r:
                if k == l:
                    lit.append(.1)
                elif k == (l+1):
                    lit.append(.2)
                elif k == (l+2):
                    lit.append(.4)
                elif k == (l+3):
                    lit.append(.25)
                elif k == (l+6):
                    lit.append(.05)
                else:
                    lit.append(0)
        matrix.append(lit)
    identity = np.identity(len(matrix))
    #print(matrix)
    M = matrix - identity
    for a in M:
        a[q] = 1
    B = inv(M)
    return B



if __name__ == '__main__':
    print(f'Q and R for 14,9: {main(14,9)}')
    print(f'What we believe to be the best: {main(14,5)}')
    p = []
    mins = 100000000
    for n in range(5,15):
        for m in range(5,15):
            if main(n,m) == None:
                pass
            else:
                p.append(main(n,m))
                if main(n,m) < mins:
                    mins = main(n,m)
                    print(n)
                    print(m)
    print(f'Minimum Expected Cost: {min(p)}')