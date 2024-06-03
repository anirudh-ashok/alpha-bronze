read = open("notlast.in")
n = int(read.readline())
log = [["Bessie", 0], ["Elsie", 0], ["Daisy", 0], ["Gertie", 0], ["Annabelle", 0], ["Maggie", 0], ["Henrietta", 0]]

for j in range(n):
    c, n = read.readline().split()
    n = int(n)
    for i in log:
        cow, milk = i[0], i[1]
        if cow == c:
            i[1] += n
            break

def comp(a):
    return a[1]

log.sort(key=comp)
curr = log[0][1]

for i in log:
    cow, milk = i[0], i[1]
    if milk != curr:
        print(cow, file=open("notlast.out", "w"))
        break


