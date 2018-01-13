from turtle import *
shape("turtle")
color("red", "grey")
a1 = 100
a2 = 70
begin_fill()
speed(0)
penup()
forward(100)
pendown()
while True:
    forward(a1)
    left(a2)
    if abs(pos()-(100,0)) <1:
        break
    #right(10)
penup()
setpos(0,0)
setheading(180)
forward(100)
pendown()
while True:
    forward(a1)
    right(a2+30)
    if abs(pos()-(-100,0)) <1:
        break
#right(10)
end_fill()
penup()
forward(1000)
#turn = 0
#while turn < 4:
#    forward(100)
#    left(90)
#    turn += 1
#right(60)
#turn = 0
#while turn < 4:
#    forward(100)
#    left(90)
#    turn += 1









mainloop()
