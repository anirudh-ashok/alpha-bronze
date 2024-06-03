'''
1. What is the problem asking?
Given N diamonds and a variation factor. Find the maximum number of diamonds that vary in size less than or equal to the
variation factor

2. Given Input
Given N diamonds, and K required variation

3. Expected Output
Number of diamonds with vary at max K from each other

4. What can You derive?
Read n, K
diamonds[n]
gnum = 0
For Loop i (Diamonds):
    count = -1
    For Loop j (Diamonds):
        If I < j < I + K: count += 1
    gnum = max(gnum, count)

'''

read = open("diamond.in")
n, k = map(int, read.readline().split())
gems= []
for i in range(n):
    var = int(read.readline())
    gems.append(var)
gnum = 0
for gem in gems:
    count = 0
    for i in gems:
        if gem <= i <= gem+k:
            count += 1
    gnum = max(gnum, count)
print(gnum, file=open("diamond.out", "w"))