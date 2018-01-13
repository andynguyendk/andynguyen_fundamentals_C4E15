from turtle import *
speed(0)
color("red", "yellow")
begin_fill()
while True:
    forward(100)
    left(90)
    if abs(pos()) <10:
     break
end_fill()

mainloop()
