def calc(lis, num):
    standard = []
    for e in range(num):
        for j in lis:
            pair = [j[0][e], j[1]]
            for i in standard:
                if pair[0] == i[0]:
                    if pair[1] != i[1]:
                        return "LIE", e
                    else:
                        continue
            standard.append(pair)
    return "OK"


t = int(input())
for i in range(t):
    d = input()
    n, m = map(int, input().split())
    l = []
    for i in range(m):
        l.append(list(input().split()))
    x = str(l[0][0])
    print(calc(l, n))