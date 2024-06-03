num_c, cow_Q = input().split(" ")
num_c = int(num_c)
milktime = []
query = []
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low < high:

        mid = (high + low)//2

        if array[mid] <= x:
            low = mid + 1
            if array[mid] == x:
                return mid
        else:
            high = mid

    return high

cows = []
times = []
x = -1
for i in range(num_c):
    x += int(input())
    times.append(x)

for i in range(int(cow_Q)):
    c = int(input())
    cow = binarySearch(times, c, 0, num_c - 1)
    cows.append(cow + 1)

for i in cows:
    print(i)



