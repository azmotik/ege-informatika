from turtle import *
color('black', 'red')
m = 100
speed(1000)

begin_fill()
lt(15)
for i in range(4):
    lt(30)
    fd(10*m)
    lt(60)
end_fill()
count = 0
canvas = getcanvas()
for x in range(-30*m, 30*m, m):
    for y in range(-30*m, 30*m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and '4' not in item:
            count += 1
print(count)

mainloop()
