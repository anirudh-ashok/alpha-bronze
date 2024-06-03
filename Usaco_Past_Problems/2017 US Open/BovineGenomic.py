read = open("cownomics.in")
r, c = map(int, read.readline().split())
pcow = [""]*c
scow = [""]*c
for i in range(r):
    lis = read.readline()
    for h in range(c):
        pcow[h] += lis[h]

for i in range(r):
    lis = read.readline()
    for h in range(c):
        scow[h] += lis[h]

count = 0
for i in range(c):
    no = 0
    pr = pcow[i]
    sr = scow[i]
    for base in pr:
        if base in sr:
            no = 1
            break
    if no == 1:
        continue

    count += 1

print(count, file=open("cownomics.out", "w"))