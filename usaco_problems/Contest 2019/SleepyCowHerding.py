# Given 3 cows. Can only move the cow at the greatest position or cow at least position.
# find out the minimum and maximum moves to make so all cows can be in a consecutive position.
# My implement: Max has to be 2 all the time
# Min is Either 1 or two. Check if diff between middle and lowest  ==  2 or middle and highest == 2: if so
# output 1, else output 2
read = open("herding.in")
lis = list(map(int, read.readline().split()))
lis.sort()
low = lis[0]
mid = lis[1]
high = lis[2]
if mid - low == 2 or high - mid == 2:
    print(1, file=open("herding.out", "a"))
else:
    print(2, file=open("herding.out", "a"))
print(2, file=open("herding.out", "a"))
