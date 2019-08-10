from turtle import *
ht()
tur = Turtle()
tur2= Turtle()
def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10
while True:
    tur.setx(+100)
    tur2.setx(+100)
    print(is_collided_with(tur, tur2))


