n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))

copy = cows[:]
copy.sort()
var = 0
for i in range(1, n):
    if cows[i] >= cows[i-1]:
        continue
    var = cows[i]
    break

print(cows)
print(copy)


def bubbleSort(arr):
    count = 0
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if not swapped:
            return
    return count

x = bubbleSort(cows)

def swap_ele_1(lis, variable):
    location = lis.index(variable)
    p = lis[location]
    q = lis[location-1]
    lis[location] = q
    lis[location-1] = p
    return lis

def swap_ele_2(lis, variable):
    location = lis.index(variable)
    p = lis[location]
    q = lis[location+1]
    lis[location] = q
    lis[location+1] = p
    return lis

count = 0
for i in range(len(cows)):
    pos = cows.index(var)
    if var < cows[pos-1]:
        cows = swap_ele_1(cows, var)
        count += 1
counte = 0
for i in range(len(cows)):
    pos = cows.index(var)
    if var > cows[pos+1]:
        cows = swap_ele_2(cows, var)
        counte += 1

if counte < count:
    print(counte)
else:
    print(count)
'''
count = 0
for i in range(7):
    count += 1
    pos = cows.index(var)
    if var < cows[pos-1]:
        if pos >= 2 and cows[pos-1] == cows[pos-2]:
            cows = swap_ele_2(cows, var)
            continue
        else:
            cows = swap_ele_1(cows, var)
print(cows)
print(copy)

n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))
copy = cows[:]
copy.sort()
#finding the bad item
for i in range(1, n):
    if cows[i] >= cows[i-1]:
        continue
    var = cows[i]
    break
print(var)

# Check if the two elements before it are greater and or equal
count = 0
for i in range(6):

    if cows == copy:
        break
    place = cows.index(var)
    if var < cows[place-1]:
        if place >=2 and cows[i-1] == cows[i-2]:
            temp = cows[place-2]
            cows[place-2] = var
            cows[place] = temp
        else:
            tem = cows[place - 1]
            cows[place - 1] = var
            cows[place] = tem
print(cows)
print(copy)
'''