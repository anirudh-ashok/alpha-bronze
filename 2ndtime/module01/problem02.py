string, charms, nail = input().split(" ")
string = int(string)
charms = int(charms)
nail = int(nail)
def calc(c_str, dist):
    if nail > dist:
        return c_str + (nail-dist)
    else:
        return c_str + (dist-nail)

lis = []
for i in range(charms):
    x,y = input().split(" ")
    d = calc(int(x), int(y))
    lis.append(d)
for i in lis:
    print(i)
