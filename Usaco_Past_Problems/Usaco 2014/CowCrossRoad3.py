read = open("cowqueue.in")
n = int(read.readline())
cows = []
for i in range(n):
    lis = list(map(int, read.readline().split()))
    cows.append(lis)
cows.sort()
start = 0

for i in range(n):
    curr, time = cows[i][0], cows[i][1]
    if curr >= start:
        start += curr - start + time
    else:
        start += time
    if i == n - 1:
        continue
    if cows[i + 1][0] > start:
        start += cows[i + 1][0] - start
print(start, file=open("cowqueue.out", "w"))
