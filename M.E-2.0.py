import random
def Tint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
print("Hello")
print("Welcome to Masters Encrypt 2.0;or M.E 2.0")
print("An amazing way to encrypt and decrypt")
print("Are you encrypting or decrypting?")
ans = input("type e for encryting, and d for decrypting")

if ans == "e":
    ewords = []
    word = input('Enter your word/sentnce:')
    length = len(word)
    rword=""
    
    while (length > 0):
        rword += word[length-1]
        length=length-1
    wordlist = [rword[i:i + 1] for i in range(0, (len(rword)),)]
    print("Encrypting.....")
    for i in range(0, len(wordlist)):
        
        print(wordlist[i],random.randint(1,10), end=' ')

elif ans == "d":
    dlist = []
    d2list = []
    word = input('Enter your word:')
    print("Decrypting.....")
    length = len(word)
    rword=""
    while (length > 0):
        rword += word[length-1]
        length=length-1
    
    wordlist = [rword[i:i + 1] for i in range(0, (len(rword)),)]
    for i in range(0, len(wordlist)):
        if wordlist[i] != " ":
            dlist.append(wordlist[i])
    #print(dlist)
    for i in range(0, len(dlist)):
        if Tint(dlist[i]) ==  False:
            d2list.append(dlist[i])
    #print(d2list)
    for i in range(0, len(d2list)):
        print(d2list[i], end=' ')

    
            
            

    
   
    

