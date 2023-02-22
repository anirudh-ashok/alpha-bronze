size, start = input().split(" ")
cphabet = [0,1,2,3,4,5,6,7,8,9]
size = int(size)
blah = size
start = int(start)
n = int((size*(size+1)) /2) + start
lis = []
for i in range(start, n):
    p = str(i)
    x = int(p[-1])
    lis.append(x)
print(lis)
cout = 0
for i in range(blah):
    for j in range(0,size):
        cout = cout+j
        print(cout)
        lis.pop(lis[cout])
    print("")
    size = size - 1
    cout = 0

print(lis)

