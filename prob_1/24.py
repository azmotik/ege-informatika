file = open('24.txt').readline()
max_count = 0
for i in range(len(file)):
    count = 0
    count_T = 0
    for j in range(i, len(file)):
        if file[j] == 'T':
            count_T += 1
        if count_T == 101:
            max_count = max(max_count, count)
            break
        count += 1

print(max_count)
