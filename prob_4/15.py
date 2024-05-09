def f(x, y):
    return (3 * x + y > a) and (y < x) and (x < 30)

for a in range(500):
    if all(f(x, y) == 0 for x in range(500) for y in range(500)):
        print(a)
        break