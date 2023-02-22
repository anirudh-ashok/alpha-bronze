reps = int(input())
block_1 = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(reps):
    x = input()
    block_1.append(x)

lis = []
for i in alphabet:
    letter = 0
    letter_2 = 0
    for j in block_1:
        x,y = j.split(" ")
        if (x[i] == 0 and y[i] == len(y)) or (y[i] == 0 and x[i] == len(x)):
            letter = letter+1
        else:
            letter = letter + x.count(i)
            letter_2 = letter_2 + y.count(i)
    if letter > letter_2:
        lis.append(letter)
    elif letter < letter_2:
        lis.append(letter_2)





'''
for i in alphabet:
    count = 0
    counter = 0
    for j in block_1:
        if j == i:
            count = count+1

    lis_1.append(count)
    for j in block_2:
        if j == i:
            counter = counter+1

    lis_2.append(counter)

new_lis = []
for i in range(26):
    if lis_1[i] > lis_2[i]:
        print(lis_1[i])
    elif lis_2[i] > lis_1[i]:
        print(lis_2[i])
    elif lis_2[i] == lis_1[i] != 0:
        print(lis_2[i]+1)
    elif lis_1[i] == lis_2[i]
    else:
        print(lis_1[i])
'''