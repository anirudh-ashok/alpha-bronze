import math
n = int(input())
lis = []
count = 0
for i in range(n):
    x, y, z = map(int, input().split(" "))
    lis.append([x,y,z])

for i in lis:
    if i[0] == 0:
        lis.remove(i)
        lis.insert(0, i)
        break

def dist(x1, y1, x2, y2):
    p = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return p
cp = lis[:]
while len(lis) != 1:
    curr_wheel = lis[0]
    lis.pop(0)
    for i in lis:
        if dist(curr_wheel[0], curr_wheel[1], i[0], i[1]) == i[2] + curr_wheel[2]:
            lis.remove(i)
            lis.insert(0, i)


print(lis[0][0], lis[0][1])
