n = int(input())
pulley = []
for i in range(n-1):
    x = list(map(int, input().split(" ")))
    pulley.append(x)
pulley.sort()
dir = [0]
for i in range(n):
    if len(dir) == n:

        break
    if dir[i] == 1:
        if pulley[i][2] == 0:
            dir.append(1)
        else:
            dir.append(0)
    else:
        if pulley[i][2] == 0:
            dir.append(0)
        else:
            dir.append(1)
x = len(dir) - 1
print(dir[x])