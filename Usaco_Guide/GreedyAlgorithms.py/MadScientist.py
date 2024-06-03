read = open("breedflip.in")
n = int(read.readline())
obj = str(read.readline())
curr = str(read.readline())
cont = 0
count = 0
for i in range(n):
    o = obj[i]
    c = curr[i]
    if o != c:
        if cont == 1:
            continue
        else:
            count += 1
            cont = 1
            continue
    cont = 0

print(count, file=open("breedflip.out", "w"))
