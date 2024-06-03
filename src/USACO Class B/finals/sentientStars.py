n = int(input())
stars = list(map(int, input().split(" ")))
ind = stars.index(max(stars))
cp = stars[:]
cp.sort()
count = 0
while stars != cp:
    if stars[0] < stars[ind + 1]:
        stars.insert(ind+1, stars[0])
    else:
        stars.insert(ind+2, stars[0])
    stars.pop(0)

    count += 1

print(count)



