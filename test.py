from numpy import sign


s = "      +-01001234a"
zero = ord('0')
nine = ord('9')
start = False
sgn = 1
b = 0
for c in s:
    if ord(c) <= nine and ord(c) >= zero:
        b = b*10 + ord(c) - zero
        start = True
        continue
    elif start:
        break
    if c == " ":
        continue
    elif c == "+" :
        start = True
    elif c == "-":
        sgn = -1
        start = True

print(sgn * b)