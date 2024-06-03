n = int(input())
g_log = input().split(" ")
game = []
for i in g_log:
    game.append(int(i))
game = game[::-1]
copy = game[:]
count = 0
u_count = 0
for i in game:
    p = game.index(i)
    if i == -1:
        if game[p+1] != 0:
            copy[p] = copy[p+1]-1
        else:
            u_count += 1
    else:
        if game[p + 1] - 1 != 0 and game[p + 1] - 1 == i:
            continue
        print(-1)
        break