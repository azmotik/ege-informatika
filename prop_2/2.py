from itertools import *


def f(x, y, z, w):
    return not (y <= w) or (x == z) or not (x)


for a in product([0, 1], repeat=6):
    tab = [(0, 1, a[0], 1), (1, a[1], 0, a[2]), (a[3], 1, a[4], a[5])]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
                print(p)
