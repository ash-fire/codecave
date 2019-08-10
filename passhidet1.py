from tkinter import *
from turtle import *
import random
import time


def callback():
    print("Welcome User!")
    sc = Screen()
    alive = True
    point = 0
    lives = 3
    ht()
    f = open('highscore.txt', 'r')
    highscore = int(f.read())
    f.close()
    print(highscore)
    bgcolor("blue")
    badmonster = "monster.gif"
    cupcake = "cupcake.gif"
    gmover = "game over.gif"
    sc.addshape(cupcake)
    sc.addshape(badmonster)
    sc.addshape(gmover)
    food = Turtle()
    snake = Turtle()
    monster = Turtle()


    shape(gmover)
    food.shape(cupcake)
    snake.shape("turtle")
    monster.shape(badmonster)
    food.color("light blue")
    snake.color("orange")
    monster.color("purple")
    monster.shapesize(2)

    snake.pu()
    monster.pu()
    snake.shapesize(2)
    food.pu()
    food.shapesize(1)
    food.setx(random.randint(-300, 300))
    food.sety(random.randint(-300, 300))


        

    def is_collided_with(a, b, c):
        return abs(a.xcor() - b.xcor()) < c  and abs(a.ycor() - b.ycor()) < c 

    def cCheck():
        global point, lives, alive
        if is_collided_with(snake, food, 25) == True:
            food.ht()
            food.setx(random.randint(-300, 300))
            food.sety(random.randint(-300, 300))
            food.st()
            point += 1
            sc.title(point)
        if is_collided_with(snake, monster, 40) == True:
            st()
            sc.title("You have been eaten by a monster !")
            snake.ht()
            food.ht()
            alive = False
            print(point)
            if point > highscore:
                f = open('highscore.txt', 'w')
                f.write(str(point))
                f.close()
            time.sleep(5)
            sc.bye()
            
            
            

    def up():
        snake.fd(50)
        is_collided_with(snake, food, 25)
        is_collided_with(snake, monster, 40)
        cCheck()
        #print(is_collided_with(snake, food))
        
    def down():
        snake.bk(10)
        is_collided_with(snake, food, 25)
        is_collided_with(snake, monster, 40)
        cCheck()
        #print(is_collided_with(snake, food))
        
    def left():
        snake.lt(90)
        is_collided_with(snake, food, 25)
        is_collided_with(snake, monster, 40)
        cCheck()
        #print(is_collided_with(snake, food))
    def right():
        snake.rt(90)
        is_collided_with(snake, food, 25)
        is_collided_with(snake, monster, 40)
        cCheck()
        
        #print(is_collided_with(snake, food))


    while (alive == True):
        sc.onkey(up, "Up")
        sc.onkey(down, "Down")
        sc.onkey(left, "Left")
        sc.onkey(right, "Right")
        sc.listen()
        monster.setx(random.randint(-300, 300))
        monster.sety(random.randint(-300, 300))





    

        
        
        







top = Tk()
L1 = Label(top, text="User Name")
L1.grid(row=0, column=0)
E1 = Entry(top, bd = 5)
E1.grid(row=0, column=1)


L1 = Label(top, text="Password")
L1.grid(row=1, column=0)
E2 = Entry(top, bd = 5, show= "*")
E2.grid(row=1, column=1)


MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=3, column=1)


top.mainloop()
