
num = int(input())

lis = {}
lis2 = []
for i in range(num):
    l = input()
    hrs, minu, sec = l.split(" ")
    hrs = int(hrs)
    minu = int(minu)
    sec = int(sec)
    time = (hrs*3600) + (minu*60) + sec
    lis[time] = l
    lis2.append(time)

lis2.sort()
for i in lis2:
    print(lis[i])



