from turtle import *
sc = Screen()
offset = 650
sc.setup(startx=offset, starty=0)
sc.bgcolor("black")
color("white")
import random
number ="345"
numberlist = [number[i:i + 1] for i in range(0, len(number),)]
sofar= []
history = []
for i in range(0, len(number)):
    sofar.insert(i, "-")
for s in range(0, len(number)): 
    print(sofar[s], end = ' ')
turns = 10 
while turns > 0:
    if "-" in sofar:
        print("\nEnter your guess(Type history to see your previous guesses)")
        guess = input()
        if guess == "history":
            for r in range(0, len(history)):
                print(history[r])
            print("\n")
                             
        for i in range(0, len(number)):
            if guess not in numberlist and guess != "history":
                turns -= 1
                history.append(guess)
                if turns == 9:
                    ht()
                    pu()
                    setx(-200)
                    sety(-200)
                    pd()
                    setx(-100)
                elif turns == 8:
                    pu()
                    setx(-150)
                    sety(-200)
                    pd()
                    sety(200)
                elif turns == 7:
                    pu()
                    setx(-200)
                    sety(200)
                    pd()
                    setx(100)
                elif turns == 6:
                    pu()
                    setx(100)
                    sety(200)
                    pd()
                    sety(175)
                elif turns == 5:
                    head = Turtle()
                    head.shape("circle")
                    head.color("white")
                    head.shapesize(3)
                    head.pu()
                    head.setx(100)
                    head.sety(160)

                elif turns == 4:
                    pu()
                    setx(100)
                    sety(150)
                    pd()
                    sety(125)
                elif turns == 3:
                    pu()
                    setx(100)
                    sety(125)
                    pd()
                    setx(0)
                    setx(200)

                elif turns == 2:
                    pu()
                    setx(100)
                    sety(125)
                    pd()
                    sety(-50)
                elif turns == 1:
                    rt(45)
                    fd(100)
                    pu()
                    bk(100)
                elif turns == 0:
                    pd()
                    rt(90)
                    fd(100)
                    pu()
                print("You have",turns,"turns left")
                break
                
            elif guess == numberlist[i]:
                sofar[i] = guess
                history.append(guess)
                    
        for s in range(0, len(number)): 
                print(sofar[s], end=' ')
    else:
        print("\nYou won!")
        exit()
        sc.title("You won!")
        exit
print("The number is", number,"! You lost!")            
sc.title("You lost!")

