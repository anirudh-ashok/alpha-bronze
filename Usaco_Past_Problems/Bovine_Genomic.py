read = open("cownomics.in")
c, r = map(int, read.readline().split())
spot = [""]*r

plain = [""]*r
for i in range(0, c):
    lis = list(read.readline())
    lis.pop(r)
    count = 0
    for j in lis:
        spot[count] += j
        count += 1

for i in range(0, c):
    lis2 = list(read.readline())
    if len(lis2) > r:
        lis2.pop(r)
    count = 0
    for j in lis2:
        plain[count] += j
        count += 1

count = 0
for i in range(r):
    m = 0
    for j in spot[i]:
        if j in plain[i]:
            m = 0
            break
        else:
            m = 1

    if m == 0:
        continue
    count += 1


print(count, file=open("cownomics.out", "w"))
