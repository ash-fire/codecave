print("Enter your number")
num = int(input())
multi = 0
def primecheck(numvar):
    for i in range(2, numvar):
        if numvar % i == 0:
            return None
        
    print(numvar)

while True:
    multi += 1
    if num % multi == 0:
        primecheck(multi)        
