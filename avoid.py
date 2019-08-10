from turtle import*
import random
class Ball(object):
    ball = Turtle()
    shape("circle")
    #rn1 = random.randint(1,10)
    #rn2 = random.randint(1,10)

    #x, y = 0, 0
    #xdir, ydir = rn1, rn2
    #xlimit, ylimit = window_width() /2, window_height() / 2
    



    def move(self, x, y):
        global x1, y1, xdir, ydir, sc 

        rn1 = random.randint(1,10)
        rn2 = random.randint(1,10)
        
        x1, y1 = 0, 0
        xdir, ydir = rn1, rn2
        xlimit, ylimit = window_width() /2, window_height() / 2
        
        x1 = x1 + xdir
        y1 = y1 + ydir 


        if not -xlimit < x1 < xlimit:
            xdir = -xdir
        if not -ylimit < y1 < ylimit:
            ydir = -ydir 
        turtle.goto(x1, y1)
        ontimer(move, 0)
for i in range(1, 8):
    ball = Ball()
    ball.move(x1, y1)
    time.sleep(60)
