from turtle import *

sc = Screen()

fillcolor()
speed(100)
setup( width = 800, height = 800, startx = None, starty = None) 
def square():
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    
def up():
    pu()
    setx(-window_width() / 2)
    sety(ycor() + 100)
    pd()
pu()
setx(-window_width() / 2)
sety(-window_height() / 2 + 100)
pd()
for y in(1,2,3,4,5,6,7,8):
    for x in(1,2,3,4,5,6,7,8):
        if (x + y) % 2 == 0:
            begin_fill()
            square()
            end_fill()
        else:
            square()
    up()
