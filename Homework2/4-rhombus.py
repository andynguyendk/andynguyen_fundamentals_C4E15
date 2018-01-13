from turtle import *
shape("triangle")
speed(0)
angle = 20
for i in range(4):
    seth(i*90)
    left(angle)
    forward(100)
    right(angle*2)
    forward(100)
    right(180-angle*2)
    forward(100)
    right(angle*2)
    forward(100)
mainloop()
