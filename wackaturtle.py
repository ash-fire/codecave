import random
import time
from turtle import *
q = False
sc = Screen()
print("easy, medium, hard")
level = input()
print("Press the square to pause, and the purple circle circle to quit")
color = ["blue", "purple", "orange","yellow" ]
pu()
wacks = 0
mole = 0
sleeptime = 0
shapesize(2)
shape("turtle")
pause = Turtle()
pause.ht()
pause.shape("square")
pause.shapesize(2)
pause.fillcolor("red")
pause.pu()
pause.setx(300)
pause.sety(300)
pause.st()
unpause = Turtle()
unpause.ht()
unpause.shape("triangle")
unpause.shapesize(2)
unpause.fillcolor("green")
unpause.pu()
unpause.setx(300)
unpause.sety(300)
quit = Turtle()
quit.ht()
quit.shape("circle")
quit.shapesize(2)
quit.fillcolor("purple")
quit.pu()
quit.setx(0)
quit.sety(300)
quit.st()


isplaying = True
def quiter(x,y):
    sc.bye()
def wack(x, y):
    global wacks
    wacks = wacks + 1
    fillcolor(random.choice(color))
    title("You have " + str(wacks) + " points")
    fillcolor("black")
    bgcolor(random.choice(color))
    
def unpauser(x, y):
    global isplaying
    isplaying = True
    pause.st()
    unpause.ht()    
def pauser(x, y):
    global isplaying
    isplaying = False
    pause.ht()
    unpause.st()
    print("Would you like to go to a diffrent level?")
    des = input()   
    if des == "yes": 
        print("Which level?")
        level = input()
    
sleeptime = 1
while True:
    while(isplaying == True):
        fillcolor("black")
        ht()
        setx(random.randint((-window_width()/2+100), (window_width()/2-100)))
        sety(random.randint((-window_width()/2+100), (window_width()/2-100)))
        st()
        mole = mole + 1
        onclick(wack)
        if level == "easy":
            sleeptime = 1
        elif level == "medium":
            sleeptime = 0.75
        elif level == "hard":
            sleeptime = 0.5
        time.sleep(sleeptime)
        print(wacks,"/",mole)
        pause.onclick(pauser)
            

        quit.onclick(quiter)
        
    while(isplaying == False):
        unpause.onclick(unpauser)     
        quit.onclick(quiter)
quit()
        
   
