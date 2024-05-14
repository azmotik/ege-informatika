from turtle import *
m = 20
tracer(0)
for i in range(2):
    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(14*m )
lt(90)
down()
for i in range(2):
    fd(17*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-30*m, 30*m, m):
    for y in range(-30*m, 30*m, m):
        goto(x, y)
        dot(3, 'blue')

mainloop()