num = input()
x = (int(num, 16))
def baseM(num, base):
    c = ""
    while num != 0:
        c += str(num % base)
        num = num//base
    return c[::-1]
print(baseM(x,8))
'''
def converter(num):
    if num == 0:
        return 0000
    count = ""
    while num != 0:
        p = num % 2
        count += str(p)
        num = num // 2
    return count[::-1]
bin_num = ""
for i in num:
    if i == "A":
        bin_num += converter(10)
        continue
    if i == "B":
        bin_num += converter(11)
        continue
    if i == "C":
        bin_num += converter(12)
        continue
    if i == "D":
        bin_num += converter(13)
        continue
    if i == "E":
        bin_num += converter(14)
        continue
    if i == "F":
        bin_num += converter(15)
        continue
    else:
        bin_num += converter(int(i))
print(int(bin_num))
'''