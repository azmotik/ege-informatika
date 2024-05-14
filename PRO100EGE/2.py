from itertools import *

def f(x, y, z, w):
    return (x or not(y)) and not(y == z) and not(w)

for a in product([0, 1], repeat = 4):
    tab = [(1, 1, a[0], a[1]), (a[2], 1, 0, 0), (1, a[3], 1, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in tab] == [1, 1, 1]:
                print(p)