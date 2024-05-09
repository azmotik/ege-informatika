from fnmatch import *

count = 0
for i in range(42, 2 * 10**8 + 1, 42):
    if fnmatch(str(i), '?2*4*0') and not fnmatch(str(i), '1*7*'):
        print(i, i // 42)
        count += 1

