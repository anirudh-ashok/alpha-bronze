acorn, height = input().split(" ")
height = int(height)
lis = []
acorn = int(acorn)
for i in range(acorn):
    x = int(input())
    lis.append(x)

lis.sort(reverse=True)
print(lis)
count = 0
sum = 0
while sum < height:
    sum = sum + lis[count]
    count = count + 1
print(count)