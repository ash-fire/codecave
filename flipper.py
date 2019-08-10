word = input()
print("Translating.......")
length = len(word)
rword=""
while (length > 0):
    rword += word[length-1]
    length=length-1


#rword =word[length-1] + word[length-2] + word[length-3] + word[length-4] + word[length-5]
print(rword)







