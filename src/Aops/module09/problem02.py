cows = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
num = 0


def str2list(s):
    s1 = list(s.replace("", " ").split(" "))
    s1.pop(0)
    s1.pop(len(s1) - 1)
    return s1


def func(L):
    returnValue = 0
    for i in range(len(L) - 1, 1, -1):
        print(len(L), i,i-1)
        if L[i] == L[i - 1]:
            print(L[i], L[i-1])
            L.pop(i)
            L.pop(i - 1)
            returnValue += 1
            i -= 1
    return returnValue

s
'''
def func(splice):
    count = 0
    for i in splice:
        if splice.count(i) == 1:
            count += 1
    return count

lis = []
ans = 0
for j in range(1):
    for i in range(len(cows)):
        newstr = cows[:i]+ cows[i+1:]
        ind = cows.index(cows[i]) + 1
        ill = func(cows[i:ind])
        ans = ans + ill
        if len(lis) == 26:
            break
        if cows[i] not in lis:
            lis.append(cows[i])

print(ans)

'''

'''
for i in cows:
    e = cows.index(i) + 1
    newstr = cows[0:e-1] + cows[e:]
    ind = newstr.index(i) + 2
    s = cows[e-1:ind]
    ans = ans + func(s)
    newstr = ""
'''
