n = int(input())
pulley = []
for i in range(n-1):
    x,y,z = map(int, input().split(" "))
    pulley.append([x, y, z])

pulley.sort()
count = 0
direction = 0
lis = []

for i in pulley:
    d = direction
    if count == n:
        print(direction)
        break
    if i[2] == 1:
        if direction == 1:
            direction = 0
        else:
            direction = 1
    else:
        ihu=0
    if count + 1 == n:
        print(direction)

    count += 2

        