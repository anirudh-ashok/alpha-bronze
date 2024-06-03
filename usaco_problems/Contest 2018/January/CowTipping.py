'''
Have to toggle the positions of cows in a rectangular fashion that
always includes the top left cow.

By example, most likely, the way to do it is to find the farthest
tipped cow from the left most cow and flip it.
'''

read = open("cowtip.in")
n = int(read.readline())
pasture = []
for i in range(n):
    row = list(map(int, list(read.readline())[:n]))
    pasture.append(row)

def done(lis):
    for i in lis:
        for j in i:
            if j == 1:
                return False
    return True


def flip(lis):
    row = 0
    col = 0
    for i in range(n):
        for j in range(n):
            if lis[i][j] == 1:
                row = i
                col = j
    # Found index of maxer
    for i in range(row, -1, -1):
        for j in range(col, -1, -1):
            if lis[i][j] == 1:
                lis[i][j] = 0
            else:
                lis[i][j] = 1
    return lis

count = 0
while done(pasture) == False:
    pasture = flip(pasture)
    count += 1

print(count, file=open("cowtip.out", "w"))

