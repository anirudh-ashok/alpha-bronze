read = open("buckets.in")
n = 10
fire = []
lake = []
rock = []
for i in range(n):
    ln = str(read.readline())
    for j in ln:
        ind = ln.index(j)
        if j == "B":
            fire = [i, ind]

        elif j == "L":
            lake = [i, ind]

        elif j == "R":
            rock = [i, ind]


min_dist = abs(fire[0] - lake[0]) - 1 + abs(fire[1] - lake[1])

if fire[1] == lake[1]:
    min_dist = abs(fire[0] - lake[0]) - 1
    if rock[1] == fire[1]:
        min_dist += 2

elif fire[0] == lake[0]:
    min_dist = abs(fire[1] - lake[1]) - 1
    if rock[0] == fire[0]:
        min_dist += 2

print(min_dist, file=open("buckets.out", "w"))
