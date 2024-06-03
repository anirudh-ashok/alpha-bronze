read = open("cowtip.in")
n = int(read.readline())
ntip = 0
cows = []
for i in range(n):
    l = list(map(int, read.readline().split()))
    ntip += l.count(0)

def swap(lis):
    for i in range(n-1):
        for j in range(n):
            if lis[i][j] == 0:
                if lis[i+1][j] == 0:



