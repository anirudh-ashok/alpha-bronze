t = int(input())
ans = []
for i in range(t):
    n = int(input())
    lis = set(list(map(int, input().split())))
    ans.append(n - len(lis))

for i in ans:
    print(i)
