n, q = map(int, input().split())
state = list(input().split())
acount = state.count("and")
queries = []

def func(s, acount):
    if len(s) == 1:
        return s
    if acount > 0:
        recon = "and"
        for i in range(1, len(s), 2):
            if s[i] == recon:
                if s[i-1] == s[i+1] == "true":
                    acount -= 1
                    s[i+1] = "true"
                else:
                    s[i+1] = "false"
                s.pop(i)
                s.pop(i - 1)
    else:
        recon = "or"
        for i in range(1, len(s), 2):
            if s[i] == recon:
                if s[i-1] == "true" or s[i+1] == "true":
                    s[i+1] = "true"
                else:
                    s[i+1] = "false"
                s.pop(i)
                s.pop(i - 1)
    func(s, acount)





ans = ""
for i in range(q):
    l, r, b = input().split()
    l = int(l)-1
    r = int(r)-1
    v = r
    copy = queries[:]
    for j in range(l, r):
        copy.pop(j)
        v = v - 1
    copy[v] = "false"
    v1 = func(copy, acount)
    copy[v] = "true"
    v2 = func(copy, acount)
    if v1 == v2 == b:
        ans += "Y"
    else:
        ans += "N"





