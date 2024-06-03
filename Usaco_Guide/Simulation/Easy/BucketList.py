'''
1. What is the Problem asking?
Given N cows with the start and end of their milking time, and the number of buckets they use in that time. Find how
many buckets FJ need if he can reuse buckets that are sitting idle

2. Given inputs
Given N. Given N cows each with Start and End of milking time and Number of Buckets used

3.Given output
How many buckets needed

4. What can you derive?
Find the total buckets. Use a for loop to iterate over every element. In that have another for loop which checks if the
i[End] var of is less than the beginning. If it is, then Total buckets -= i[buckets]

'''

read = open("blist.in")
n = int(read.readline())
total = 0
cows = []
for i in range(n):
    lis = list(map(int, read.readline().split()))
    cows.append(lis)
    total += lis[2]

for i in cows:
    et = i[1]
    bt = i[2]
    for j in cows:
        if i == j:
            continue
        sc = j[0]
        if sc >= et:
            total -= bt

print(total, file=open("blist.out", "w"))