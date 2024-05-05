#19 не правильно
def f(a, b, step):
    if a + b <= 46 or step > 2:
        return step == 2

    h = [f(a - 2, b, step + 1), f(a, b - 2, step + 1)]

    if a % 2 != 0 and b % 2 == 0:
        h += [f(a // 2 + 1, b, step + 1), f(a, b // 2, step + 1)]
    elif a % 2 == 0 and b % 2 != 0:
        h += [f(a // 2, b, step + 1), f(a, b // 2 + 1, step + 1)]
    elif a % 2 == 0 and b % 2 == 0:
        h += [f(a // 2, b, step + 1), f(a, b // 2, step + 1)]
    elif a % 2 != 0 and b % 2 != 0:
        h += [f(a // 2 + 1, b, step + 1), f(a, b // 2 + 1, step + 1)]

    if step % 2 != 0:
        return any(h)
    return all(h)


print([s for s in range(27, 1000) if f(20, s, 0)])

#20
def f1(a, b, step):
    if a + b <= 46 or step > 3:
        return step == 3

    h = [f1(a - 2, b, step + 1), f1(a, b - 2, step + 1)]

    if a % 2 != 0 and b % 2 == 0:
        h += [f1(a // 2 + 1, b, step + 1), f1(a, b // 2, step + 1)]
    elif a % 2 == 0 and b % 2 != 0:
        h += [f1(a // 2, b, step + 1), f1(a, b // 2 + 1, step + 1)]
    elif a % 2 == 0 and b % 2 == 0:
        h += [f1(a // 2, b, step + 1), f1(a, b // 2, step + 1)]
    elif a % 2 != 0 and b % 2 != 0:
        h += [f1(a // 2 + 1, b, step + 1), f1(a, b // 2 + 1, step + 1)]

    if step % 2 == 0:
        return any(h)
    return all(h)


print([s for s in range(27, 1000) if f1(20, s, 0)])

#21
def f2(a, b, step):
    if a + b <= 46 or step > 4:
        return step == 2 or step == 4

    h = [f2(a - 2, b, step + 1), f2(a, b - 2, step + 1)]

    if a % 2 != 0 and b % 2 == 0:
        h += [f2(a // 2 + 1, b, step + 1), f2(a, b // 2, step + 1)]
    elif a % 2 == 0 and b % 2 != 0:
        h += [f2(a // 2, b, step + 1), f2(a, b // 2 + 1, step + 1)]
    elif a % 2 == 0 and b % 2 == 0:
        h += [f2(a // 2, b, step + 1), f2(a, b // 2, step + 1)]
    elif a % 2 != 0 and b % 2 != 0:
        h += [f2(a // 2 + 1, b, step + 1), f2(a, b // 2 + 1, step + 1)]

    if step % 2 != 0:
        return any(h)
    return all(h)


print([s for s in range(27, 1000) if f2(20, s, 0)])

