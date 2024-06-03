cows, finalists = input().split(" ")
cows = int(cows)
finalists = int(finalists)
candidates = []
round_1 = []
round_2 = []
for i in range(cows):
    r_1, r_2 = input().split(" ")
    r_1 = int(r_1)
    r_2 = int(r_2)
    candidates.append([r_1, r_2])
    round_1.append(r_1)
    round_2.append(r_2)

round_1.sort(reverse = True)
M_list = round_1[0:finalists]
maxe = 0

for i in candidates:
    if i[0] in M_list:
        if maxe < i[1]:
            ind = candidates.index(i) + 1
            maxe = i[1]

print(ind)
