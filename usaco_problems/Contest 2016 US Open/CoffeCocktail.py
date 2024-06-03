n, q, x = map(int, input().split())
bars = []
for i in range(q):
    bars.append([i+1, 0])
for i in range(n):
    a, b, c = map(int, input().split())
    tcaf = float((c/100)*b)
    bars[a-1][1] += tcaf


maxe = 10000000000000000000
for i in bars:
    count = 1
    caff = i[1]
    for e in bars:
        if i[0] == e[0]:
            continue
        if caff >= x:
            break
        caff += e[1]
        count += 1

    if caff < x:
        continue
    if count < maxe:
        maxe = count

print(maxe)

