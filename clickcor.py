from turtle import *
sc = Screen()
def oncli(x, y):
    print(x, y)
    
sc.onclick(oncli)
sc.listen()
