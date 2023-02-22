cows = int(input())
index_cow = list(input().split(" "))
lis = []
for i in index_cow:
    lis.append(int(i))
lis.sort(reverse=True)
print(lis)


dist = []
for i in range(1,cows):
    dist.append(-(lis[i] - lis[i-1]))

print(dist)
count = 0
for i in range(cows-2):
    if dist[i] >= dist[i+1]:
        continue
    else:
        count += 1

print(count+1)