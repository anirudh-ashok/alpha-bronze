n = int(input())
g_log = list(input().split(" "))
g_log = g_log[::-1]
game = []
for i in g_log:
    game.append(int(i))
copy = game[:]

for i in copy:
    if i == -1:
        p = game.index[i]
        if p != 0:
            if game[p-1] != -1:
                game[p] = game[p-1] + 1
            elif game[p+1] != -1:
                game[p] = game[p+1] - 1






'''
for i in range(n,0,-1):
    if game[i] != -1:
        p = i
        for j in range(game[i],0,-1):
            if j == game[i]:
                continue
            elif game[i] == -1:
                continue
            else:
                print(0)
            p = p-1
        print(p)

for i in game:
    if i != -1:
        p = game.index(i)
        for j in range(i-1,0,-1):
            print(game[p])
            p = p-1
            if game[p] == -1:
                continue
            elif game[p] == j:
                continue
            else:
                print(0)
                break



'''