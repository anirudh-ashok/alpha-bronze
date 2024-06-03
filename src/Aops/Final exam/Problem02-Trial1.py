n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))

copy = cows[:]
copy.sort()
var = 0
for i in range(1, n):
    if cows[i] >= cows[i - 1]:
        continue
    var = cows[i]
    break


def bubbleSort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        return arr


x = bubbleSort([1,11,3,2,3,6,5,4,8,7,9,10,12,11])
print(x)