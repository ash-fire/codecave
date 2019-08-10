from turtle import *
sc=Screen()
shape("turtle")
def keyu():
    
    fd(10)
def keyl():
   
    lt(45)
def keyr():
    
    rt(45)
def keyd():
    
    bk(10)

sc.onkey(keyu, "Up")
sc.onkey(keyl, "Left")
sc.onkey(keyr, "Right")
sc.onkey(keyd, "Down")
sc.listen()
