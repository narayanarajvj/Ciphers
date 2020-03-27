s = input("Enter a plain text: ")
k = int(input("Enter a key: "))
en = []
print("CAESAR CIPHER")
print("Encryption:")
for i in s:
    a = ord(i)
    if a == 32:
        en.append(9999)
        continue
    q = a + k
    en.append(q)

cip = ""
for val in en:
    if val == 9999:
        cip = cip + " "
        continue
    cip = cip + chr(val)
print("Cipher text: ", str(cip))

print("Decryption:")
r = int()
de = []
for v in en:
    if v == 9999:
        de.append(9999)
        continue
    r = v - k
    de.append(r)

y = ""
for j in de:
    if j == 9999:
        y = y + " "
        continue
    g = chr(j)
    y = y + g
print("Plain text: ", str(y))
