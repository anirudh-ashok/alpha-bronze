read = open("shuffle.in")
n = int(read.readline())
order = [int(i)-1 for i in read.readline().split()]
order2 = [int(i) for i in read.readline().split()]


def rearrange(ord, lis):
    n_lis = []
    for i in ord:
        n_lis.append(lis[i])
    return n_lis

for i in range(3):
    order2 = rearrange(order, order2)
    print(order2)

with open("shuffle.out", "w") as out:
    for i in order2:
        print(i, file=out)
