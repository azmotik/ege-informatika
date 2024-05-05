file = [int(x) for x in open('17.txt')]
max_arr = max([int(x) for x in open('17.txt') if int(x) % 100 == 13])
count = 0
max_sum = 0
for i in range(len(file) - 2):
    count_2 = 0
    sum = 0
    for j in range(3):
        sum += file[i + j]
        if 99 < file[i + j] < 1000:
            count_2 += 1
    if count_2 == 2 and sum <= max_arr:
        count += 1
        max_sum = max(max_sum, sum)
print(count, max_sum)
