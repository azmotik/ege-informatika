for a in range(1, 200):
    count = 1
    for x in range(1, 100):
        for y in range(1, 100):
            if ((x + 2 * y < a) or (y > x) or (x > 60)) == 0:
                count = 0
    if count == 1:
        print(a)
        break