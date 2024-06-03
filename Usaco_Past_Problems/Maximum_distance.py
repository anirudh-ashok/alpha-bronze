import math
n = int(input())
lis = list(map(int, input().split(" ")))
lis2 = list(map(int, input().split(" ")))
def euclid(c1, c2):
    return ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
maxe = 0
for i in range(n):
    for j in range(i+1, n):
        num = euclid([lis[i], lis2[i]], [lis[j], lis2[j]])
        if num > maxe:
            maxe = num
print(maxe)
