rows, columns = input().split(" ")
rows = int(rows)
columns = int(columns)
count = 0
e = 0
while rows % 2 == 1 and columns % 2 == 1:
    count = count + 2 ** e
    e = e + 2
    rows = ((rows + 1) / 2) - 1
    columns = ((columns + 1) / 2) - 1

print(count)
