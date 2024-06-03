read = open("moocrypt.in")
n, m = map(int, read.readline().split())
puzzle = []
for i in range(n):
    puzzle.append(list(read.readline()))

pairs = []


def func(g):
    if len(g) == 2:
        g = list(g)
        f = 0
        for i in pairs:
            if g[0] in i[0] and g[1] in i[0]:
                i[1] += 1
                f = 1
                break
        if f == 0:
            pairs.append([g, 0])


# Check for Vertical Moo
vsearch = n - 3
if vsearch >= 0:
    for row in range(vsearch):
        for col in range(m):
            one = puzzle[row][col]
            two = puzzle[row + 1][col]
            three = puzzle[row + 2][col]
            g = set(one + two + three)
            func(g)

# Check for Horizontal Moo
hsearch = m - 3
if hsearch >= 0:
    for row in range(n):
        for char in range(hsearch):
            one = puzzle[row][char]
            two = puzzle[row][char+1]
            three = puzzle[row][char+2]
            g = set(one + two + three)
            func(g)

# Check for Diagonal Moo
if n >= 3 and m >= 3:
    for row in range(vsearch):
        for col in range(hsearch):
            one = puzzle[row][col]
            two = puzzle[row + 1][col+1]
            three = puzzle[row + 2][col+1]
            g = set(one + two + three)
            print(one, two, three)
            func(g)
    for row in range(vsearch):
        for col in range(0, hsearch-1, -1):
            one = puzzle[row][col]
            two = puzzle[row - 1][col - 1]
            three = puzzle[row - 2][col - 2]
            g = set(one + two + three)
            print(one, two, three)
            func(g)


print(pairs)

