n = int(input())
mon = 0
tue = 0
wed = 0
thu = 0
fri = 0
sat = 0
sun = 0
leap = 0
days = ["mon", "tue", "wed",  "thu", "fri", "sat", "sun"]
start = "mon"
day = "Mon"
def sim(start, days):
    d = days % 7
    if d == 0:



for i in range(1900, 1900+n):
    count = 1
    if i % 4 == 0:
        leap = 1
    else:
        leap = 0
    for j in range(1, 12):
        if j == 2:
            if leap == 1:
            else:







