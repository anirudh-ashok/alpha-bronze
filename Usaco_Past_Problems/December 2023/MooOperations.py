n = int(input())
text = []


def ops(s, fstr):
    if fstr == "MOO":
        return len(s) - 3
    elif fstr[0] != "M" and fstr[1:3] == "OO":
        return len(s) - 2
    elif fstr[2] != "O" and fstr[:2] == "MO":
        return len(s) - 2
    return -1

for i in range(n):
    v = input()
    b = v[-3:]
    f = v[:3]
    bstep = ops(v, f)
    fstep = ops(v, b)
    if bstep == -1 and fstep == -1:
        text.append(-1)
        continue
    text.append(min(bstep, fstep))

for i in text:
    print(i)