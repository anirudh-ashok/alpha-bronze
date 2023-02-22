num, ti = input().split(" ")
num = int(num)
ti = int(ti)
lis = []
for i in range(ti):
    work = list(input().split(" "))
    lis.append(work)
lis_1 = []
for i in lis:
    serial = int(i[0])
    t_1 = int(i[2])
    t_2 = int(i[3])
    lis_1.append([serial, i[1], t_1, t_2])

lis_1.sort()

d = int(ti / 2)
count = 0
lis_4 = []
for i in range(d):
    start_m = lis_1[0][2] * 60
    start_s = lis_1[0][3]
    d = lis_1.pop(0)
    p = lis_1[0][0]
    for j in lis_1:
        if j[1] == "STOP":
            stop_m = j[2] * 60
            stop_s = j[3]
            count = count + ((stop_m + stop_s) - (start_m + start_s))
            lis_1.remove(j)
            break
    if lis_1 == []:
        lis_4.append(count)
        break
    else:
        if lis_1[0][0] != p:
            lis_4.append(count)
            count = 0


for i in lis_4:
    p = int((i - (i%60)) / 60)
    d = i%60
    print(p, d)