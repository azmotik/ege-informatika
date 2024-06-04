'''P = list(range(25, 38))
Q = list(range(32, 48))
A = list(range(1, 100))

for x in range(1, 100):
    if (((x in A) and (x not in P)) <= ((x not in P) and x in Q)) == False:
        A.remove(x)

print(A)

P = list(range(12, 24))
Q = list(range(18, 30))
A = []

for x in range(1, 100):
    if ((x not in A) <= ((x in P) <= (x not in Q))) == False:
        A.append(x)

print(A)

P = list(range(25, 51))
Q = list(range(12, 37))
A = list(range(1, 100))

for x in range(1, 100):
    if (((x in P) == (x in Q)) <= (x not in A)) == False:
        A.remove(x)

print(A)'''


A = []

for x in range(-100, 100):
    if (((x in A) <= (x**2 <= 25)) and ((x**2 <= 16) <= (x in A))) == False:
        A.append(x)

print(A)