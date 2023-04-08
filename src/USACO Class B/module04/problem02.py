num_c, cow_Q = input().split(" ")
num_c = int(num_c)
milktime = []
query = []
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1
cows = []
times = []
x = 0
for i in range(num_c):
    x += int(input())
    times.append(x-1)
print(times)




