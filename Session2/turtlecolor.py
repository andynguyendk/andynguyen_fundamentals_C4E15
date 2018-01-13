from turtle import *
shape("triangle")
pensize(3)
for i in range(3):
    for i in range(3):
        color("green")
        forward(10)
        color("white")
        forward(10)
    for i in range(2):
        color("red")
        forward(10)
        color("white")
        forward(10)
color("black")
mainloop()
