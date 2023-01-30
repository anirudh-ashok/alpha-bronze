'''
## Given
1. Number of nuts
2. Deviation
3. Nut sizes

## Goal
1. Find the nut size that will give max number of nuts from the nut-sizes with given deviation

## Challenge
1. Selected nut acts as the mean of the nut size
2. Accepted nuts are 1 Deviation away from the selected nut size

## Method
1. Create a function to return the number of selected nuts for a given (nut size, deviation)
2. Iterate nut-list and calculate the max-selected-nuts for given (nut size, deviation)
3. max-selected-nuts will be the answer

## Algorithm

'''

num, diff = input().split(" ")
num = int(num)
diff = int(diff)
nuts = []
for i in range(num):
    x = int(input())
    nuts.append(x)


def max_nut_calc(pivot, dev, nuts_list):
    count = 0
    high = pivot + dev
    low = pivot - dev
    for nut in nuts_list:
        g = abs(pivot-nut)
        if abs(pivot-nut) <= dev:
            print(nut)
            count = count+1
    return count


max_pivot_nuts = 0
max_nut_calc(84, 20, nuts)
'''
for pivot in nuts:
    temp = max_nut_calc(pivot, diff, nuts)
    print(f"pivot:{pivot}, count:{temp}")
    if temp > max_pivot_nuts:
        max_pivot_nuts = temp

print(max_pivot_nuts)
'''
