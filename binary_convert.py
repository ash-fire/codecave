print("Enter a  binary code.")
code = input()
bina = [code[i:i + 1] for i in range(0, len(code),)]
value = 0
for i in range(0, len(code)):
    ni = int(bina[i]) * 2**(len(code) - (i + 1))
    value = value + ni
print(code, "=" ,value)

