des = "yes"
while (des == "yes"):
    word = input()
    length = len(word)
    rword=""
    while (length > 0):
        rword += word[length-1]
        length=length-1



    print(rword)







