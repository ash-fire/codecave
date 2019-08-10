from turtle import *
import time
sc = Screen()
pu()
sety(100)
setx(-300)
pd()
setx(300)
pu()
sety(-100)
setx(-300)
pd()
setx(300)
pu()
sety(300)
setx(-100)
pd()
sety(-300)
pu()
sety(300)
setx(100)
pd()
sety(-300)
pu()
ht()
def find_cor(x, y):
    global x1
    global y1
    x1 = x
    y1 = y
def ukey():
    s1 = Turtle()
    s1.shape("circle")
    s1.shapesize(5)
    s1.color("red")
    s1.pu()
    s1.setx(x1)
    s1.sety(y1)
    
def dkey():
    s2 = Turtle()
    s2.shape("circle")
    s2.shapesize(5)
    s2.color("blue")
    s2.pu()
    s2.setx(x1)
    s2.sety(y1)

sc.onclick(find_cor)
sc.onkey(ukey, "Up")
sc.onkey(dkey, "Down")
sc.listen()
   
 
