read = open("lostcow.in")
acc, bes = [int(i) for i in read.readline().split()]
stan = []
bess = []
for i in range(acc):
    a, b = [int(i) for i in read.readline().split()]
    stan.append([a, b])

for i in range(bes):
    a, b = [int(i) for i in read.readline().split()]
    bess.append([a, b])

print(stan, bess)

b_count = 0
maxe = 0
for i in stan:
    r_count = 0
    b_count += i[0]
    ad = 0
    for j in range(acc):
        r_count += bess[j][0]
        if r_count >= b_count:
            ad = bess[j][1]

            break
    print(ad, i[1])
    if ad - i[1] > maxe:
        maxe = ad - i[1]

with open("lostcow.out", "w+") as f:
    print(maxe, file=f)

