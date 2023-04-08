q, task = input().split(" ")
q = int(q)
task = int(task)
question = []
tasks = []
def time_when(ques, lis):
    count = 0
    c = 0
    for i in lis:
        count += 1
        c = c+i
        if c > ques:
            break
    return count

for i in range(q):
    x = int(input())
    tasks.append(x)

for i in range(task):
    y = int(input())
    question.append(time_when(y,tasks))

for i in question:
    print(i)



