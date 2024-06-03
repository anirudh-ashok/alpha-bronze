'''
Stratergy:
Bessie out of place. Can be either among shorter cows or among taller cows. find the number of swaps FJ has to
do to get her back to the correct pos. If there are many consecutive cows in a row she can bypass all of them
with one swap.

Solve:
Find bessies proper pos by iterating which is shorter.
if bessies curr pos is > proper pos: create lis with all nums greater than bessies proper poss all the way up
to not including bessies curr pos. Make a set of this lis
'''

read = open("outofplace.in")
n = int(read.readline())
cows = []
for i in range(n):
    cows.append(int(read.readline()))

copy = cows[:]
copy.sort()
currpos = 0
for i in range(n):
    if copy[i] == cows[i]:
        continue
    currpos = i

properpos = 0
for i in range(1, n-1):
    if cows[i-1] <= cows[currpos] <= cows[i+1]:
        properpos = i

print(copy, cows)
print(currpos, properpos)
if currpos > properpos:
    newstr = set(cows[properpos:currpos])
else:
    newstr = set(cows[currpos:properpos])
print(len(newstr), file=open("outofplace.out", "w"))
