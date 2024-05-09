from turtle import *
m = 20
tracer(0)
rt(60)
fd(4*m)
rt(120)
for i in range(4):
    fd(3*m)
    rt(240)
    fd(3*m)
    rt(120)
fd(4*m)
rt(90)
fd(8 * 3**0.5 * m)
rt(90)
fd(8*m)
up()
for x in range(-30*m, 30*m, m):
    for y in range(-30*m, 30*m, m):
        goto(x, y)
        dot(3, 'blue')

mainloop()
