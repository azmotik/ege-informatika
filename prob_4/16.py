def f(n):
    if n > 10000: return 42
    if n % 2 == 0: return 2 * n + f(n + 3) + f(n + 4) + f(n + 6)
    return -(n + f(n + 1) + f(n + 3))

print(f(9996) - f(9994))