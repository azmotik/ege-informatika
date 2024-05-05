for a in range(1, 500):
    flag = 1
    for x in range(1, 500):
        if ((x % 6 == 0 <= x % 15 != 0) or ((x + a) not in range(142, 253))) == 0:
            flag = 0
    if flag == 1:
        print(a)
        break