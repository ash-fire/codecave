from turtle import *
import random
rn1 = random.randint(100, 400)
speed(1000)
while True:
        while True:
            forward(100)
            left(100)
            if abs(pos()) < 1:
                break
        
done()
