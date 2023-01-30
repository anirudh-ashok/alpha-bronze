N, M = input().split(" ")
n = int(N)
m = int(M)
lis = []
for i in range(m):
    x = int(input())
    lis.append(x)

max_1 = 0
count = 0
price = 0
for j in lis:
    for l in lis:
        if j <= l:
            count = count+1
    if count*j > max_1 and count <= n:
        max_1 = count * j
        price = j
    count = 0


print(price, max_1)

'''
    elif count*j == max_1 and count <= n:
        if j < price:
            price = j
            max_1 = count*j
    count = 0
'''