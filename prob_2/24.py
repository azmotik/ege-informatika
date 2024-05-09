file = open('24.txt').readline()
min_count = len(file)
for i in range(len(file)):
    count = 0
    count_3 = 0
    for j in range(i, len(file)):
        if int(file[j], 36) % 3 == 0:
            count_3 += 1
        if count_3 == 1001:
            min_count = max(min_count, count)
            break
        count += 1

print(min_count)
