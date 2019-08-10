import random
bulls = 0
cows = 0
number = random.randint(100, 1000)
nlist = [str(number)[i:i + 1] for i in range(0, 3,)]
while (bulls != 3):
    print("Please enter a three digit number")
    guess = input()
    glist = [str(guess)[i:i + 1] for i in range(0, 3,)]
    for i in range(0, 3):
        if glist[i] == nlist[i]:
            bulls += 1
        elif glist[i] != nlist[i]:
            if glist[i] == nlist[i + 1]:
                cows += 1
            if glist[i] == nlist[i + 2]:
                cows += 1

    print(bulls,"bull(s)",cows,"cow(s)")
print("Yay!!! You won! The number was", number)


