print("enter your number")
num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        exit()
print("that is prime")
    
