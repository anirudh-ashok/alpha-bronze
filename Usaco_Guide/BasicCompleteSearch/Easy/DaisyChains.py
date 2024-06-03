'''
1. What is the problem asking?
Given N flowers, find the number of combinations of them that have a number of average petals in the list

2. Given Input
Given N flowers

3. Expected Output
Number of combinations of flowers that have avg petal

4. What can be derived from input?
Given N
flowers[n]
def avgcheck(lis):
    if sum{lis} % len(lis) == 0:
        Return True
    return False
 count = 0
for i in range(n):
    for j in range(i+1, n):
        if avgcheck(flowers[i:j]) == True:
            count += 1

'''

n = int(input())
flowers = list(map(int, input().split()))
def avgcheck(lis):
    t = 0
    for i in lis:
        t += i
    if t % len(lis) == 0:
        return True
    return False

count = 0
for i in range(n):
    for j in range(i, n):
        if avgcheck(flowers[i:j]):
            count += 1

print(count)