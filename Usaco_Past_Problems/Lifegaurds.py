read = open("lostcow.in")
n = int(read.readline())
gaurd = []
for i in range(n):
    x = list(map(int, read.readline().split()))
    gaurd.append(x)
gaurd.sort()
cp = gaurd[:]


def time(lis):
    dist = 0
    for i in range(n - 2):
        if lis[i][1] > lis[i + 1][0]:
            dist += lis[i + 1][1] - lis[i][0]
            m = 0
            continue
        dist += lis[i][1] - lis[i][0]
        m = 1
    if m == 0:
        return dist
    return dist + (lis[n - 2][1] - lis[n - 2][0])


maxe = 0

for i in range(n):
    gaurd.pop(i)
    var = time(gaurd)
    gaurd = cp[:]
    if var > maxe:
        maxe = var

print(maxe, file=open("lifeguards.out", "w"))
