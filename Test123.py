elif pas == "amala":
    f = open('balance2.txt', 'r')
    bal = int(f.read())
    f.close()
    des2 = "yes"
    while (des2 == "yes" or des2 == "y"):
        print("Press 1 to depostit, 2 to withdraw, or 3 to check your balance.")
        des=input()
        if des == "1":
            print("How much would you like to deposit?")
            num = int(input())
            bal = bal + num
        elif des == "2":
            print("How much would you like to withdraw?")
            num = int(input())
            while (bal - num < 0):
                if bal - num < 0:
                    print("You don't have enough money, please renter.")
                    num = int(input())
            bal = bal - num
        elif des == "3":
            print("Your balance is,", bal)
        print("Would you like to do more transactions?") 
        des2 = input()
        if des2 == "no" or des2 == "n":
            f = open('balance2.txt', 'w')
            f.write(str(bal))
            f.close()
            exit
elif pas == "radha":
    f = open('balance3.txt', 'r')
    bal = int(f.read())
    f.close()
    des2 = "yes"
    while (des2 == "yes" or des2 == "y"):
        print("Press 1 to depostit, 2 to withdraw, or 3 to check your balance.")
        des=input()
        if des == "1":
            print("How much would you like to deposit?")
            num = int(input())
            bal = bal + num
        elif des == "2":
            print("How much would you like to withdraw?")
            num = int(input())
            while (bal - num < 0):
                if bal - num < 0:
                    print("You don't have enough money, please renter.")
                    num = int(input())
            bal = bal - num
        elif des == "3":
            print("Your balance is,", bal)
        print("Would you like to do more transactions?") 
        des2 = input()
        if des2 == "no" or des2 == "n":
            f = open('balance3.txt', 'w')
            f.write(str(bal))
            f.close()
            exit
else:
    print("Your passward in incorrect")
