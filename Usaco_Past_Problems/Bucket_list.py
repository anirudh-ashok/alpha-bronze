counter = []
lis = [3,2,3]
n = 3
done = 0
for i in lis:
    for j in range(n-1):
        if lis[j] != i:
            continue
        for e in range(n):
            if e <= j:
                continue
            nlis = lis[j:(e+1)]
            print(nlis, j)
            if nlis.count(i) > len(nlis) / 2:
                counter.append(i)
                done = 1
                break
        if done == 1:
            break

print(counter)