read = open("sleepy.in")
n = int(read.readline())
cows = list(map(int, read.readline()))
ideal = cows[:]
ideal.sort()

while cows != ideal:
    char = cows[0]
    for i in range(1, n):
        b.,jkb
