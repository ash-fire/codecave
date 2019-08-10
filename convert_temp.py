print("What scale are you starting with, c, or f?")
scale=input()
print("What is the temp?")
intemp=int(input())
if scale == "c":
    outtemp = intemp * (9/5) + 32
    print(intemp," celcius in farenhiet is",outtemp,)        
elif scale =="f":
    outtemp = (intemp - 32) * (5/9) 
    print(intemp," farenhiet in celcius is",outtemp,)
else:
    quit()
print("Thank you for using TEMP converter!")
goodbye=input()
if goodbye == "bye":
    print("See you soon!")
else:
    print("Goodbye!")
exit

    
