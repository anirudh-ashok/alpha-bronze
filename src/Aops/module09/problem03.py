columns, rows = input().split(" ")

columns = int(columns)
rows = int(rows)
garden = []
for i in range(columns):
    e = list(input().split(" "))
    l = []
    for j in e:
        j = int(j)
        l.append(j)
    garden.append(l)


print(garden)
ra = max(rows, columns)
sha = min(rows, columns)
max = 0
li = 0
gi = j
for i in range(ra-3):
    for j in range(sha - 3):
        x = garden[i][j] + garden[i][j+1] + garden[i][j+2] + garden[i+1][j] + garden[i+1][j+1] + garden[i+1][j+2] + garden[i+2][j] + garden[i+2][j+1] + garden[i+2][j+2]
        if x > max:
            max = x
            li = i
            gi = j

print(max)
print(li+ 1, gi+ 1)

