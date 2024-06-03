'''
1. What does problem ask?
Asks for you to find the minimum distance FJ has to travel from his initial position to the lost cow's position if
he uses the pattern x+1, x-2, x+4...

2. Given inputs
Given FJ's Starting pos and the Lost cow's location

3. Output
The distance he has to travel to reach the cow

4. What can derive from the input?
I can run a simulation of (x + 1, x - 2, x + 4, ....) By using a multiple factor of 2 on the integer until the value is
greater than the cow's pos. There will be a count for distance. Then if the value exceeds the cows pos then I will
subtract difference of their positions from distance


'''

read = open("lostcow.in")
fj, lc = map(int, read.readline().split())
n = 1
dist = 0
pos_lis = [fj]
overcount = 0
if fj == lc:
    print(0)
elif fj < lc:
    for i in range(9):
        if i % 2 == 1:
            pol = -1
        else:
            pol = 1
        pos = fj + (n*pol)
        pos_lis.append(pos)
        if pos >= lc:
            overcount = pos - lc
            break
        n = n*2

    for i in range(len(pos_lis) - 1):
        dist += abs(pos_lis[i] - pos_lis[i + 1])
    print((dist - overcount), file=open("lostcow.out", "w"))
    #print(dist - overcount)
else:
    for i in range(9):
        if i % 2 == 1:
            pol = -1
        else:
            pol = 1
        pos = fj + (n*pol)
        pos_lis.append(pos)
        if pos <= lc:
            overcount = pos - lc
            break
        n = n*2

    for i in range(len(pos_lis)-1):
        dist += abs(pos_lis[i] - pos_lis[i+1])
    print((dist + overcount), file=open("lostcow.out", "w"))
    #print(dist + overcount)