def f(start, end):
    if start > end or start == 81: return 0
    if start == end: return 1
    return f(start + int(str(start)[0]), end) + f(start + 3, end) + f(2 * start - 1, end)

print(f(42, 73) * f(73, 89))