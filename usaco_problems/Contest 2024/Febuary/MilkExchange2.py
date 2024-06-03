n, m = map(int, input().split())
dire = list(input())
cap = list(map(int, input().split()))
print(dire)

def exchange(lis):
    count = 0
    for i in range(n):
        curr = lis[i]
        pos = 0
        if dire[i] == "L":
            pos = i - 1
            swap = lis[pos]
        else:
            if i == n - 1:
                pos = 0
                swap = lis[pos]
            else:
                pos = i + 1
                swap = lis[pos]
        lis[i] -= 1
        
    return count, lis

total = 0
for i in range(m):
    lab, cap = exchange(cap)
    total = lab

print(total)
