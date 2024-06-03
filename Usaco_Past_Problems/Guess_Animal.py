#Incomplete
read = open("lostcow.in")
n = int(read.readline())
attr = []
sig = []
for i in range(n):
    lis = list(read.readline().split())[2:]
    for j in lis:
        attr.append(j)
        if j not in sig:
            sig.append(j)
maxe = 0
for i in sig:
    ct = attr.count(i)
    if ct > maxe:
        maxe = ct
print(maxe, file=open("guess.out", "w"))
