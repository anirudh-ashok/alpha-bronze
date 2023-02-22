acorns = int(input())
ind_acorn = list(input().split(" "))
identity = list(input().split(" "))
for i in range(acorns):
    ind_acorn[i] = int(ind_acorn[i])
    identity[i] = int(identity[i])
newlis = ind_acorn[:]


def func(lis, serial):
    nlis = []
    for i in lis:
        p = serial[i - 1]
        nlis.append(p)
    return nlis


e = identity[:]
for i in range(3):
    e = func(newlis, e)

for i in e:
    print(i)

'''
def new_sequence(lis, arr):
    # Arr is the ind_acorn
    new = arr
    print(lis)
    arr.sort()
    print(new)
    for i in arr:
        var = new.index(i)
        num = lis[var]
        lis.pop(var)
        lis.insert(i, num)
        print(lis, var)


print(new_sequence(identity, ind_acorn))
'''
