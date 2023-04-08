
x1, y1, x2, y2 = input().split(" ")
x3, y3, x4, y4 = input().split(" ")
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
x4 = int(x4)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)
y4 = int(y4)
#rect1 = [[x1,y1], [x1,y2], [x2,y2], [x2,y1]]
#rect2 = [[x3,y3], [x3,y4], [x4,y4], [x4,y3]]
def finder(x1,y1,x2,y2, x3, y3, x4, y4 ):
    #Input bottom left and top right
    lis = []
    if x4 > x1 > x3 and y4 > y1 > y3:
        lis.append([x1,y1])
    if x4 > x2 > x3 and y4 > y2 > y3:
        lis.append([x2,y2])
    if x4 > x1 > x3 and y4 > y2 > y3:
        lis.append([x1,y2])
    if x4 > x2 > x3 and y4 > y1 > y3:
        lis.append([x2, y1])
    return lis


p = (finder(x1, y1, x2, y2, x3, y3, x4, y4))
print(p)
if len(p) == 0 or len(p) == 1:
    # Area of rect
    print(int(x2 - x1) * int(y2 - y1))
elif len(p) == 2:
    d = min(x1,x3) - max(x2,x4) * min(y3,y1) - max(y4,y2)
    print(d)
else:
    print(0)
