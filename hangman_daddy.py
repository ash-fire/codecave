word="amala"
lengthofword=len(word)
position=0
guess = ""
while (position < lengthofword):
    position = position + 1
    guess = guess + "-"
print(guess)
guess = ""
guessword = ""
while (guess != word):
    print("Guess a letter.")
    l1=input()
    position=0
    while (position < lengthofword):
        if l1 == word[position]:
            guess.replace(position, l1)
        else:
            guess.replace(position,"-")
        position = position + 1
    position = 0
    while (position < lengthofword):
        guessword = guessword + guess[position]
        position = position + 1
    print(guessword)
    print(guess)

