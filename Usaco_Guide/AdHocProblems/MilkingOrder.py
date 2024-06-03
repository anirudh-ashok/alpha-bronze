'''
Problem Statment:
Given n cows, that keep breaking out. Fj keeps counter that counts the number of days without breakout after a break out
Some days, the log is unknown, so he puts -1. Find the greatest number of breakouts, and the least.

How to:
read n
read log
minimum = (all positive integers preceeded by a -1) + 1
# This is because, all ints preceeded by a (-1) indicate there was a break out some time
maximum = Count the number of (-1) that do not have a number greater than 1 directly after

'''

read = open("taming.in")
n = int(read.readline())
log = list(map(int, read.readline().split()))
small = 1
large = 0
for i in range(1,n):
    if log[i] > 0 and log[i-1] == -1:
        small += 1

for i in range(n-1):
    if log[i] == -1:
        large += 1
        if log[i+1] > 1:
            large -= (log[i+1] - 1)

if log[n-1] == -1:
    large += 1

print(small, large, file=open("taming.out", "w"))