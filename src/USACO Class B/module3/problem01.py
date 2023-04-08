dot, tasks = input().split(" ")
dot = int(dot)
tasks = int(tasks)
cows = []
for i in range(dot):
    cows.append(".")

def w_cows(cows, start, increment):
    for i in range(start-1, dot, increment):
        cows[i] = "V"
    return cows


for i in range(tasks):
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    cows = w_cows(cows,x,y)
print(cows.count("."))

