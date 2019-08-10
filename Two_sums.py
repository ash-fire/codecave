num = []
print("Please enter four numbers")
for i in range(0,4):
    n1 = input()
    num.append(n1)
print(num)
print("Please enter your target")
target = input()
for i in range(0, 2):
    if num[i] + num[i + 1] == target:
        print("lol")
    else 
