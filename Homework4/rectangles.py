from turtle import *
shape("triangle")
colors  = ["red", "blue","brown","yellow","grey"]
speed(0)
for i in range(5):
    color(colors[i])
    setx(100*i)
    begin_fill()
    forward(100)
    left(90)
    forward(150)
    left(90)
    forward(100)
    left(90)
    forward(150)
    end_fill()
    seth(0)
mainloop()
