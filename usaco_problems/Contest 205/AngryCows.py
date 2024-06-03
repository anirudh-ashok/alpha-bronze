read = open("angry.in")
n = int(read.readline())
pos = []
for i in range(n):
    var = int(read.readline())
    pos.append(var)

pos.sort()
maxe = 0
for burst in range(1, n-1):
    ex = 1
    curr = pos[burst]
    count = 0
    for j in range(10):
        c = 0
        if burst + ex <= n-1:
            f = pos[burst+ex]
        if burst - ex >= 0:
            b = pos[burst - ex]
        if f - curr <= (ex*(ex+1))/2:
            count += 1
            c = 1
        elif curr - b <= (ex*(ex+1))/2:
            count += 1
            c = 1
        print(f, b, j, ex)
        if c == 0:
            break
        ex += 1
    if count > maxe:
        maxe = count

print(maxe)