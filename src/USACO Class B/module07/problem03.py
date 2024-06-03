n, m = input().split(" ")
record = []
bessie = []
less = 76543
for i in range(int(n)):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    record.append([x, y])
    if x * y < less:
        less = x*y
        ind_1 = [x,y]
most = 0
for i in range(int(m)):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    bessie.append([x, y])
    if x*y > most:
        most = x*y
        ind = [x,y]
print(ind, ind_1)
if most > less:
    print(ind[1] - ind_1[1])
else:
    print(0)


'''
for i in record:
    r_cow = i[1] * i[0]
    for j in bessie:
        bess = j[1] * j[0]
        if bess > r_cow:
            if bess - r_cow > rs:
                rs = bess - r_cow
                max_num = j[1] - i[1]

print(max_num)'''