import math
n = int(input())
dancers = []
for i in range(n):
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    dancers.append([x,y])
def cartesian(x1,y1,x2,y2):
    diff = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return diff

maxe = 0
p1 = 0
p2 = 0
for i in dancers:
    for j in dancers:
        d = cartesian(i[0], i[1], j[0], j[1])
        if d > maxe:
            maxe = d
            p1 = dancers.index(i)
            p2 = dancers.index(j)

print(min(p1, p2)+1, max(p1,p2) + 1)
