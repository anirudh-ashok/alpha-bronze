rep = int(input())
# Plan Have one dictionary, and two lists. find max dipi in one ist. then add them up and print. Now, take those
# three and get the dictionary values. print the order +1
scale = []
dict = {}
items = []

for i in range(rep):
    y,x = input().split(" ")
    y = int(y)
    x = int(x)
    items.append([y,x])
    scale.append(y/x)
    dict[y/x] = [y,x]

scale.sort(reverse = True)
var = dict[scale[0]]
var_2 = dict[scale[1]]
var_3 = dict[scale[2]]
print(var[1]+var_2[1]+var_3[1])

p_1 = items.index(var)
p_2 = items.index(var_2)
p_3 = items.index(var_3)

print(p_1)
print(p_2)
print(p_3)

