n = int(input())
S = []
O = []
M = []
E = []
B = []
I = []
G = []
for i in range(n):
    x,y = input().split(" ")
    y = int(y)
    if x == "S":
        S.append(y)
    elif x == "O":
        O.append(y)
    elif x == "M":
        M.append(y)
    elif x == "E":
        E.append(y)
    elif x == "B":
        B.append(y)
    elif x == "I":
        I.append(y)
    elif x == "G":
        G.append(y)

def somebig(S,O,M,E,B,I,G):
    shallop = (O+M+O)*(S+I+S+B+E+E)*(E+G+O+S)
    return shallop

count = 0
for s in S:
    for o in O:
        for m in M:
            for e in E:
                for b in B:
                    for i in I:
                        for g in G:
                            if somebig(s,o,m,e,b,i,g) % 2 == 0:
                                count = count+1

print(count)