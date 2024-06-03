'''
1. Problem Statement
Given The length of the Number line and the place where bessie starts. Bessie can either jump on a target which breaks
if her jump force is greater than its force, or a launch pad which multiplies and reverses her direction and forece.
Bessie jumps infinetly so
'''
n, start = map(int, input().split())
pads = []
for i in range(n):
    pads.append(list(map(int, input().split())))

prevpos = []
jump = [start,0]
mv = [start, 1]
count = 0
while mv not in prevpos:
    pos = pads[mv[0]+mv[1]-1]
    prevpos.append(pos)
    print(pos, mv)
    # it is a Target
    if pos[0] == 1 and mv[1] >= pos[1]:
        count += 1
        mv[0] += 1
    elif pos[0] == 0:
        mv[0] -= pos[1]
        mv[1] += pos[1]
    if mv[0] > n or mv[0] <= 0:
        break
print(count)



