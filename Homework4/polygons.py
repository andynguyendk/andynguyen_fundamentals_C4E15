from turtle import *
shape("triangle")
colors  = ["red", "blue","brown","yellow","grey"]
speed(0)
for i in range(3, 8):
    color(colors[i-3])
    for _ in range(i):
        forward(100)
        left(180-180*(i-2)/i)
    seth(0)
mainloop()
