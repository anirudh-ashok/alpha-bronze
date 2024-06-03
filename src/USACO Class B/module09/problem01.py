diag = ["", ""]
row = []
col = ["", "", ""]
count = 2
for i in range(3):
    n = input()
    row.append(n)
    col[0] += n[0]
    col[1] += n[1]
    col[2] += n[2]
    diag[0] += n[i]
    diag[1] += n[count]
    count -= 1
pair = 0
actual = 0
lis = diag + row + col


ind = []
'''def check(ind, s):
    count = 0
    for i in ind:
        for j in i:
            if i[0] != i[1] or i[0] != i[1] or i[1] != i[2]:
                if j in s:
                    count += 1
        if count >=2:
            return True

    return False
'''
def check(ind, s):
    for i in ind:
        count = 0
        if i == s:
            return True

    return False


for i in lis:
    if i[0] == i[1] == i[2]:
        if i not in ind:
            ind.append(i)
            actual += 1
        continue
    elif i[0] == i[1]:
        if check(ind, i) == False:
            ind.append(i)
            pair += 1
        continue
    elif i[0] == i[2]:
        x = i[0] + i[0] + i[1]
        if check(ind, x) == False:
            ind.append(x)
            pair += 1
        continue
    elif i[1] == i[2]:
        y = i[1] + i[1] + i[0]
        if check(ind, y) == False:
            ind.append(y)
            pair += 1
        continue
    else:
        continue

print(ind)


print(actual)
print(pair)


