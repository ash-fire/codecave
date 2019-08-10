import random
import time

RPS = ["Rock","Paper","Scissors"]
for mycount in [1,2,3]:
    print("Rock, Paper, Scissors, shoot!!!")
    input()
    print(random.choice(RPS))
print('How many times did you win?')
worn = int(input())
if worn >= 2:
    print("You won!!!!")
else:
    print("Sorry, you lost...")
    
    
