n, m = input().split(" ")
m = int(m)
def baseTen(num, base):
    count = 0
    c = 0
    num = num[::-1]
    for i in num:
        c += int(i) * (int(base) ** count)
        count += 1
    return c
print(baseTen(n,m))