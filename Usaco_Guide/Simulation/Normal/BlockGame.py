'''

'''
alpha = "abcdefghijklmnopqrstuvwxyz"
read = open("blocks.in")
n = int(read.readline())
letters = [0]*26
words = []
for i in range(n):
    w1, w2 = (read.readline().split())
    for i in w1:
        pos = w1.index[i]
        if i == w2[pos]:



