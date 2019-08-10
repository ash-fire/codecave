import turtle
from turtle import *
import random
sc = Screen()
alive = True


begin_poly()
pu()
fd(100)
rt(90)
fd(20)
rt(90)
fd(100)
rt(90)
fd(20)
rt(90)
end_poly()
ball = Turtle()
ht()
l = get_poly()
register_shape("rectangle", l)

ball.shape("circle")
ball.pu()
ball.color("white")
bgcolor("black")

sc = Screen()
paddle = Turtle()
paddle.ht()
paddle.pu()
paddle.shape("rectangle")
paddle.color("white")
paddle.rt(90)
paddle.setx(0)
paddle.sety(-300)
paddle.st()

def ukey():
    paddle.fd(100)
    
def dkey():
    bk(100)



rn1 = random.randint(1,10)
rn2 = random.randint(1,10)

x,y = 0,0
xdir, ydir = rn1, rn2
xlimit, ylimit = turtle.window_width() /2, turtle.window_height() / 2


def is_collided_with(a, b, c):
    return abs(a.xcor() - b.xcor()) < c  and abs(a.ycor() - b.ycor()) < c


def move():
    
    global x, y, xdir, ydir, sc


    x = x + xdir
    y = y + ydir 


    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir 
    
    
    ball.goto(x, y)
    ontimer(move, 0)

def cCheck():
    if is_collided_with(ball, paddle, 40):
        ydir = -ydir
        xdir = -xdir
while (alive == True):
    move()
    sc.onkey(ukey, "Right")
    sc.onkey(dkey, "Left")
    sc.listen
    cCheck()
#turtle.exitonclick()
