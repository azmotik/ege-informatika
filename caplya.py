from turtle import *

'''m = 20
tracer(0)

for i in range(7):
    right(90)
    circle(4*m, 180)
up()
for x in range(-30*m, 30*m, m):
    for y in range(-30*m, 30*m, m):
        goto(x, y)
        dot(3, 'blue')

mainloop()'''

screensize(10000, 10000)
m = 20
tracer(0)

rt(180)
fd(3*m)
rt(90)
fd(48*m)
rt(90)
fd(3*m)
for i in range(6):
    seth(0)
    circle(-4*m, 180)
up()
for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        goto(x, y)
        dot(3, 'blue')

mainloop()