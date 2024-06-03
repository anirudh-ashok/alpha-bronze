'''
n = int(input())
num = n
count = 0
while num != int(str(num)[::-1]):
    num += int(str(num)[::-1])
    count += 1

print(count, num)
'''

lis = [1,2,3,4]
p = lis[3]
d = lis[2]
lis[3] = d
lis[2] = p
print(lis)