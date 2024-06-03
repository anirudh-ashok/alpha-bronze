'''
n, m = map(int, input().split(" "))
doors = []
for i in range(m):
    x, y, a, b = map(int, input().split(" "))
    if [x, y] == [1, 1]:
        doors.insert(0, [[x,y], [a,b]])
    else:
        doors.append([[x,y], [a,b]])
on = [[1,1]]
acc = [[1,1]]
for i in doors:
    for j in doors:
        if i[0] == j[0] and j[1] not in on and j[0] in acc:
            on.append(j[1])
            acc.append(j[1])
print(on)
'''