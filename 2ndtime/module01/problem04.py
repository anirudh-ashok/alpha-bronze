row, column, times = input().split(" ")
row = int(row)
column = int(column)
times = int(times)
fig = []
for i in range(row):
    fig.append(list(input()))
x = ""
lis2 = []
for i in fig:
    for j in i:
        x += j*times
    lis2.append(x)
    x = ""
for i in lis2:
    for j in range(times):
        print(i)
'''

'''