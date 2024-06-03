'''
1. What is the problem asking?
Given a tictactoe board with many cows that have played, find the number of cows that have won singlehandedly, and the
number of pairs of cows that can win if they are counted as one

2. Given input
Three strings of lenght three to represent a tic tac toe board

3.Expected output
Number of cows who won singlehandedly
Number of cow pairs who could have won as a team

4. How to solve:
board = ["", "", ""]
Solve for singlehandedly and double handedly simultaneously
single = 0
double = 0
Check vertical and horizontal cases
def diag(ttt):
    d1 = ""
    for i in range(3):
        d1 += ttt[i][i]
    d2 = ""
    for i in range(0, 3, -1):
        d2 += ttt[i][i]

'''

read = open("tttt.in")
board = []
for i in range(3):
    n = read.readline()
    if i < 2:
        n = n[0:3]
    board.append(n)

single = 0
double = 0


def diag(ttt):
    d1 = ""
    for i in range(3):
        d1 += ttt[i][i]
    d2 = ""
    count = 0
    for i in range(2, -1, -1):
        d2 += ttt[count][i]
        count += 1
    return list(set(d1)), list(set(d2))


uno = []
dos = []
# Checking for Horizontal
for i in board:
    simp = list(set(i))
    if len(simp) == 1 and simp[0] not in uno:
        single += 1
        uno.append(simp[0])
        print(simp)
    elif len(simp) == 2 and str(simp[0] + simp[1]) not in dos and str(simp[1] + simp[0]) not in dos:
        double += 1
        dos.append(str(simp[0] + simp[1]))

# Checking for vertical
for i in range(3):
    col = list(set((board[0][i] + board[1][i] + board[2][i])))

    if len(col) == 1 and col[0] not in uno:
        single += 1
        uno.append(col[0])

    elif len(col) == 2 and str(col[0] + col[1]) not in dos and str(col[1] + col[0]) not in dos:
        double += 1
        dos.append(str(col[0] + col[1]))




diagonals = list(diag(board))

for simp in diagonals:
    if len(simp) == 1 and simp[0] not in uno:
        single += 1
        uno.append(simp[0])

    elif len(simp) == 2 and str(simp[0] + simp[1]) not in dos and str(simp[1] + simp[0]) not in dos:
        double += 1
        dos.append(str(simp[0] + simp[1]))


print(single, file=open("tttt.out", "w"))
print(double, file=open("tttt.out", "a"))
