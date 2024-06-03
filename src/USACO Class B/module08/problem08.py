n, m = map(int, input().split(" "))
record = []
bess = []
for i in range(n):
    x, y = map(int, input().split(" "))
    record.append([x, y])
for i in range(m):
    x, y = map(int, input().split(" "))
    bess.append([x, y])
count = 0
for i in record:
    for j in bess:
        if i[0]*j[1]*i[1] < j[0] * i[1]*j[1]:
            count += j[1] - i[1]

print(count)