num = int(input())
matches = []
for i in range(num):
  c1, c2 = input().split(" ")
  c1 = int(c1)
  c2 = int(c2)
  matches.append([c1,c2])

def func(horn, grass, shears, lis):
  count = 0
  for i in lis:
    if i[0] == horn:
      if i[1] == shears:
        count += 1
      else:
        continue
    elif i[0] == grass:
      if i[1] == horn:
        count += 1
      else:
        continue
    elif i[0] == shears:
      if i[1] == grass:
        count += 1
    else:
      continue
  return count

t_1 = func(1,2,3, matches)
t_2 = func(1,3,2, matches)
t_3 = func(2,1,3, matches)
t_4 = func(2,1,3, matches)
t_5 = func(3,1,2, matches)
t_6 = func(3,2,1, matches)
print(max(t_1, t_2, t_3, t_4, t_5, t_6))


