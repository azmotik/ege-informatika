from itertools import *

def f(x, y, z, w):
    return (x and not(y)) or (y == z) or not(w)

for a in product([0, 1], repeat = 4):
    tab = [(a[0], a[1], 0, 0), (1, 0, a[2], 0), (1, 0, 1, a[3])]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
                print(p)