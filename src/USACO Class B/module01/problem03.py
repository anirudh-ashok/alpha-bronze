import math
cows, b_num = input().split(" ")
cows = int(cows)
x_val = []
y_val = []
for i in range(cows):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    x_val.append([x, y])


def quadrant(x_ax, y_ax, lis):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for i in lis:
        if i[0] >= x_ax and i[1] >= y_ax:
            q1 += 1
        if i[0] >= x_ax and i[1] <= y_ax:
            q2 += 1
        if i[0] <= x_ax and i[1] >= y_ax:
            q3 += 1
        if i[0] <= x_ax and i[1] <= y_ax:
            q4 += 1
    p = max(q1, q2, q3, q4)
    return p


max_num = 879656865764576879
p_val = x_val[:]
pliss = []
for i in x_val:
    for j in x_val:
        x = quadrant(i[0], j[1], p_val)
        if x >= cows // 4 and x not in pliss:
            pliss.append(x)

pliss.sort()
print(pliss)
