from turtle import *
m = 20
tracer(0)

for i in range(2):
    fd(6*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
back(-2*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(4):
    fd(8*m)
    rt(90)
up()
for x in range(-30*m, 30*m, m):
    for y in range(-30*m, 30*m, m):
        goto(x, y)
        dot(3, 'blue')

mainloop()
