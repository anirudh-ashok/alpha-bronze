n = int(input())
fence = []
for i in range(n):
    x, y = map(int, input().split(" "))
    fence.append([x, y])
dist = 0
fence.sort()

def esc(f1, f2):
    dist = abs(f1[1] - f2[1])
    if dist < f1[0] and dist < f2[0]:
        return dist
    else:
        return 0
used_fence = []
count = 0
cont = 0
for i in fence:
    for j in fence:
        if i == j:
            continue
        if [i, j] in used_fence or [j, i] in used_fence:
            continue
        else:
            used_fence.append([i, j])
            if esc(i, j) != 0:
                cont= esc(i, j)
            else:
                break

    count += cont
print(count)






