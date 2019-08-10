from turtle import *
sc = Screen()

points = 0
sc.title(points)
pu()
setx(-380)
sety(-100)
points = 0
pd()
begin_poly()
fd(750)
rt(90)
fd(350)
fd(700)
rt(90)
fd(350)
end_poly()
g = get_poly()
register_shape("Ground", g)
sety(-400)
setx(0)
shape("Ground")
color("green")
fd(500)
ob1 = Turtle()
ob2 = Turtle()
ob3 = Turtle()
ob1.shape("circle")
ob3.shape("circle")
ob2.shape("circle")
ob1.color("yellow")
ob2.color("yellow")
ob3.color("yellow")
ob1.pu()
ob2.pu()
ob3.pu()
ob1.setx(-200)
ob1.sety(0)
ob2.setx(0)
ob2.sety(0)
ob3.setx(200)
ob3.sety(0)
doxi = "dino-rex.gif"
sc.addshape(doxi)


t = Turtle()
t.shape(doxi)
t.pu()


def is_collided_with(a, b, c):
    return abs(a.xcor() - b.xcor()) < c  and abs(a.ycor() - b.ycor()) < c

def fw():
    t.setheading(0)
    t.fd(50)
def bw():
    t.setheading(180)
    t.fd(50)
def cCheck():
    global points
    if is_collided_with(t, ob1, 25) == True:
        points += 1
        ob1.ht()
    if is_collided_with(t, ob2, 25) == True:
        points += 1
        ob2.ht()
    if is_collided_with(t, ob3, 25) == True:
        points += 1
        ob3.ht()
while (points < 4):
    sc.onkey(fw, "Right")
    sc.onkey(bw, "Left")
    sc.listen()
    cCheck()
    


    
