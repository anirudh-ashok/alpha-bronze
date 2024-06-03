n = int(input())
cow = []
for i in range(n):
    x, y = list((input().split(" ")))
    x = int(x)
    cow.append([x, y])
cow.sort()
on = []
count = 0
print(cow)
maxe = 0
for i in range(n):
    h = 0
    g = 0
    for j in range(i, n):

        if cow[j][1] == "H":
            h += 1
        else:
            g += 1
        #print(cow[i], cow[j], h, g)
        if h == g:
            count = abs(cow[j][0] - cow[i][0])
    if count > maxe:
        maxe = count


print(maxe)