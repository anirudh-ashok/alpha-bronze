rep = int(input())
leaderboard = []

for i in range(rep):
    e,v,x = (input().split(" "))
    e = int(e)
    x =  int(x)
    lis = [e,v,x]
    leaderboard.append(lis)
    lis = []

leaderboard.sort()
b = 7
m = 7
e = 7
maxe = 0
count = 0
for i in leaderboard:
    if i[1] == "Bessie":
        b = b+i[2]
    elif i[1] == "Mildred":
        m = m+i[2]
    elif i[1] == "Elsie":
        e = e+i[2]
    max_num = max(b,m,e)
    print(max_num,maxe)
    if max_num > maxe or max_num < maxe:
        count = count+1
        maxe = max_num

print(count)