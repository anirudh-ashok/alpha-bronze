cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
read = open("notlast.in")
n = int(read.readline())
lis = []
for i in range(7):
    l = [cows[i], 0]
    lis.append(l)
for i in range(n):
    c, n = read.readline().split()
    n = int(n)
    for j in lis:
        if c == j[0]:
            j[1] += n


def comp(a):
    return a[1]


lis.sort(key=comp)
ans = "Tie"
for i in range(7):
    if lis[i][1] > lis[0][1]:
        ans = (lis[i][0])
        break
print(ans, file=open("notlast.out", "w"))
