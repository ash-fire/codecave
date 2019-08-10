import array as Z
n = arr.array([])
swamp = 0
swap = "true"
print("How many numbers do you want to sort?")
num = int(input())
#for w in range(0,num):
#    n[w] = 0
print("Enter ",num,"numbers")
for i in range(0, num):
    temp = int(input())
    n.append(temp)

while (swap == "true"):
    for j in range(0, num, 1):
        if n[j] <= n[j+1]:
            j = j + 1
            swamp = "false"
        else:
            swamp = n[j+1]
            n[j+1] = n[j]
            n[j] = swamp
            j = j + 1
    
