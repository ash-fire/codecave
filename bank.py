from tkinter import *



    


top = Tk()
L1 = Label(top, text="User Name")
L1.grid(row=0, column=0)
El = Entry(top, bd = 5)
El.grid(row=0, column=1)
E1 = El


def callback():
    global E1
    print(E1)
    if E1 == "ashwin":
        f = open('balance.txt', 'r')
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
                f = open('balance.txt', 'w')
                f.write(str(bal))
                f.close()
            exit
    elif E1 == "amala":
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


L1 = Label(top, text="Password")
L1.grid(row=1, column=0)
E2 = Entry(top, bd = 5, show= "*")
E2.grid(row=1, column=1)


MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=3, column=1)



top.mainloop()
