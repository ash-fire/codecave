print("Press R to start")
des=input()
while (des == "R"):
    print("Enter your first number.")
    n1=int(input())
    print("Please enter your operation(/,*,+,-).")
    opo=input()
    print("Now enter your second number.")
    n2=int(  input())
    if opo == "*":
        answer = n1 * n2
    elif opo == "/":
        answer = n1 / n2
    elif opo == "+":
        answer = n1 + n2
    elif opo == "-":
        answer = n1 - n2
    print("The answer is",answer,)
    print("Press R to repeat.")
    print("Press E to exit.")
    des = input()
    if des == "E":
        exit
