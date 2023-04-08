num = int(input())

cows = list(input().split(" "))
cow = []
for i in cows:
    x = int(i)
    cow.append(x)
cow.sort()
cow_d = cow[:]
print(cow)
diff = []
for i in range(0,len(cows)-1):
    diff.append(abs(cow[i] - cow[i+1]))
qualify = []
q_lis = diff[:]
count = 0
for i in range(len(diff)-1):
    for j in range(0,i+1,-1):
        print(q_lis[j])
        if q_lis[j] >= q_lis[j-1]:
            count += 1
    qualify.append(count)

print(qualify)
