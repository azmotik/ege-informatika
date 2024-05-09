file = [int(x) for x in open('17.txt')]
max_arr = max([int(x) for x in open('17.txt') if abs(int(x)) % 100 == 18])
max_sum = 0
count = 0
for i in range(len(file) - 2):
    count_3 = 0
    summ = 0
    for j in range(3):
        summ += file[i + j]
        if '3' in str(file[i + j]):
            count_3 += 1
    if count_3 <= 2 and summ <= max_arr:
        count += 1
        max_sum = max(max_sum, summ)
print(count, max_sum)



