def morseletter(letter):
    answer = 0
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    code = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", "|"]
    for i in range(0, 25):
        if letter == letters[i]:
            answer = code[i]            
    print(answer)
    
def morseword(word):
    wordlist = [word[i:i + 1] for i in range(0, len(word),)]
    answer = []
    letters = ["a", "b", "c", "d," "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    code = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__.."]
    for i in range(0, len(word)):
        wordlist[i]
        for w in range(0, 25):
            if wordlist[i] == letters[w]:
                answer.append(code[w])
    for q in range(0, len(word)):
        print(q)
        print(answer[q])
        

def morseletter2(letter):
    answer = 0
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    code = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", "|"]
    for i in range(0, 25):
        if letter == code[i]:
            answer = letters[i]            
    print(answer)
