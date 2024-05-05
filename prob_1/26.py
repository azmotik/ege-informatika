#со второго раза
file = open('26.txt')
n = int(file.readline())
a = [[int(y) for y in x.split()] for x in file]
a.sort(key=lambda x: x[1])
min_start = 0
finish = 0
mx = 0
count = 0
for i in a:
    if finish <= i[0]:
        count += 1
        min_start = finish
        finish = i[1]
    if min_start <= i[0]:
        mx = i[1]
print(count, mx)