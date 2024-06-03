diff = [3, 5, 7, 9, 12]
def last(low, high, key):
    while high - low > 1:
        mid = (low+high)//2
        if diff[mid] == key:
            if diff[mid-1] == diff[mid]:
                low = mid-1
            return mid
        if diff[mid] < key:
            low = mid + 1
        elif diff[mid] > key:
            high = mid - 1
    return high
print(last(0, 5, 11))
