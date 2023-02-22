def bubble_sort(lis):
    for i in range(len(lis) - 1):
        count_swaps = 0
        for j in range(1, len(lis) - 1):
            if lis[j] < lis[j - 1]:
                temp = lis[j - 1]
                lis[j - 1] = lis[j]
                lis[j] = temp
                count_swaps += 1
        if count_swaps == 0:
            break

def bubble_sort_abs(lis):
    for i in range(len(lis) - 1):
        count_swaps = 0
        for j in range(1, len(lis) - 1):
            if abs(lis[j]) < abs(lis[j - 1]):
                temp = lis[j - 1]
                lis[j - 1] = lis[j]
                lis[j] = temp
                count_swaps += 1
        if count_swaps == 0:
            break

L = [-6, -2, 7, 14, -17, -5, 3, 18]
bubble_sort_abs(L)
print(L)