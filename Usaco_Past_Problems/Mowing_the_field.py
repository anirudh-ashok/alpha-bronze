#Incomplete
read = open("shuffle.in")
n = int(read.readline())
move = []
for i in range(n):
    a, b = read.readline().split()
    b = int(b)
    move.append([a, b])

pos = []
x = 0
y = 0
for i in move:
    x_pos = 1
    y_pos = 1
    dir = 1
    if i[0] == "N":
        x_pos = 1
        dir = 0
    elif i[0] == "S":
        x_pos = -1
        dir = 0
    elif i[0] == "E":
        y_pos = 1
    else:
        y_pos = -1

    if dir == 0:
        for j in range(1, i[1] + 1, x_pos):
            x += j
            print([x,y])
            if [x, y] in pos:
                print(pos.index([x, y]), len(pos))
            pos.append([x, y])
    else:
        for j in range(1, i[1] + 1, y_pos):
            print([x, y])
            y += j
            if [x, y] in pos:
                print(pos.index([x, y]), len(pos))
            pos.append([x, y])

