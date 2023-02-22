rows, columns = input().split(" ")
rows = int(rows)

puddles = []
columns = int(columns)
for i in range(rows):
    x = list(input().replace("", " ").split(" "))
    x.pop(0)
    x.pop(len(x) - 1)
    puddles.append(x)

count = 0

for i in range(0, rows-1):
    for j in range(0, columns):
        if puddles[i][j] == puddles[i + 1][j] == "#":
            count = count + 1
            puddles[i][j] = 0
            puddles[i+1][j] = 0


for j in range(0,rows):
    for i in range(0,columns):
        if i == columns-1:
            continue
        elif puddles[j][i] == puddles[j][i+1] == "#":
            count = count + 1
            puddles[j][i] = 0
            puddles[j][i + 1] = 0

for e in puddles:
    for i in e:
        if i != 0 and i != ".":
            count = count+1


print(count)

'''
if i == rows-1 and puddles[i][j] == "#" and puddles[i-1][j] == ".":
    print("yanina")
    if j == rows-1 and puddles[i][j-1]==".":
        count = count+1
        continue
    elif puddles[i][j-1]==puddles[i][j+1] == ".":
        count = count+1
        continue
        
        
                elif j == 0 or j== rows-1 and puddles[j][i] == "#":
            if puddles[j][i] !=
'''