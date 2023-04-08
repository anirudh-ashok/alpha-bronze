length, participants = input().split(" ")
length = int(length)
participants = int(participants)


def func(rate, stretch, rest, length):
    rate = int(rate)
    stretch = int(stretch)
    rest = int(rest)
    count = 0
    e = 0
    while e < length:
        for i in range(1, stretch + 1):
            if (i * rate) + e >= length:
                e = e + (rate * i)
                count = count + i

                break
            elif i == stretch:
                e = e + (rate * i)
                count = count + i + rest
    return count


lis = []
for i in range(participants):
    x, y, z = input().split(" ")
    ans = func(x, y, z, length)
    lis.append(ans)

for i in lis:
    print(i)
