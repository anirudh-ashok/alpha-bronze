'''
row, column = input().split(" ")

row = int(row)
column = int(column)
lis = []
for i in range(row):
    x = list(input())
    lis.append(x)
sheesh = []
# horizontal clues
for i in lis:
    for j in range(column):
        if i[j] == "." and (j == 0 or i[j - 1] == "."):
            if j != column-1 or j != column -2:
                if i[j + 1] == i[j + 2] == ".":
                    sheesh.append([i, j])


print(sheesh)


rep = int(input())
leaderboard = []

for i in range(rep):
    e,v,x = (input().split(" "))
    e = int(e)
    x = int(x)
    leaderboard.append([e,v,x])

leaderboard.sort()
print(leaderboard)
b = 7
m = 7
e = 7
maxe = 0
count = 0
for i in leaderboard:
    var = i[1][0]
    if var == "B":
        b += i[2]
    elif var == "E":
        e += i[2]
    else:
        m += 2
    if max(b,m,e) > maxe:
        count += 1
        maxe = max(b,m,e)

print(count)
'''

reps = int(input())
block_1 = ""
block_2 = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
b_1 = []
b_2 = []
for i in range(reps):
    x,y = input().split(" ")
    b_1.append(x)
    b_2.append(y)
    block_1 = block_1 + x
    block_2 = block_2 + y


side_1 = list(block_1)
side_2 = list(block_2)
p = 0
li = []
for i in alphabet:
    if side_1.count(i) > side_2.count(i):
        print(side_1.count(i))
    elif side_1.count(i) == side_2.count(i):
        for j in b_1:
            if i in j and i in b_2[b_1.index(j)]:
                p += 1
                continue
        print(side_2.count(i)-p)
    else:
        print(side_2.count(i))