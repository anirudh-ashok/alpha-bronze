alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cow = input()
code = input()

product = 1

for i in cow:
    for j in alphabet:
        if j == i:
            c = alphabet.index(j) + 1
            product = product * c
            c = 0

c_code = product % 47
product = 1
c = 0
for i in code:
    for j in alphabet:
        if j == i:
            c = alphabet.index(j) + 1
            product = product * c
            c = 0

r_code = product % 47
print(r_code, c_code)
if r_code == c_code:
    print("GO")

else:
    print("STAY")
