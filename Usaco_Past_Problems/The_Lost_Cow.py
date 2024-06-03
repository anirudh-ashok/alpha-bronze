
inFile = open("lostcow.in")
x, y = [int(i) for i in inFile.readline().split()]
dist = 0
move = 1
direction = 1
count = 0
while dist != y - x:
    dist += (direction*move)
    count += move
    move *= 2
    direction *= -1

with open("lostcow.out", "w") as outFile:
    print(count + 2, file=outFile)


'''
read = open("lostcow.in")
x, y = [int(i) for i in read.readline().split()]
dist = 0
move = 1
direction = 1
count = 0
while x != y:
    x += (direction*move)
    print(x)
    count += move
    move *= 2
    direction *= -1

with open("lostcow.out", "w") as out:
    print(count + 2, file=out)
'''