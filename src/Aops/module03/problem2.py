x = int(input())
door = []
for i in range(x):
    e = int(input())
    door.append(e)
temp = door
for start in door:
    ind = door.index(start)
    door.pop(start)
    for j in range(x-1):
        for i in door:
            count = count+i
            if door.index(i) ==0:
                door.pop(i)
