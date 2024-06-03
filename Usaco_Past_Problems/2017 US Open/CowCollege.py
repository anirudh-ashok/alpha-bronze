'''
Problem Statement:
Given N cows who want to pay different tuitions. Find the optimal Tuition to charge so FJ can make the most money

Given Inputs:
N, and N Tuition requests

Expected Output:
Find the minimum tuition Fj can give to get the maximum amount of money

Stratergy:
TLE: Iterate through all numbers from 1 to 10,000 checking for matches. Complete Search
Sort the numbers. Iterate through subsets n, n-1, n-2,...,1 checking for most money. Every time a greater money is
achived, Take
'''

n = int(input())
requests = list(map(int, input().split()))
requests.sort()
most = 0
tuition = 0
count = 0

while count != n-1:
    money = (n-count) * requests[count]
    if money > most:
        most = money
        tuition = requests[count]
    elif money == most:
        tuition = min(tuition, requests[count])
    count += 1

print(most, tuition)




'''
Turn_num = max(requests)
for i in range(1, Turn_num+1):
    print(i)
    money = 0
    for r in requests:
        if r >= i:
            money += i
    if most == money:
        tuition = min(tuition, i)
        continue
    elif money > most:
        most = money
        tuition = i
        continue
print(most, tuition)
'''
