import sys
sys.setrecursionlimit(10000)

def f(n):
    if n < 4: return 3
    if n > 3: return 3 * f(n - 3)
print(int(f(3333) / f(3300)))