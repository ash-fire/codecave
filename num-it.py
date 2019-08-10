import random
import time
playing = True
i = 0
while (playing == True):
    bop = False
    rn = random.randint(1,3)
    print(rn)
    bop = True 
    anw = int(input())
    time.sleep(1)
    if bop != True:
            print("you're out")
            print("score", i)
            playing == False
    if rn == 1:
        if anw != 1:
            print("you're out")
            print("score", i)
            playing == False
        
             
    if rn == 2:
        if anw != 2:
            print("you're out")
            print("score", i)
            playing == False

    if rn == 3:
        if anw != 3:
            print("you're out")
            print("score", i)
            playing == False
            
        
    i += 1
exit()
        
