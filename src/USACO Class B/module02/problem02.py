n = int(input())
point = []
point2 = []
for i in range(n):
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    point.append([x,y])
    point2.append([y,x])
point.sort(reverse=True)
point2.sort(reverse=True)
print(point[0], point[1])
'''
max = 0
d = 0
dist = 0

coor = coordinates[:]
for i in coordinates:
    coor.remove(i)
    print(coor)
    for j in coor:
        dist = (abs(i[0] - j[0]) * abs(i[1] - j[1]))
        if dist > d:
            d = dist
        dist = 0
    max += d
    coor.append(i)
print(max)
'''