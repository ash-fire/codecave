from turtle import*
import random

rn1 = random.randint(1,10)
rn2 = random.randint(1,10)
speed(1)
sc = Screen()
bgcolor("black")
shapesize(2)
color("white")
shape("turtle")
alive = True
def turn(x, y):
    rt(90)

x,y = 0,0
xdir, ydir = rn1, rn2
xlimit, ylimit = window_width() /2, window_height() / 2

def deathcheck():
    global x, y, xdir, ydir, sc

    x = x + xdir
    y = y + ydir 


    if not -xlimit < x < xlimit:
        alive = False
        sc.title("You lose!")
    if not -ylimit < y < ylimit:
        alive = False
        sc.title("You lose!")

while (alive == True):
    fd(100)
    onclick(turn)
    deathcheck()
sc.bye()
