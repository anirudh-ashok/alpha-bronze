n = int(input())
cow = []
for i in range(n):
    x = list(map(int, input().split(" ")))
    cow.append(x)
cp = cow[:]
maxe = 0
for i in cow:
    count = 0
    cp.remove(i)
    cp.sort()
    for j in range(len(cp) - 1):
        if cp[j][1] <= cp[j+1][0]:
            count += (cp[j][1] - cp[j][0])
        else:
            count += (cp[j][1] - cp[j][0]) - (cp[j][1] - cp[j+1][0])
    count += cp[n-2][1] - cp[n-2][0]
    cp.append(i)
    if count > maxe:
        maxe = count


print(maxe)