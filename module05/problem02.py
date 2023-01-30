'''
row, column = input().split(" ")
row = int(row)
column = int(column)
matrix_1 = []
for i in range(row):
    x = list((input().replace("", " ")).split(" "))
    x.pop(0)
    x.pop(column-1)
    matrix_1.append(x)
count = 0
for slist in matrix_1:
    for j in slist:
        place = slist.index(j)
        if j == "." and place == 0 and slist[place+1] == "." and slist[place+2] == ".":
            count = count + 1
            print(98)
        elif j == "." and slist[place - 1] == "#" and slist[place + 1] and slist[place + 2] == ".":
            count = count + 1

print(count)


row, column = input().split(" ")
row = int(row)
column = int(column)
matrix_1 = []
for i in range(row):
    x = list((input().replace("", " ")).split(" "))
    x.pop(0)
    x.pop(column - 1)
    matrix_1.append(x)
# Vertical clues
clues = 0
for chars in range(0, row):
    for char in range(0, column):
        if matrix_1[chars][char] == ".":
            clues = clues + 1

        else:
            continue
        print("hi")
print(clues)
'''
row, column = input().split(" ")
row = int(row)
column = int(column)
matrix_1 = []
for i in range(row):
    x = list((input().replace("", " ")).split(" "))
    x.pop(0)
    x.pop(column - 1)
    matrix_1.append(x)

# Vertical Clues
count = 0
'''
for i in matrix_1:
    ind = matrix_1.index(i)
    for j in i:
        if j == "." and matrix_1[ind+1][j] == "." and matrix_1[ind+2][j] == ".":
            if matrix_1[i].index(j) == 0 or matrix_1[ind-1][j] == "#":
                count += 1
 '''
for i in range(0, row):
    for j in range(0, column):
        print("hi")
        if matrix_1[i][j] == matrix_1[i + 1][j] == matrix_1[i + 2][j] == ".":
            if j == 0 or matrix_1[i - 1][j] == "#":
                count += 1
        else:
            continue

print(count)
