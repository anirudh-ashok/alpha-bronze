read = open("cownomics.in")
x, y, m = map(int, read.readline().split())
mol = 12345678
for i in range(int(m/y) + 1):
    num = (m - i*y) % x
    if num < mol:
        mol = num
print(m - mol, file=open("pails.out", "w"))
