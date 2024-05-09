file = [int(x) for x in open('17.txt')]

count = 0
min_3 = 10000000

for i in range(2, len(file) - 3):
        s1 = file[i - 2] + file[i - 1]
        s2 = file[i] + file[i + 1]
        s3 = file[i + 2] + file[i + 3]
        if s1 > 0 and s2 > 0 and s3 > 0 and s2 > s1 and s2 > s3:
            count += 1
            min_3 = min(min_3, file[i] * file[i+1])

print(count, min_3)
