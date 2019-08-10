def morseword(letter):
    answer = []
    letters = ["a", "b", "c", "d," "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    code = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__.."]
    for i in range(0, 25):
        if letter == letters[i]:
            answer.append(code[i])
    for i in range(0, len(letter)):           
        print(answer[i])
