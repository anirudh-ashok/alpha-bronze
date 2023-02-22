rows, columns = input().split(" ")
rows = int(rows)
columns = int(columns)
brown_cow = []
for i in range(rows):
    x = input()
    brown_cow.append(x)
black_cow = []

for j in range(rows):
    x = input()
    black_cow.append(x)

new_str = ""
new_str_2 = ""
index_cow = []
index_bcow = []
for i in range(columns):
    for j in black_cow:
        new_str = j[i] + new_str
    index_cow.append(new_str)
    new_str = ""
    for e in brown_cow:
        new_str_2 = new_str_2 + e[i]
    index_bcow.append(new_str_2)
    new_str_2 = ""

count = 0
roosh = "2"
go= "1"
for i in index_cow:
    a = str(i.count("A"))
    c = str(i.count("C"))
    t = str(i.count("T"))
    g = str(i.count("G"))
    ap = a +c +g +t

    if ap.count("0") == rows - 2 or ap.count("1") == rows:
        count = count + 1
counter = 0
for i in index_bcow:
    a = str(i.count("A"))
    c = str(i.count("C"))
    t = str(i.count("T"))
    g = str(i.count("G"))
    ap = a +c +g +t

    if ap.count("0") == rows - 2 or ap.count("1") == rows:
        counter = counter + 1
print(min(count, counter))
