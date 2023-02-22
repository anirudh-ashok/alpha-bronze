n = int(input())
pattern_1 = []
new_pattern = []
for i in range(n):
    e = input()
    pattern_1.append(e)

for i in range(n):
    e = input()
    new_pattern.append(e)

bean = pattern_1[:]


def turn_90(lis):
    par = lis[:]
    new = []
    for i in range(n):
        p = ""
        for j in par:
            p = p + j[i]
        z = p[::-1]
        new.append(z)
    return new


def turn_180(lis):
    nlis = lis[:]
    nlis = nlis[::-1]
    shod = []
    for i in nlis:
        shod.append(i[::-1])

    return shod


def turn_270(lis_90):
    nlis = []
    for i in lis_90:
        n = i[::-1]
        nlis.append(n)
    return nlis




if 0 == 0:
    op_1 = turn_90(bean)
    op_2 = turn_180(bean)
    al = turn_90(bean)
    op_3 = turn_270(al)
    op_4 = turn_270(bean)
    if op_1 == new_pattern:
        print(1)
    elif op_2 == new_pattern:
        print(2)
    elif op_3 == new_pattern:
        print(3)
    elif op_4 == new_pattern:
        print(4)
    elif turn_90(op_4) == new_pattern or turn_180(op_4) == new_pattern or turn_270(op_4) == new_pattern:
        print(5)
    elif pattern_1 == new_pattern:
        print(6)
    else:
        print(7)

