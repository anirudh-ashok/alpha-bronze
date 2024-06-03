
def maxim(num, num2):
    cp = ""
    for i in num:
        if i != "5":
            cp += i
            continue
        cp += "6"
    cp_2 = ""
    for i in num2:
        if i != "5":
            cp_2 += i
            continue
        cp_2 += "6"
    return int(cp) + int(cp_2)

def minim(num, num2):
    cp = ""
    for i in num:
        if i != "6":
            cp += i
            continue
        cp += "5"
    cp_2 = ""
    for i in num2:
        if i != "6":
            cp_2 += i
            continue
        cp_2 += "5"
    return int(cp) + int(cp_2)
p = []

for i in range(1):
    x,y = input().split(" ")
    p.append([minim(x,y), maxim(x,y)])

for i in p:
    print(i[0], i[1])
