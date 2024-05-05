from itertools import *


def f(a, b, c, d):
    return (a <= b) and (b <= (not c)) and (c == (not d))


for a in product([0, 1], repeat=4):
    tab = [(1, 1, 0, a[0]), (a[1], 0, 1, 0), (1, 0, a[2], 1), (0, a[3], 0, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, row))) for row in tab] == [1, 1, 1, 1]:
                print(p)
