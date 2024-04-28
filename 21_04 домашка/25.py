from fnmatch import *

for i in range(1234, 10**10 + 1, 1234):
    if fnmatch(str(i), '4*5*6') and fnmatch(str(i), '?74*68?'):
        print(i, i // 1234)



for i in range(98591, 10**12 + 1, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        print(i, i // 98591)

