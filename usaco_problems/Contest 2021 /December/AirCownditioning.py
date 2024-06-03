n = int(input())
goal = list(map(int, input().split()))
curr = list(map(int, input().split()))
diff = []
for i in range(n):
    d = goal[i] - curr[i]
    diff.append(d)

for i in range(n):
    for j in diff:

