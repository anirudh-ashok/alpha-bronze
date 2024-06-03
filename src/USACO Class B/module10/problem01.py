n = int(input())
moves = []
for i in range(n):
    x, y = input().split(" ")
    y = int(y)
    moves.append([x, y])

pos = []
c_x = 0
c_y = 0
def checker(x, y, lis, c_y, c_x):
    if x == 0:
        for j in range(1, i[1] + 1):
            if [c_x, c_y+j] in lis:
                p = lis.index([c_x, c_y+j])
                lis.pop(p)
                lis.append([c_x, c_y+j])
                break
        return j
    elif y == 0:
        if [c_x + ]
        for e in range(1, i[1] + 1):
            if [c_x+e, c_y] in lis:
                p = lis.index([c_x+e, c_y])
                lis.pop(p)
                lis.append([c_x+e, c_y])
                break
        return e


for i in moves:
    if i[0] == "N":
        y = 1
    elif i[0] == "E":
        x = 1
    elif i[0] == "S":
        x = -1
    else:
        y = -1





print(li)