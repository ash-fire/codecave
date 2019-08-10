from PyDictionary import *
from html.parser import *
rimtop = 0
dictionary=PyDictionary()
des = "yes"
while(des == "yes"):
    from turtle import *
    sc = Screen()
    offset = 650
    sc.setup(startx=offset, starty=0)
    sc.bgcolor("black")
    color("white")
    import random
    print("Easy, medium, hard")
    level = input()
    word_file="10k_words.txt"
    words = open(word_file).read().splitlines()
    wordsLower = [item.lower() for item in words]
    word = random.choice(wordsLower)
    if level == "easy":
        while(len(word) > 5):
            word = random.choice(wordsLower)
    elif level == "medium":
        while(len(word) > 8):
            word = random.choice(wordsLower)
    elif level == "hard":
        while(len(word) < 8):
            word = random.choice(wordsLower)
    definition = dictionary.meaning(word)
    if definition == None:
        while(definition == None):
            word = random.choice(wordsLower)
    wordlist = [word[i:i + 1] for i in range(0, len(word),)]
    rn1 = random.randint(0, len(word))
    sofar= []
    history = []
    for i in range(0, len(word)):
        sofar.insert(i, "-")
    for s in range(0, len(word)): 
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
            elif guess ==  "hint":
                guess = wordlist[rimtop]
                rimtop += 1
            elif guess in history:
                print("You have already guessed that please guess again>")
                guess = input()
                         
            for i in range(0, len(word)):
                if guess not in wordlist and guess != "history" and guess != "hint":
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
                
                elif guess == wordlist[i]:
                    sofar[i] = guess
                    history.append(guess)
                    
            for s in range(0, len(word)): 
                print(sofar[s], end='')
        else:
            print("\nYou won!")
            sc.title("You won!")
            print("Would you like to know the definition?")
            defo = input()
            if defo == "yes":
                print (word, "\nMeaning:", dictionary.meaning(word))
                print("Would you like to play again?")
                des = input()
            else:
                print("Would you like to play again?")
                des = input()
            if des == "yes":
                sc.clear()
                break
            elif des != "yes":
                exit()
    print("The word is", word,"! You lost!")            
    sc.title("You lost!")
    print("Would you like to know the definition?")
    defo = input()
    if defo == "yes":
        print (word, "\nMeaning:", dictionary.meaning(word))
        print("Would you like to play again?")
        des = input()
    else:
        print("Would you like to play again?")
        des = input()
        if des == "yes":
            sc.clear()

