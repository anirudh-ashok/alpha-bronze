sz, pieces = map(int, input().split(" "))
og = []
ct = 0
for i in range(sz):
    x = input()
    og.append(x)
    ct += x.count("#")


shard = []
for i in range(pieces):
    s = []
    for j in range(sz):
        s.append(input())
    shard.append(s)
print(ct)

cp = shard[:]
for i in shard:
    p = 0
    for e in i:
        p += e.count("#")
    for j in cp:
        e = 0
        for a in j:
            e += a.count("#")
        if j == i:
            continue

        if p + e == ct:
            print(shard.index(i)+1, shard.index(j)+1)
            break




