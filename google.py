houses = [4, 11, 10, 1, 2, 8, 5]


def f(n):
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return n[0]
    pred_1 = 0
    pred_2 = 0
    for i in range(len(n)):
        x = pred_2
        pred_2 = max(pred_1 + n[i], pred_2)
        pred_1 = x

    return max(pred_1, pred_2)


print(f(houses))
