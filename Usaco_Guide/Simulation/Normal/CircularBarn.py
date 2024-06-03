'''
1. What is the problem asking?
Given N rooms connected to each other that can hold ri cows. Find the minimum number of distance the cows have to travel
by going through the best door

2. Given Inputs
N. N door cow capacity

3. Output
The minimum distance the cows have to travel

4. What can I derive?
Simple search and sort will solve the problem.
'''
read = open("cbarn.in")
n = int(read.readline())
room = []
for i in range(n):
    r = int(read.readline())
    room.append(r)


def sum(lis):
    count = 0
    while len(lis) != 0:
        for i in lis:
            count += i
        v = lis[0]
        lis.pop(0)
    return count


maxe = 100000000
for i in range(n):
    n_lis = room[i + 1:] + room[:i]
    var = sum(n_lis)
    maxe = min(maxe, var)
print(maxe, file=open("cbarn.out", "w"))