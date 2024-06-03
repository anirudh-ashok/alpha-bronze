'''
Solution Idea:
Read inputs seperating the first two letters of the first word
Since the input can go up to 200,000 cannot do brute force
Instead construct a solution set by using the list with the first 2 elements from the
'''
read = open("citystate.in")
n = int(read.readline())
solutionset = []
for i in range(n):
    state, address = read.readline().split()
    state = state[0:2]
    if [state, address] in solutionset or [address, state] in solutionset:
        continue
    solutionset.append([state, address])
#print(n-len(solutionset), file=open("citystate.out", "w"))
print(solutionset)
