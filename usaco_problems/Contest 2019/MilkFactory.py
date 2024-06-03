read = open("factory.in")
n = int(read.readline())
lis = []
for i in range(n):
    lis.append(i+1)
station = []
for i in range(n-1):
    z = list(map(int, read.readline().split()))
    lis.remove(z[0])


if len(lis) == 1:
    print(lis[0], file=open("factory.out", "w"))
else:
    print(-1, file=open("factory.out", "w"))
