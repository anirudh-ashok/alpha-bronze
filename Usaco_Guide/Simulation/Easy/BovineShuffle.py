'''
1. What is the Problem asking?
Given N cows, and a list showing how to sort them, and their ending order, find their original order

2. What is the Given input?
N cows. Indexes of N length showing the mixed order of 1 shuffle. Cows after 3 shuffles

3. Expected output
The original order of cows

4. What can be derived from input?
Read each input, assigning increasing indexes to each input. Create a function which takes in this list and the sort
commands. It will shuffle the list according to the commands, but the indexes will still be in numerical order.
This function will be run 3 times


'''

read = open("shuffle.in")
n = int(read.readline())
inst = list(map(int, read.readline().split()))
cows = list(map(int, read.readline().split()))

def shuffle(lis, comm):
    n_lis = []
    for i in comm:
        n_lis.append(lis[i-1])
    return n_lis

for i in range(3):
    cows = shuffle(cows, inst)

for i in cows:
    print(i, file=open("shuffle.out", "a"))
