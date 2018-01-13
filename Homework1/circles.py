from turtle import *
speed(0)
color("red", "cyan")
begin_fill()
no = 10
drawn = 0
while drawn<no:
    circle(100)
    left(360/no)
    drawn += 1
end_fill()

mainloop()
