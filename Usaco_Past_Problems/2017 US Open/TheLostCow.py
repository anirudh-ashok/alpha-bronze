read = open("lostcow.in")
start, end = map(int, read.readline().split())
dist = 0
turn = 1
polarity = 1
pos = start
bpos = start
if start <= end:
    while pos < end:
        pos = start + (polarity * turn)
        dist += abs(pos - bpos)
        polarity *= -1
        turn *= 2
        bpos = pos
    print(dist - (pos - end), file=open("lostcow.out", "w"))
    #print(dist)
else:
    while pos > end:
        pos = start + (polarity * turn)
        dist += abs(pos - bpos)
        polarity *= -1
        turn *= 2
        bpos = pos
    print(dist - (pos - end), file=open("lostcow.out", "w"))
    #print(dist)


