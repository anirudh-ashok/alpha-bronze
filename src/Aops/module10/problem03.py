n = int(input())
lis = []
for i in range(n):
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    lis.append([x,y])

lis.sort()
count = 0
for i in lis:
    if count == 0:
        count = count + i[0] + i[1]

        continue
    c = i[0] - count
    if -1 * c == -(abs(c)):
        count = c + count + i[1]

        continue
    count = count + i[1]


print(count)