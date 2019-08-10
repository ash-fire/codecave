from turtle import *
import random
sc = Screen()
alive = True
point = 0
ht()
bgcolor("blue")
food = Turtle()
snake = Turtle()
food.shape("circle")
snake.shape("turtle")
food.color("light blue")
snake.color("orange")
snake.pu()
snake.shapesize(2)
food.pu()
food.setx(random.randint(-300, 300))
food.sety(random.randint(-300, 300))


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 20 and abs(a.ycor() - b.ycor()) < 20

def cCheck():
    global point
    if is_collided_with(snake, food) == True:
        food.ht()
        food.setx(random.randint(-300, 300))
        food.sety(random.randint(-300, 300))
        food.st()
        point += 1
        sc.title(point)
def up():
    snake.seth(90)
    snake.fd(10)
    is_collided_with(snake, food)
    cCheck()
    #print(is_collided_with(snake, food))
    
def down():
    snake.seth(270)
    snake.fd(10)
    is_collided_with(snake, food)
    cCheck()
    #print(is_collided_with(snake, food))
    
def left():
    snake.seth(180)
    snake.fd(10)
    is_collided_with(snake, food)
    cCheck()
    #print(is_collided_with(snake, food))
def right():
    snake.seth(0)
    snake.fd(10)
    is_collided_with(snake, food)
    cCheck()
    
    #print(is_collided_with(snake, food))
sc.onkey(up, "Up")
sc.onkey(down, "Down")
sc.onkey(left, "Left")
sc.onkey(right, "Right")
sc.listen()




