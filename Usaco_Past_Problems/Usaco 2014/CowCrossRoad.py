read = open("crossroad.in")
n = int(read.readline())
pos = []
curr_pos = []
count = 0
for i in range(n):
    var = list(map(int, read.readline().split()))
    ind = -1
    for j in range(len(curr_pos)):
        if curr_pos[j][0] == var[0]:
            ind = j
    if ind == -1:
        curr_pos.append(var)
        continue
    if curr_pos[ind][1] != var[1]:
        count += 1
        curr_pos[ind][1] = var[1]
print(count, file=open("crossroad.out", "w+"))
