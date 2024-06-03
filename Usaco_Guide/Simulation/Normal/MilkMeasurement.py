read = open("measurement.in")
n = int(read.readline())
cows = []
for i in range(n):
    d, c, m = read.readline().split()
    d = int(d)
    m = int(m)
    cows.append([d, c, m])
cows.sort()

def comp(lis):
    return lis[1]

B = ["B", 7]
E = ["E", 7]
M = ["M", 7]
leadval = 7
leaders = ""
count = 0
for i in cows:
    d, c, m = i[0], i[1], i[2]
    if c[0] == "B":
        B[1] += m
    elif c[0] == "M":
        M[1] += m
    else:
        E[1] += m
    Tlis = [B, M, E]
    Tlis.sort(key=comp)
    for i in Tlis:
        if Tlis



print(count, file=open("measurement.out", "w"))