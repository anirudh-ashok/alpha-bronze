read = open("art.in")
n = int(read.readline())
canv = []
for i in range(n):
    ln = list(map(int, read.readline()))
    canv.append(ln)

def contains(lis, val):
    for i in range(n):
        for j in range(n):
            if lis[i][j] == val:
                return True
    return False

def overlap(lis, test, overlap):
    # Find the top left and bottom right
    topi, topj, bottomi, bottomj = n, n, 0, 0
    for i in range(n):
        for j in range(n):
            if lis[i][j] == test:
                topi = min(topi, i)
                topj = min(topj, j)
                bottomi = max(bottomi, i)
                bottomj = max(bottomj, j)
    for i in range(topi, bottomi+1):
        for j in range(topj, bottomj+1):
            if lis[i][j] == overlap:
                return True
    return False

count = 0
for i in range(1, 11):
    d = 0
    for j in range(1, 11):
        if contains(canv, i) and contains(canv, j) and j != i:
            if overlap(canv, i, j):
                continue
            d = 1

    if d != 1:
        count += 1
