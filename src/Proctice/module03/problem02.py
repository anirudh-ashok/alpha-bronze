n_cow, indices = input().split(" ")
n_cow = int(n_cow)
indices = int(indices)
brown_cows = []
black_cow = []
for i in range(n_cow):
    brown_cows.append(input())
for i in range(n_cow):
    black_cow.append(input())


def perm_lis(lis):
    n_lis = []
    s = ""
    for i in range(indices):
        for j in lis:
            s += j[i]
        n_lis.append(s)
        s = ""
    return n_lis


bl_cow = perm_lis(black_cow)
br_cow = perm_lis(brown_cows)

fake_count = 0
count = 0

def match(ind_1, ind_2):
    for i in ind_1:
        if i in ind_2:
            return 0
    return 1


for i in range(indices):
    if match(br_cow[i], bl_cow[i]) == 1:
        count += 1

print(count)

'''
n = int(input())
words = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    x = list(input().split(" "))
    words.append(x)

print(words)

count = 0
for i in alphabet:
    for j in words:
        w_0 = j[0].count(i)
        w_1 = j[1].count(i)
        if w_0 == w_1:
            count += w_0
            continue
        elif w_0 > w_1:
            count += w_0
            continue
        else:
            count += w_1
            continue
    print(count)
    count = 0






n = int(input())
lis = []
for i in range(n):
    p = int(input())
    lis.append(p)

x = 0
min = 3748547324836
temp = lis[:]
pars = lis[:]
for e in range(n - 1):
    for i in range(n - 1):
        temp.pop(0)
        for j in temp:
            x += j

    if min > x:
        min = x
    r = pars[0]
    pars.pop(0)
    pars.append(r)
    temp = pars[:]
    x = 0


print(min)
'''
