
n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))
DEBUG = True

def misplaced_cow(cows):
    wrong_cow = 0
    nCows = len(cows)
    for i in range(1, nCows):
        if cows[i] < cows[i-1]:
            wrong_cow = i
            break
    return wrong_cow

# Test misplaced_cow
'''
A = [1,3,4,4,5,2,6,7]
print(misplaced_cow(A))

'''
def var_swap(lis, location):
    p = lis[location]
    q = lis[location-1]
    lis[location] = q
    lis[location-1] = p
    return lis

# Test variable swapping
'''
A = [1,3,4,4,5,2,6,7]
print(var_swap(A,5))
'''

def count_swaps_1(cows,wrong_cow):
    count = 0
    nCows = len(cows)
    for i in range(nCows):
        if cows == cow_copy:
            break
        cows = var_swap(cows,wrong_cow)
        count+=1

        return (count)


def count_swaps(cows, ind):
    count = 0
    previous = 0
    E = cows[ind]
    for i in range(0,ind):
        if cows[i] > E:

            if previous != cows[i]:
                if DEBUG:
                    print(f"Cows[i]: {cows[i]}, E: {E}")
                count += 1
                previous = cows[i]

    return (count)

# Testing count swaps
'''
A = [1,3,4,4,5,2,6,7]
print(count_swaps(A,5))
'''


w_cow = misplaced_cow(cows)
if DEBUG:
    print("W_cow:", w_cow)
num_swaps = count_swaps(cows, w_cow)
print(num_swaps)
