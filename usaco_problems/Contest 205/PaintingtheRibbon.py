t = int(input())
resp = []
for i in range(t):
    m, n, k = map(int, input().split())
    if n > k:
        resp.append("YES")
        continue
    resp.append("NO")

for i in resp:
    print(i)