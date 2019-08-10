f=open('triv.txt')
lines=f.readlines()
correct = 0

for i in range(0, 1):
    if i % 2 == 0:
        answer= lines[i + 1]
        Ques = lines[i]
        print(Ques)
        ans = str(input())
        if ans == answer:
            print("correct")
            correct += 1
        else:
            print("incorrect")
            print("The  correct answer is", answer)

