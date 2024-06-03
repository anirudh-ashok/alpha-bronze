for i in range(1):
    l, r, b = input().split()
    l = int(l)-1
    r = int(r)-1
    v = r
    copy = [1,2,3,4,5,6,7,8,9]
    for j in range(l, r):
        print(copy[j])
        copy.pop(j)
    print(v, copy)
copy = [1,2,3,3,5,6,7,8,9]
copy.pop(3)
print(copy)