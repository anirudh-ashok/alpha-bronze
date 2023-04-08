import math
num = int(input())

root = math.ceil(math.sqrt(num))
cout = 0
for i in range(0,root+1):
  for j in range(0,root+1):
    for k in range(0,root+1):
      for e in range(0,root+1):
        if i**2 + j**2 + k**2 + e**2 == num:
          cout = cout+1
          if e == root:
            break
print((cout))