from turtle import *
import random

ht()
des = "food"
snake = Turtle()
turns = 0
points = 0
bopx = xcor() + 10
bopy = ycor() + 10
alive = True
sc = Screen()
snake.pu()
snake.shape("turtle")
snake.color("green")
snake.shapesize(2)

def up():
    snake.seth(90)
    snake.fd(100)
def down():
        snake.seth(270)
        snake.fd(100)
    def left():
        snake.seth(180)
        snake.fd(100)
    def right():
        snake.seth(0)
        snake.fd(100)
    sc.onkey(up, "Up")
    sc.onkey(down, "Down")
    sc.onkey(left, "Left")
    sc.onkey(right, "Right")
    sc.listen()

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

def maker():
    global des
    global food
    if des == "food":
        food = Turtle() 
        food.shape("circle")
        food.pu()
        food.setx(random.randint(-300, 300))
        food.sety(random.randint(-300, 300))
def eat():
    move()
    global food, points
    if is_collided_with(snake, food) == True:
        food.ht()
        points += 1
maker()
while (alive == True):
    eat()
    move()
    
    
    
     
    
    
