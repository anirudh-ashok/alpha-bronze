read = open("diamond.in")
n, k = map(int, read.readline().split())
diamonds = []
for i in range(n):
    gem = int(read.readline())
    diamonds.append(gem)


maxe = 0
for pivot in diamonds:
    count = 0
    for gem in diamonds:
        if pivot <= gem <= pivot+k:
            count += 1
            continue
    if count > maxe:
        maxe = count

print(maxe, file=open("diamond.out", "w+"))