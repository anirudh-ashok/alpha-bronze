t = int(input())
turn_num = 10 ** 100


def func(n, lis):
    for i in range(turn_num):
        damage = 0
        for ind in range(n):
            cpos = lis[ind]
            p = ind + 1
            if ind == n - 1:
                p = 0
                npos = lis[p]
            else:
                npos = lis[p]
            if cpos <= npos:
                lis[p] = npos - cpos
                print(lis)
                continue
            if npos > 0:
                lis[p] = 0
                print(lis, cpos, npos)
                continue

        for e in range(0, n - 1):
            if e == 0 and lis[e] > 0 and lis[e + 1] == 0:
                print(lis[e], 0)
                continue
            if lis[e] > 0 and lis[e + 1] == 0 and lis[e - 1] == 0:
                print(lis[e], 1)
                continue
            damage = 1
        if damage == 0:
            break

    return lis


print(func(13, [1, 1, 4, 5, 1, 4, 1, 9, 1, 9, 8, 1, 0]))

'''
ans = []
for i in range(t):
    n = int(input())
    monsters = list(map(int, input().split()))
    remain = func(n, monsters)
    indexes = []
    count = 0
    for j in range(n):
        if remain[j] != 0:
            indexes.append(j+1)
            count += 1
    ans.append([count, indexes])

for i in ans:
    print(i[0])
    for j in i[1]:
        print(j, end=" ")
    print()
'''
