import random
q = "s"
while q != "q" :
    print("Press r to role the dice")
    print("Press q at the end to quit")
    com=input()
    if com == "r":
        print(random.randint(1,6))
    else:
        print("Please try again")
        print("Press r to role the dice")
        com=input()
    q = input()
   
