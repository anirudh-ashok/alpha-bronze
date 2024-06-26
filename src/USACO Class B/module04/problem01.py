n, q = input().split(" ")
n = int(n)
q = int(q)
lis = list(input().split(" "))
arr = []
for i in lis:
    arr.append(int(i))


def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = ((high+low)//2)

        if array[mid] == x and array[mid-1] != x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

query = []
for i in range(q):
    cow = int(input())
    cow_ind = binarySearch(arr, cow, 0, len(arr)-1)
    query.append(cow_ind)

for i in query:
    print(i)