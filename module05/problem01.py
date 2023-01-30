# First input: number of sudents in class
# SSecond input: number of questions
answer_lis = []
q_lis = []
question, column, s_question = input().split(" ")
column = int(column)
question = int(question)
s_question = int(s_question)
for i in range(question):
    x = input().split(" ")
    answer_lis.append(x)
for j in range(s_question):
    y = input()
    q_lis.append(y)

cout = 0

students = []
for i in range(question):
    students.append(i)
arr = []
for i in range(column):
    for j in q_lis:
      #  print(students)
        x,y = j.split(" ")
        x = int(x)-1
        y = int(y)
        for e in students:
            if students[e] != -1 and int(answer_lis[e][x]) != y:
                students[e] = -1
            else:
                continue
count = 0
for i in students:
    if i != -1:
        count += 1

print(count)




'''
for j in q_lis:   
    for i in answer_lis:
        for e in i:
   '''