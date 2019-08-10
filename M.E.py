
print("Hello")
print("Welcome to Masters Encrypt or M.E")
print("An amazing way to encrypt and decrypt")
print("Are you encrypting or decrypting?")
ans = input("type e for encryting, an d d for decrypting")
if ans == "e":
    
    word = input('Enter your word/sentnce:')
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







