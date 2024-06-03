'''
1. What is the problem asking?
Given x, y, m bucket sizes. Find the max amount of fluid you can pour into m using only x, and y

2. Given Inputs
X, Y, M. Bucket sizes

3. Expected Output
Max amount of milk to fill into M using both x and y

4. Deriving from input?
Find var = M%X
int small = 100000000
For loop(1, var+1): temp = (M - (X*i))%Y, small = min(var, small)
print(M - small)
'''
read = open("pails.in")
X, Y, M= map(int, (read.readline()).split())
small = 10000000000
turn_num = M//X
for i in range(1, turn_num + 1):
    temp = (M - (X * i)) % Y
    small = min(temp, small)

print(M - small, file=open("pails.out", "w"))