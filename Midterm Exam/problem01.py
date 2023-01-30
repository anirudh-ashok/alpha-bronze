x, y = input().split(" ")
x = int(x)
y = int(y)
lis = []
for i in range(x, y + 1):
    i = str(i)
    for letter in i:
        lis.append(letter)
lis2 = lis

count = 0
for e in range(0, 10):
    for i in lis2:
        if int(i) == e:
            count = count + 1
    print(count, end=" ")
    count = 0
'''
x, y = input().split(" ")
x = int(x)
y = int(y)
lis = []
for i in range(x, y + 1):
    i = str(i)
    for letter in i:
        lis.append(letter)
lis2 = []
for j in lis:
    lis2.append(int(j))

lis2.sort()

count = 0
for e in range(0, 10):
    for i in lis2:
        if i == e:
            count = count + 1
    print(count, end=" ")
    count = 0

'''