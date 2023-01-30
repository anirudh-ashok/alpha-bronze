reps = int(input())
block_1 = ""
block_2 = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(reps):
    x,y = input().split(" ")
    block_1 = block_1 + x
    block_2 = block_2 + y

print(block_1, block_2)

u_count_1 = 0
lis_1 = []
lis_2 = []
counter = 0
count = 0
u_count_2 = 0
for i in alphabet:
    count = 0
    counter = 0
    for e in block_1:
        if e == i:
            count = count+1
            u_count_1 = u_count_1 + 1
    lis_1.append(count)
    for j in block_2:
        if j == i:
            counter = counter+1
            u_count_2 = u_count_2 + 1
    lis_2.append(counter)

print(lis_1)
print(lis_2)