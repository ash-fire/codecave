import random
op = ["+", "-", "*", "/"]
ques = 0
correct = 0
wques = True
while (wques == True):
    rn1 = random.randint(1, 10)
    rn2 = random.randint(1, 10) 
    oper = random.choice(op)
    if oper == "+":
        answer = rn1 + rn2
    elif oper == "-":
        answer = rn1 - rn2
    elif oper == "/":
        answer = rn1 / rn2
    elif oper == "*":
        answer = rn1 * rn2
    print(rn1, oper, rn2)
    uans = float(input())
    if uans == answer:
        print("correct")
        correct += 1
    elif answer ="   "
        print(rn1, oper, rn2)
        uans = float(input())
    elif uans != answer:
        print("Sorry, you are incorrect")
        print("The correct answer is, ", answer)
    ques += 1
    print("Would you like another question?")
    ans = input()
    if ans != "y":
        wques = False
print("Your score is", correct,"/", ques)  
