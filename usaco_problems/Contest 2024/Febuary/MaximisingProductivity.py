n, q = map(int, input().split())
close = list(map(int, input().split()))
travel = list(map(int, input().split()))
diff = []
for i in range(n):
    c = close[i]
    t = travel[i]
    diff.append((c - t))
diff.sort()
answers = []


def last(low, high, key):
    while high - low != 1:
        mid = (low+high)//2
        if diff[mid] == key:
            if diff[mid-1] == diff[mid]:
                low = mid-1
            return mid
        if diff[mid] < key:
            low = mid + 1
        elif diff[mid] > key:
            high = mid - 1
    return high



for i in range(q):
    v, s = (map(int, input().split()))
    count = last(0, n-1, s)
    '''
    for e in diff:
        if e > s:
            count += 1
      '''
    print(count)
    if count >= v:
        answers.append("YES")
        continue
    answers.append("NO")

for i in answers:
    print(i)
