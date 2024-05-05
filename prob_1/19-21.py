#19
def f(result, step):
    if result >= 129 or step > 2:
        return step == 2
    if step % 2 != 0:
        return any([f(result + 1, step + 1), f(result * 2, step + 1)])
    return all([f(result + 1, step + 1), f(result * 2, step + 1)])


print([s for s in range(1, 129) if f(s, 0)])

#20
def f1(result, step):
    if result >= 129 or step > 3:
        return step == 3
    if step % 2 == 0:
        return any([f1(result + 1, step + 1), f1(result * 2, step + 1)])
    return all([f1(result + 1, step + 1), f1(result * 2, step + 1)])


print([s for s in range(1, 129) if f1(s, 0)])

#21
def f2(result, step):
    if result >= 129 or step > 4:
        return step == 2 or step == 4
    if step % 2 != 0:
        return any([f2(result + 1, step + 1), f2(result * 2, step + 1)])
    return all([f2(result + 1, step + 1), f2(result * 2, step + 1)])


print([s for s in range(1, 129) if f2(s, 0)])

#проверяем какой вариант исключить
def f2(result, step):
    if result >= 129 or step > 2:
        return step == 2 or step == 4
    if step % 2 != 0:
        return any([f2(result + 1, step + 1), f2(result * 2, step + 1)])
    return all([f2(result + 1, step + 1), f2(result * 2, step + 1)])


print([s for s in range(1, 129) if f2(s, 0)])