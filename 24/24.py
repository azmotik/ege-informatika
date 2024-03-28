#24_01(1)
'''file = open('24var01.txt').readline()
#file = "ABCAADDDD"
min_len = len(file)
count = 0
A_count = 0
for i in range(len(file)):
    print('step:', i, len(file))
    for tek in range(i, len(file)):
        count += 1

        if file[tek] == 'A':
            A_count += 1
        if A_count == 2024:
            min_len = min(min_len, count)
            count = 0
            A_count = 0
            break
print('1(1):', min_len)

#24_01(2)
file = open('24var01.txt').readline()
A_index = []
for i in range(len(file)):
    if file[i] == 'A':
        A_index.append(i)
min_len = len(A_index)
for i in range(len(A_index) - 2023):
    min_len = min(min_len, A_index[i+2023] - A_index[i] + 1)
print('1(2):', min_len)
'''

''' --------------------------------------------------------------------------------------- '''

#24_02
file = open('24var02.txt').readline()
A_index = []
for i in range(len(file)):
    if file[i] == 'A':
        A_index.append(i)
max_len = 0
for i in range(len(A_index) - 349):
    max_len = max(max_len, A_index[i+349] - A_index[i] + 1)
print('2:', max_len)



#24_03
file = open('24var03.txt').readline()
A_index = []
for i in range(len(file)):
    if file[i] == 'A':
        A_index.append(i)
min_len = len(A_index)
for i in range(len(A_index) - 499):
    min_len = min(min_len, A_index[i+499] - A_index[i] + 1)
print('3:', min_len)

#24_04
file = open('24var04.txt').readline()
file = file.split('E')
A_index = []
for s in file:
    for i in range(len(s)):
        if s[i] == 'A':
            A_index.append(i)
max_len = 0
for i in range(len(A_index) - 699):
    max_len = max(max_len, A_index[i+699] - A_index[i] + 1)
print('4:', max_len)

#24_05
file = open('24var05.txt').readline()
A_index = []
for i in range(len(file)):
    if file[i] == 'A':
        A_index.append(i)
max_len = 0
for i in range(len(A_index) - 2):
    max_len = max(max_len, A_index[i+2] - A_index[i] + 1)
print('5:', max_len)

#24_06
file = open('24var06.txt').readline()
A_index = []
for i in range(len(file)):
    if file[i] == 'A':
        A_index.append(i)
min_len = len(A_index)
for i in range(len(A_index) - 34):
    min_len = min(min_len, A_index[i+34] - A_index[i] + 1)
print('6:', min_len)

#24_07
file = open('24var07.txt').readline()
AB_index = []
for i in range(len(file)- 1):
    if file[i] == 'A' and file[i+1] == 'B':
        AB_index.append(i)
min_len = len(AB_index)
for i in range(len(AB_index) - 20):
    min_len = min(min_len, (AB_index[i+20] + 1) - AB_index[i] + 1)
print('7:', min_len)

#24_08
file = open('24var08.txt').readline()
AB_index = []
max_len = 0
for i in range(len(file) - 1):
    if file[i] == 'A' and file[i+1] == 'B' or file[i] == 'B' and file[i+1] == 'A':
        AB_index.append(i)
for i in range(len(AB_index) - 20):
    max_len = max(max_len, (AB_index[i+20] + 1) - AB_index[i] + 1)
print('8:', max_len)

#24_09
file = open('24var09-12.txt').readline()
count = 0
max_len = 0
for i in range(len(file) - 1):
    count+=1
    if file[i] == '0' and file[i+1] == '0':
        max_len = max(max_len, count)
        count = 0
print('9:', max_len)

#24_10
file = open('24var09-12.txt').readline()
count = 0
max_len = 0
for i in range(len(file) - 2):
    count+=1
    if file[i] == '0' and file[i+1] == '0' and file[i+2] == '0':
        max_len = max(max_len, count)
        count = 1 #т.к берем по три элемента
