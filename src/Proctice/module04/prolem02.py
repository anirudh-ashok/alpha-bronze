num, diff = input().split(" ")
num = int(num)
diff = int(diff)
nuts = []
max_num = 0
count = 0
for i in range(num):
    x = int(input())
    nuts.append(x)
ls = nuts[:]

for i in nuts:
    for j in ls:
        if i+diff >= j >= i:
            count += 1
    if count > max_num:
        max_num = count
    count = 0

print(max_num)