file = open('files/24_11667.txt').readline()
count = 1
arr = [0] + [i + 1 for i in range(len(file) - 7) if file[i:i+8] == 'INFINITY'] + [len(file) - 6]
max_count = 0
for i in range(count+1, len(arr)):
    max_count = max(max_count, arr[i] + 5 - arr[i - count - 1] + 1)
print(max_count)

file = open('files/24_11241.txt').readline()
max_len = 0
count = 0
for i in range(len(file)):
    if file[i] not in 'ABCD':
        count += 1
        max_len = max(max_len, count)
    else:
        count = 0
print(max_len)