print('10:', max_len)
'''
#24_11(1)
file = open('24var09-12.txt').readline()
count = 0
max_len = 0
for i in range(len(file) - 1):
    count+=1
    if (file[i] == '2' and file[i+1] == '1') or (file[i] == '1' and file[i+1] == '2'):
        max_len = max(max_len, count)
        count = 0
print('11(1):', max_len)

#24_11(2)
max_len = 0
file = open('24var09-12.txt').readline()
file = file.replace('12', '1 2').replace('21', '2 1')
file = file.split()
for i in file:
    max_len = max(max_len, len(i))
print('11(2):', max_len)

#24_12
max_len = 0
file = open('24var09-12.txt').readline()
file = file.replace('12', '1 2').replace('21', '2 1').replace('31', '3 1').replace('13', '1 3')
file = file.split()
for i in file:
    max_len = max(max_len, len(i))
print('12:', max_len)

#24_13(1)
count = 0
max_len = 0
file = open('24var13-17.txt').readline()
for i in range(len(file) - 1):
    if file[i] <= file[i+1]:
        count+=1
    else:
        max_len = max(max_len, count)
        count = 1
print('13(1):', max_len)

#24_13(2)
max_len = 0
file = open('24var13-17.txt').readline()
file = file.replace('ZY', 'Z Y').replace('ZX', 'Z X').replace('YX', 'Y X')
file = file.split()
for i in file:
    max_len = max(max_len, len(i))
print('13(2):', max_len)

#24_14
max_len = 0
file = open('24var13-17.txt').readline()
file = file.replace('YZ', 'Y Z').replace('XZ', 'X Z').replace('XY', 'X Y')
file = file.split()
for i in file:
    max_len = max(max_len, len(i))
print('14:', max_len)

#24_15(1)
file = open('24var13-17.txt').readline()
count = 0
for i in file: 
    if i == 'Z':
        max_len = max(max_len, count)
        count = 0
    else:
        count+=1
print('15(1):', max_len)

#24_15(2)
file = open('24var13-17.txt').readline()
max_len = 0
file = file.split('Z')
for i in file:
    max_len = max(max_len, len(i))
print('15(2):', max_len)

#24_16
file = open('24var13-17.txt').readline()
count = 0
Z_count = 0
max_len = 0
for i in file: 
    if i == 'Z':
        Z_count += 1
    if Z_count > 1:
        max_len = max(max_len, count)
        count = 0
        Z_count = 0
    else:
        count+=1
print('16:', max_len)

#24_17(1)
file = open('24var13-17.txt').readline()
count = 0
Z_count = 0
max_len = 0
for i in file:
    count+=1 
    if i == 'Z':
        Z_count += 1
    if Z_count > 2:
        max_len = max(max_len, count)
        count = 0
        Z_count = 0
        
print('17(1):', max_len)

#24_17(2)
file = open('24var13-17.txt').readline()
file = file.split('Z')
max_len = 0
for i in range(len(file) - 2):
    max_len = max(max_len, len(file[i]) + 1 + len(file[i+1]) + 1 + len(file[i+2]))
print('17(2):', max_len)

#24_18
file = open('24var18-20.txt').readline()
count = 0
max_len = 0
for i in range(len(file) - 1):
    if file[i] == file[i+1]:
        count+=1
    else:
        max_len = max(max_len, count)
        count = 1
print('18:', max_len)

#24_19
file = open('24var18-20.txt').readline()
count = 0
max_len = 0
for i in range(len(file) - 1):
    if file[i] != file[i+1]:
        count+=1
    else:
        max_len = max(max_len, count)
        count = 1
print('19:', max_len)

#24_19
file = open('24var18-20.txt').readline()
count = 0
max_len = 0
for i in range(len(file) - 1):
    if file[i] < file[i+1]:
        count+=1
    else:
        max_len = max(max_len, count)
        count = 1
print('20:', max_len)'''