from turtle import *
speed(0)
color("red", "cyan")
begin_fill()
while True:
    forward(100)
    left(120)
    if abs(pos()) <10:
     break
end_fill()

mainloop()
