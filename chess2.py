from turtle import *
sc = Screen()

fillcolor()
speed(10000000000000000000000000000000)
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

def move(clicked, x, y):
    
    def ukey():
        clicked.fd(100)
    def dkey():
        clicked.bk(100)
    def lkey():
        clicked.lt(90)
    def rkey():
        clicked.rt(90)
    sc.onkey(ukey, "Up")
    sc.onkey(dkey, "Down")
    sc.onkey(lkey, "Left")
    sc.onkey(rkey, "Right")
    sc.listen()

pu()
setx(-window_width() / 2)
sety(-window_height() / 2 + 100)
pd()
for y in range(1,9):
    for x in range(1,9):
        if (x + y) % 2 == 0:
            begin_fill()
            square()
            end_fill()
        else:
            square()
    up()
whitepawn = "chess_pieces/white_pawn.gif"
sc.addshape(whitepawn)

class CP(Turtle):
    clicked = False
    def __init__(self, posx, posy):
        self.setx(posx)
        self.sety(posy)
        
    def yesno(clicked):
        if clicked == False:
            clicked = True
        if clicked == True:
            clicked = False
        
wp1 = Turtle()
wp1 = CP(-350, 250)
wp1.shape(whitepawn)






