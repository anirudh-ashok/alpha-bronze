n = int(input())
ppl = []
for i in range(n):
    ppl.append(int(input()))

def adder(lis):
    count = 0
    cp = lis[:]
    for i in lis:
        cp.pop(0)
        for j in cp:
            count += j
    return count

max_num = 8097654
copy = ppl[:]
for i in range(n-1):
    if ppl[0] == copy[i]:
        p = 0
    else:
        p = ppl[0]
        ppl.pop(0)
        ppl.append(p)
    num = adder(ppl)
    if num < max_num:
        max_num = num
print(max_num)

