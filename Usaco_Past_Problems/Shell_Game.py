read = open("shell.in")

n = int(read.readline())

# shell_at_pos[i] stores the label of the shell located at position i
# The shells can be placed arbitrarily at the start.
shell_at_pos = [i for i in range(3)]

# counter[i] stores the number of times the shell with label i was picked
counter = [0 for _ in range(3)]

for _ in range(n):
	# Zero indexing: offset all positions by 1
	a, b, g = [int(i) - 1 for i in read.readline().split()]

	# Perform Bessie's swapping operation
	shell_at_pos[a], shell_at_pos[b] = shell_at_pos[b], shell_at_pos[a]

	# Count the number of times Elsie guesses each particular shell
	counter[shell_at_pos[g]] += 1

print(max(counter), file=open("shell.out", "w"))

'''
read = open("mixmilk.in")
b1 = list([int(i) for i in read.readline().split()])
b2 = list([int(i) for i in read.readline().split()])
b3 = list([int(i) for i in read.readline().split()])
def mix(b1, b2):
    if b1[1] + b2[1] > b2[0]:
        b1[1] = abs(b1[1] - b2[1])
        b2[1] = b2[0]
    else:
        b2[1] = b1[1] + b2[1]
        b1[1] = 0
    return b1, b2


for i in range(1):
    b1, b2 = mix(b1, b2)
    b2, b3 = mix(b2, b3)
    b1, b3 = mix(b1, b3)

print(b1, file=open("mixmilk.out", "w"))
print(b2, file=open("mixmilk.out", "a"))
print(b3, file=open("mixmilk.out", "a"))

print(b1, b2, b3)
'''