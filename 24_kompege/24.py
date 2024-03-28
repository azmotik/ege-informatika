'''file = open('24_12931.txt').readline()

x = 0
count = 0
max_count = 0
for i in range(len(file) - 2):
    if (file[i] == 'H' and file[i+1] == 'P' and file[i+2] == 'Y') or (file[i] == 'N' and file[i+1] == 'Y' and file[i+2] == 'P'):
        count+=1
            
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)

#1 попытка
file = open('24_11813.txt').readline()
count = 0
max_count = 0
for i in range(len(file) - 1):
    if (file[i] in 'AEIOUY' and file[i+1] not in 'AEIOUY') or (file[i+1] in 'AEIOUY' and file[i] not in 'AEIOUY'):
        count+=1
    else:
        max_count = max(max_count, count)
        count = 1
print(max_count)
#1 попытка
file = open('24_11241.txt').readline()
max_count = 0
count = 0
for i in file:
    if i not in 'ABCD':
        count+=1
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)

#1 попытка
file = open('24_10724.txt').readline()
count = 0
max_count = 0

for i in file:
    if i in '0123456789ABCDEF':
        if i != '0':
            count += 1
        else:
            if count != 0:
                count += 1
    else:
        count = 0
    max_count = max(max_count, count)

print(max_count)

#1 попытка
file = open('24_9850.txt').readline()
max_count = 0
count = 0
for i in file:
    if i not in 'LISENOK':
        count+=1
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)

#1 попытка
file = open('24_9845.txt').readline()
max_count = 0
count = 0
for i in range(len(file) - 1):
    if (file[i] in 'ABC' and file[i+1] in '89') or (file[i+1] in 'ABC' and file[i] in '89'):
        count+=1
    else:
        max_count = max(max_count, count)
        count = 1
print(max_count)

#2 попытка
file = open('24_9075.txt').readline()
max_count = 0
count = 0
arr_1 = '13579'
arr_2 = '02468'
for i in range(len(file) - 1):
    if not((file[i] in arr_1 and file[i+1] in arr_2) or (file[i+1] in arr_1 and file[i] in arr_2)):
        count+=1
    else:
        max_count = max(max_count, count)
        count = 1
print(max_count)

#1 попытка
file = open('24_8959.txt').readline()
arr = file.replace('EA', '**').replace('NPC', '***')
max_count = 0
count = 0
for i in arr:
    if i == '*':
        count +=1
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)

#3 попытка
file = open('24_8615.txt').readline()
max_count = 0
count = 0
back = 0
for i in range(len(file) - 2):
    max_count = max(max_count, i+1 - back + 1)
    if file[i] in 'ABCDEF' and file[i+1] in 'ABCDEF' and file[i+2] in 'ABCDEF':
        back = i + 1

print(max_count)

#1 попытка
file = open('24_8567.txt').readline()
max_count = 0
count = 0
back = 0
for i in range(len(file) - 2):
    max_count = max(max_count, i+1 - back + 1)
    if file[i] in 'ABCD' and file[i+1] in 'ABCD' and file[i+2] in 'ABCD':
        back = i + 1

print(max_count)

#1 попытка
file = open('24_8166.txt').readline()
max_count = 0
count = 0
for i in range(len(file) - 1):
    if file[i] in 'ABC' and file[i+1] in 'ABC':
        count+=1
    else:
        max_count = max(max_count, int(count / 2))
        count = 0
print(max_count)'''

#2 попытка
file = open('24_7723.txt').readline()
max_count = 0
count = 0
for i in range(len(file) - 2):
    if file[i] in '18' and file[i+1] in '18' and file[i+2] in 'DR':
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
    
print(max_count)