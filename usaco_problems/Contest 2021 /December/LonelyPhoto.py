n = int(input())
cows = str(input())
count = 0
for i in range(n-2):
    substr = cows[i:i+3]
    gcount = substr.count("G")
    hcount = substr.count("H")
    if gcount == 2 or hcount == 2:
        count += 1

    for c in range(i+3, n):
        if cows[c] == "G":
            gcount += 1
        else:
            hcount += 1
        if gcount > 1 and hcount > 1:
            break
        elif gcount == 0 or hcount == 0:
            continue
        count += 1


print(count)