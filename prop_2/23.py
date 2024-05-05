def f(start, end, command):
    if start > end: return 0
    if start == end and (command[-1] == 'A' or command[-1] == 'B'): return 1
    return f(start + 2, end, command + 'A') + f(start + 5, end, command + 'B') + f(start * 2, end, command + 'C')

print(f(8, 40, ''))