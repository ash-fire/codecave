from turtle import *

sc = Screen()

def get_mouse_click_coor(x, y):
    player = 1
    s1 = Turtle()
    s1.shape("circle")
    s1.color("red")
    s1.pu()
    s1.setx(x)
    s1.sety(y)
    print(player)
    player = 2
    print(player)
    if  player == 2:
            s2 = Turtle()
            s2.shape("circle")
            s2.color("blue")
            s2.pu()
            s2.setx(x)
            s2.sety(y)
            player = 2
   

    #def gmcc2(x,y):
    #global player
    #s2 = Turtle()
    #s2.shape("circle")
    #s2.color("blue")
    #s2.pu()
    #s2.setx(x)
    #s2.sety(y)
    #player = 1




onscreenclick(get_mouse_click_coor)


