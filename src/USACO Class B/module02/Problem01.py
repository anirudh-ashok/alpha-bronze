x, end = input().split(" ")
x = int(x)
end = int(end)
direction = 1
distance = 1
ans = 0
c_pos = 0
while c_pos != end:
    c_pos = x + (direction * distance)
    ans += distance + distance // 2
    if x < end and c_pos >= end:
        print(ans)
        break
    elif x > end and c_pos <= end:
        print(ans)
        break
    else:
        direction *= -1
        distance *= 2






