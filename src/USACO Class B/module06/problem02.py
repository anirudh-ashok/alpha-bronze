n = int(input())
lis = []
for i in range(n):
    num = int(input())
    lis.append(num)
lis.pop(0)
p = []
c = 0
cp = lis[:]
for i in cp:
    if len(lis) == 1:
        print(c)
        break
    diff = i - 1
    count = i
    c += 1
    while count < lis[n-1]:
        if count in lis:
            lis.remove(count)
            count += diff


'''
for i in lis:
    if len(p) == n-1:
        print(c)
        break
    c += 1
    print(c)
    diff = i - 1
    count = i
    for j in lis:
        if j == count:
            count += diff
            p.append(j)

'''