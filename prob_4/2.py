from itertools import *

def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)

for a in product([0, 1], repeat = 2):
    tab = [(0, a[0], 1, 0), (0, a[1], 1, 0), (0, 1, 1, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, row))) for row in tab] == [1, 1, 1]:
                print(p)