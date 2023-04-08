n, m = input().split(" ")
m = int(m)
def baseM(num, base):
    c = ""
    while num != 0:
        c += str(num % base)
        num = num//base
    return c[::-1]
print(baseM(int(n), m))