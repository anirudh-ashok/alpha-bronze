'''
Weak points:
The shape has to be a square. Find the endpoints of the square. Then using start and end points given, calculate the
smallest right tri dist
'''
n, p = map(int, input().split())
coor = []
for i in range(p):
    x, y = map(int, input().split())
    if i == 0:
        maxc = [x, y]
        minc = [x, y]
        continue
    if x > maxc[0] and y > maxc[1]:
        maxc = [x, y]
    if x < minc[0] and y < minc[1]:
        minc = [x, y]


print(maxc, minc)

def func(x1, y1, x2, y2):
    if x1 <= maxc[0]:
        if y2 <= maxc[1]:
            return maxc[0] - x1 + maxc[1] - y1
        elif x2 > min[]

path = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())



