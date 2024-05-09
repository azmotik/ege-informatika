#19 не правильно
def f(a, b, step):
    if a + b >= 231 or step > 2:
        return step == 2
    h = [f(a + 4, b, step + 1), f(a, b + 4, step + 1), f(a * 3, b, step + 1), f(a, b * 3, step + 1)]
    if step % 2 != 0:
        return any(h)
    return any(h)


print([s for s in range(1, 217) if f(10, s, 0)])

#20
def f1(a, b, step):
    if a + b >= 231 or step > 3:
        return step == 3
    h = [f1(a + 4, b, step + 1), f1(a, b + 4, step + 1), f1(a * 3, b, step + 1), f1(a, b * 3, step + 1)]
    if step % 2 == 0:
        return any(h)
    return all(h)


print([s for s in range(1, 218) if f1(10, s, 0)])

#21
def f2(a, b, step):
    if a + b >= 231 or step > 4:
        return step == 2 or step == 4
    h = [f2(a + 4, b, step + 1), f2(a, b + 4, step + 1), f2(a * 3, b, step + 1), f2(a, b * 3, step + 1)]
    if step % 2 != 0:
        return any(h)
    return all(h)



print([s for s in range(1, 218) if f2(10, s, 0)])

