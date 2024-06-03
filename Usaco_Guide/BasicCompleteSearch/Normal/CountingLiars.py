'''
1. What is the problem asking?
Given N statements telling bessie's position,
'''
n = int(input())
glis = []
lis = []
gmin = 1000000000
lmax = 0
for i in range(n):
    l, num = input().split()
    num = int(num)
    if l == "G":
        glis.append(num)
        continue
    lis.append(num)

for i in glis:
    count = 0
    for j in lis:
        if i > j:
            count += 1
    maxe += min(1, )
