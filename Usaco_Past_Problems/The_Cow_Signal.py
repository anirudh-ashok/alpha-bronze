
n_str = []
'''
ln, r, scale = map(int, input().split(" "))
lis = [ln, r, scale]
with open("cowsignal.in", "a+") as read:
    read.write(ln)
    read.write(r)
    read.write(scale)
for i in range(ln):
    sig = list(input())
    s = ""
    for i in sig:
        s += i * scale
    for i in range(scale):
        n_str.append(s)
with open("cowsignal.out", "a+") as out:
    for i in n_str:
        out.write(i)
'''
input_file = open("cowsignal.in")
ln, r, scale = [int(i) for i in input_file.readline().split()]
for i in range(ln):
    sig = list(input_file.readline().split("\n")[0])
    #if i != ln-1:
    #   sig.pop(r)
    s = ""
    for i in sig:
        s += i * scale
    for i in range(scale):
        n_str.append(s)
    # print(n_str)

with open("cowsignal.out", "w+") as f:
    for m in n_str:
        print(m, file=f)

