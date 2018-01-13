import random
from turtle import *
shape("triangle")
colors  = ["red","green","blue","orange","purple","pink","yellow"]
speed(5)
for i in range(3, 17):
    color(random.choice(colors))
    for _ in range(i):
        forward(100)
        left(180-180*(i-2)/i)
    seth(0)
mainloop()
