secret_number = 7
while (guess != secret_number):
    guess = input("What number am I thinking of? ")
    if secret_number == guess:
        print("Yay! You got it!")
    else:
        print("No, that's not it.")
    
