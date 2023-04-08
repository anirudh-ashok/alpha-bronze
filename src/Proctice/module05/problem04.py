n = int(input())
room_c = []
for i in range(n):
    room_c.append(int(input()))

copy = room_c[:]


def func(lis):
    count = 0
    cp = lis[:]
    for i in range(len(lis)):
        for j in cp:
            count += j
        cp.pop(0)
    return count

print(func([9,1,2,3]))
counter = 0
minimum = 5894083769574327863
for i in room_c:
    copy.remove(i)
    counter = func(copy)
    print(copy)
    if counter < minimum:
        minimum = counter
    counter = 0
    copy = room_c[:]
print(minimum)
'''
rep = int(input())
lis = []
for i in range(rep):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    lis.append([x, y])
# Remember, 1 == horn, 2 == grass, 3 == shears
count = 0


def func(horn, grass, shears):
    count = 0
    for j in lis:
        if j[0] == horn and j[1] == shears:
            count +=1
            continue
        elif j[0] == grass and j[1] == horn:
            count +=1
            continue
        elif j[0] == shears and j[1] == grass:
            count += 1
            continue
    return count
maxe = 0
t_1 = func(1,2,3)
t_2 = func(1,3,2)
t_3 = func(2,1,3)
t_4 = func(2,1,3)
t_5 = func(3,1,2)
t_6 = func(3,2,1)
print(max(t_1, t_2, t_3, t_4, t_5, t_6))


lines, start = input().split(" ")
lines = int(lines)
start = int(start)
reps = int(((lines * 1 / 2) * lines + 1) + start)
lis = []
for i in range(start, reps):
    last_digit = str(i)[len(str(i)) - 1]
    if last_digit == '0':
        continue
    lis.append(int(last_digit))
temp = lines
count = 0
print(lis)
'''
'''
for j in range(0, temp):
    count += j
    print(lis[count], end=" ")
    lis[count] = 0

'''
'''
for i in range(lines):
    for j in range(i,temp):
        count += j
        if lis[count] == 0:
            continue
        print(lis[count], end=" ")
        lis[count] = 0
    count = 0
    print("")

'''
