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

        if array[mid] == x:
            for i in range(mid, high):
                if array[i] != x:
                    return i - 1

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

'''
n, q = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))[::-1]
query = []
for i in range(q):
    cow = int(input())
    if cow not in arr:
        query.append(-1)
    else:
        query.append(n - arr.index(cow) - 1)

for i in query:
    print(i)
'''