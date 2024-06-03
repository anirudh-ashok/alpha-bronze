read = open("circlecross.in")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cow = str(read.readline())

def isolate(char):
    mid = []
    count = 0
    for i in range(52):
        if cow[i] == char:
            count += 1
            mid.append(i)
        if count == 2:
            break
    return cow[mid[0]+1:mid[1]]

def sim(sub):
    temp = set(sub)
    c = 0
    for i in temp:
        if sub.count(i) == 1:
            c += 1
    return c

count = 0
for i in alphabet:
    sub = isolate(i)
    count += sim(sub)

print(int(count/2), file=open("circlecross.out", "w"))

