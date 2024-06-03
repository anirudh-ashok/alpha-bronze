read = open("cownomics.in")
n, diff = map(int, read.readline().split())
gem = []
for i in range(n):
    x = int(read.readline())
    gem.append(x)
maxe = 0
for i in gem:
    count = 0
    for j in gem:
        if i+diff >= j >= i:
            count += 1
    maxe = max(maxe, count)
print(maxe, file=open("diamond.out", "w"))

