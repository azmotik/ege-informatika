def f(a, b, step):
    if a * b >= 123 or step > 2:
        return step == 2
    if step % 2 == 0:
        return any([f(a + 2, b, step + 1), f(a, b + 2, step + 1), f(a * 2, b, step + 1), f(a, b * 2, step + 1)])
    return all([f(a + 2, b, step + 1), f(a, b + 2, step + 1), f(a * 2, b, step + 1), f(a, b * 2, step + 1)])


print([s for s in range(1, 41) if f(3, s, 0)])

def f1(a, b, step):
    if a * b >= 123 or step > 3:
        return step == 3
    if step % 2 == 0:
        return any([f1(a + 2, b, step + 1), f1(a, b + 2, step + 1), f1(a * 2, b, step + 1), f1(a, b * 2, step + 1)])
    return all([f1(a + 2, b, step + 1), f1(a, b + 2, step + 1), f1(a * 2, b, step + 1), f1(a, b * 2, step + 1)])
print([s for s in range(1, 41) if f1(3, s, 0)])

def f2(a, b, step):
    if a * b >= 123 or step > 4:
        return step == 2 or step == 4
    if step % 2 != 0:
        return any([f2(a + 2, b, step + 1), f2(a, b + 2, step + 1), f2(a * 2, b, step + 1), f2(a, b * 2, step + 1)])
    return all([f2(a + 2, b, step + 1), f2(a, b + 2, step + 1), f2(a * 2, b, step + 1), f2(a, b * 2, step + 1)])
print([s for s in range(1, 41) if f2(3, s, 0)])

#проверяем, чтобы исключить первый ход Вани, ответ: 16
def f2(a, b, step):
    if a * b >= 123 or step > 2:
        return step == 2 or step == 4
    if step % 2 != 0:
        return any([f2(a + 2, b, step + 1), f2(a, b + 2, step + 1), f2(a * 2, b, step + 1), f2(a, b * 2, step + 1)])
    return all([f2(a + 2, b, step + 1), f2(a, b + 2, step + 1), f2(a * 2, b, step + 1), f2(a, b * 2, step + 1)])
print([s for s in range(1, 41) if f2(3, s, 0)])

