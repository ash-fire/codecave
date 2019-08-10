import turtle
from turtle import *
import random
import threading

sc = Screen()

def movepaddle():
    global paddle
    def keyl():
        paddle.bk(50)
    def keyr():
        paddle.fd(50)
    sc.onkey(keyl, "Left")
    sc.onkey(keyr, "Right")
    sc.listen()
#def keyl():
    #paddle.bk(50)
#def keyr():
    #paddle.fd(50)
#sc.onkey(keyl, "Left")
#sc.onkey(keyr, "Right")
#sc.listen()

def move():
    global x, y, xdir, ydir, sc

    x = x + xdir
    y = y + ydir 

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir 
    elif paddle.xcor()-10 < xcor() < paddle.xcor()+10 and paddle.ycor()-10 < ycor() < paddle.ycor()+10:
        xdir = -xdir
        ydir = -ydir
    turtle.goto(x, y)
    
def turtleThread():
    global sc
    rn1 = random.randint(1,10)
    rn2 = random.randint(1,10)

    x,y = 0,0
    xdir, ydir = rn1, rn2
    xlimit, ylimit = turtle.window_width() /2, turtle.window_height() / 2
    turtle.shape("circle")
    turtle.pu()
    turtle.color("white")
    turtle.bgcolor("black")

    turtle.ontimer(move, 0)

def paddleThread():
    paddle = Turtle()
    paddle.pu()
    paddle.shape("square")
    paddle.color("white")
    paddle.setx(0)
    paddle.shapesize(5)
    paddle.sety(-ylimit - 5 )
    
    def keyl():
        paddle.bk(50)
    def keyr():
        paddle.fd(50)
    sc.onkey(keyl, "Left")
    sc.onkey(keyr, "Right")
    sc.listen()

if __name__== '__main__':    

    t1 = threading.Thread(target=turtleThread, args=())
    
#    t1 = threading.Thread(target=turtle.ontimer(move,0), args=(turtle,))
    t2 = threading.Thread(target=paddleThread, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
#turtle.exitonclick()
