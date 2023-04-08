rows, columns = (input()).split(" ")
columns = int(columns)
rows = int(rows)
matrix = []
for i in range(int(rows)):
    l = list(input().replace("", " ").split(" "))
    l.pop(0)
    l.pop(len(l)-1)
    matrix.append(l)
count = 0
copy = matrix[:]
for i in matrix:
    for j in range(0, columns - 1):
        if i[j] == i[j+1] == "#":
            count += 1
            p = matrix.index(i)
            copy[p][j] = "."
            copy[p][j+1] = "."


for i in range(rows - 1):
    for j in range(0, columns):
        if matrix[i][j] == matrix[i+1][j] == "#":
            count += 1
            copy[i][j] = "."
            copy[i+1][j] = "."
            continue
for i in copy:
    p = i.count("#")
    count += p



print(count)

'''
rows, columns = input().split(" ")
rows = int(rows)

puddles = []
columns = int(columns)
for i in range(rows):
    x = list(input().replace("", " ").split(" "))
    x.pop(0)
    x.pop(len(x) - 1)
    puddles.append(x)

count = 0

for i in range(0, rows-1):
    for j in range(0, columns):
        if puddles[i][j] == puddles[i + 1][j] == "#":
            count = count + 1
            puddles[i][j] = 0
            puddles[i+1][j] = 0


for j in range(0,rows):
    for i in range(0,columns):
        if i == columns-1:
            continue
        elif puddles[j][i] == puddles[j][i+1] == "#":
            count = count + 1
            puddles[j][i] = 0
            puddles[j][i + 1] = 0

for e in puddles:
    for i in e:
        if i != 0 and i != ".":
            count = count+1

print(count)

'''