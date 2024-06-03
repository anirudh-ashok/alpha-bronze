t = int(input())
def compare(l1, l2):
    val = 1/4
    count = 0
    for i in l1:
        c = 0
        for v in l2:
            if v < i:
                c += 1
        count += (c/4)*val
    if count > 0.5:
        coun