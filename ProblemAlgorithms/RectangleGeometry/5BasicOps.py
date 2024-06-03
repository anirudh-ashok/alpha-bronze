import math

x1 = 0
x2 = 0
y1 = 0
y2 = 0
endpoint1 = [x1, y1]
endpoint2 = [x2, y2]
# The coordinates (x1, y1) and (x2, y2) are the two farthest endpoints of a rectangle
'''
Example: The starts are the two farthest endpoints
.......*
........
........
*.......

'''


def Dimensions(x1, y1, x2, y2):
    length = y2 - y1
    width = x2 - x1
    return length, width


def Distance(x1, y1, x2, y2):
    return math.sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)


def area(length, width):
    return length * width


# The two variables below r1 and r2 are the coordinates of 2 rectangles
r1 = [x1, y1, x2, y2]
r2 = [x1, y1, x2, y2]


def intersect(s1, s2):
    bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
    bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

    # no overlap
    if bl_a_x >= tr_b_x or tr_a_x <= bl_b_x or bl_a_y >= tr_b_y or tr_a_y <= bl_b_y:
        return False
    else:
        return True

