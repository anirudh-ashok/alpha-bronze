'''

'''
def best():
    n = int(input())
    lis = list(map(int, input().split()))
    counter = []
    sub = set(lis)
    for i in sub:
        done = 0
        for j in range(n-1):
            if lis[j] == i and lis[j+1] == i:
                counter.append(i)
                done = 1
                break
        if done == 1:
            continue
        curr = 0
        for j in range(n - 1):
            if lis[j] != i:
                continue
            for e in range(n):
                if e <= j:
                    continue
                nlis = lis[j:(e + 1)]
                if nlis.count(i) > len(nlis) / 2:
                    counter.append(i)
                    done = 1
                    break
            if done == 1:
                break

    counter.sort()

    '''
    counter.sort(reverse=True)
    ind = 0
    while True:
        top = counter[ind]
        if len(counter) == 1 or len(counter) < ind:
            break
        if top[0] > counter[ind+1][0]:
            top[0] += counter[ind+1][0]
            counter.pop(ind+1)
        else:
            ind += 1
    '''
    if counter == []:
        return [-1]
    return counter


t = int(input())
ans = []
for i in range(t):
    v = best()
    ans.append(v)

for i in ans:
    for j in i:
        print(j,end=" ")
    print()