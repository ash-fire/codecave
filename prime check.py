print("enter your number")
num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("that is not prime")
        quit()
print("that is prime")
    
