x = int(input("how many level?"))
import random
from turtle import *
shape("arrow")
speed(0)
color("black", "red")
colors  = ["red","black","blue","orange","purple","cyan"]
penup()
def draw_hex(sz):
    color(random.choice(colors))
    begin_fill()
    seth(60)
    pendown()
    for i in range(6):
        forward(sz)
        left(60)
    end_fill()
    penup()
def draw_line(x, sz):
    seth(0)
    forward(sz*x)
    for i in range(x):
        draw_square(sz)
        forward(sz)
    left(180)
    forward(sz)
    left(180)
    for i in range(x-1):
        left(90)
        forward(sz)
        draw_square(sz)
    setx(-350)
    sety(-300)

for i in range(x):
    draw_line(i, 20)

color("white", "white")
setx(-350)
sety(0)
mainloop()
