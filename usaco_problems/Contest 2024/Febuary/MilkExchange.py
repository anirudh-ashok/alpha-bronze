n, m = map(int, input().split())
per = list(str(input()))
capacity = list(map(int, input().split()))
s = sum(capacity)
cp = capacity[:]


def round(lis, order):
    for i in range(n):
        mv = order[i]
        if mv == "R":
            d = 1
        else:
            d = -1
        if i == 0 and d == -1 and lis[i] > 0:
            lis[n - 1] += 1
            lis[0] -= 1
        elif i == n - 1 and d == 1 and lis[i] > 0:
            lis[0] += 1
            lis[i] -= 1
        elif lis[i] > 0:
            if d == 1:
                lis[i] -= 1
                lis[i + 1] += 1
            else:
                lis[i] -= 1
                lis[i - 1] += 1
    return lis


count = 0
for i in range(m):
    cp = round(cp, per)

for e in range(n):
    c = cp[e]
    o = capacity[e]
    if c > o:
        count += c - o
        cp[e] = o
print(s - count)
