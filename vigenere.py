s = input("Enter the plain text: ")
k = input("Enter the key: ")
print("VIGENERE CIPHER")
s = s.upper()
k = k.upper()
print("Entered plain text is: ", s)
en = []
ke = []

print("Encryption:")
for i in s:
    g = ord(i)
    g = g - 65
    en.append(g)
print("Plain text: ", en)

for j in k:
    h = ord(j)
    h = h - 65
    ke.append(h)
print("Key: ", ke)

if len(en) != len(ke):
    for o in range(0, len(ke)):
        ke.append(ke[o])
        if len(en) == len(ke):
            break
    print("Key after appending: ", ke)

fu = []
for l in range(0, len(en)):
    fu.append(en[l] + ke[l])
    if fu[l] > 26:
        fu[l] = fu[l] - 26
print("Cipher text: ", fu)

ki = ""
op = ""
for f in range(0, len(fu)):
    op = fu[f] + 65
    op = chr(op)
    ki = ki + op
print("Cipher text: ", str(ki))


print("Decryption:")
ty = []
for t in range(0, len(fu)):
    ty.append(fu[t] - ke[t])
    if ty[t] < 0:
        ty[t] = ty[t] + 26
print("Plain text code: ", ty)

ol = ""
jp = ""
for u in range(0, len(ty)):
    jp = ty[u] + 65
    jp = chr(jp)
    ol = ol + jp
print("Plain text: ", str(ol))
