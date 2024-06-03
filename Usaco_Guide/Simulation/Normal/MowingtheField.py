read = open("mowing.in")
n = int(read.readline())
steps = []
for i in range(n):
    s, r = read.readline().split()
    r = int(r)
    steps.append([s, r])
coor = [[0,0]]
done = 0
less = 10000000000
for i in steps:
    done = 0
    d = i[0]
    mag = i[1]
    x = 0
    y = 0
    if d == "N":
        y = 1
    elif d == "E":
        x = 1
    elif d == "S":
        y = -1
    else:
        x = -1
    pos = len(coor) - 1
    for j in range(1, mag+1):
        v = coor[pos]
        s = [v[0]+(x*j), v[1]+(y*j)]
        if s in coor:
            done = 1
            less = min(less, len(coor) - coor.index(s))
        coor.append(s)

if done == 0:
    print(-1, file=open("mowing.out", "w"))
else:
    print(less, file = open("mowing.out", "w"))