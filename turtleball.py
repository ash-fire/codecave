import turtle
import random
rn1 = random.randint(1,10)
rn2 = random.randint(1,10)
turtle.shape("circle")
#turtle.pu()
turtle.color("white")
turtle.bgcolor("black")
turtle.pu()

x,y = 0,0
xdir, ydir = rn1, rn2
xlimit, ylimit = turtle.window_width() /2, turtle.window_height() / 2

def move():
    global x, y, xdir, ydir

    x = x + xdir
    y = y + ydir 

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir

    turtle.goto(x, y)

    turtle.ontimer(move, 0)

turtle.ontimer(move, 0)
turtle.exitonclick()
