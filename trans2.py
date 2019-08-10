

print("Are you encrypting or decrypting?")
ans = input("type e for encryting, and d for decrypting")
if ans == "e":
    
    word = input('Enter your word:')
    print("Encrypting.....")
    length = len(word)
    rword=""
    while (length > 0):
        rword += word[length-1]
        length=length-1


elif ans == "d":

    word = input('Enter your word:')
    print("Decrypting.....")
    length = len(word)
    rword=""
    while (length > 0):
        rword += word[length-1]
        length=length-1

    
print(rword)







