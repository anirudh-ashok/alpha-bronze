max_time, flowers = input().split(" ")
flowers = int(flowers)
max_time = int(max_time)
f_dist = []
p_dist = []
for i in range(flowers):
    x = int(input())
    p_dist.append(x)
print(p_dist)

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
dist = 0
bubble_sort_abs(p_dist)
prev = 0
lise = [0]
for i in p_dist:
    if dist+abs(lise[0]-i) > max_time:
        break
    else:
        dist = dist+abs(lise[0]-i)
        prev+=1
    lise.append(i)
    lise.pop(0)
print(prev)
