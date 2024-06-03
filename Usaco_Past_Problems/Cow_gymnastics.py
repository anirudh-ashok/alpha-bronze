read = open("lostcow.in")
s, n = map(int, read.readline().split())
ses = []
for i in range(s):
	lis = list(map(int, read.readline().split()))
	ses.append(lis)

l = []
for j in range(n):
	e = []
	for i in ses:
		e.append(i[j])
	l.append(e)
count = 0
for i in l:
	for j in l:
		var = 0
		if i == j:
			continue
		else:
			for a in range(len(i)):
				if i[a] > j[a]:
					var = 1
				else:
					var = 0
					break
		if var == 1:
			count += 1
			continue


print(count, file=open("gymnastics.out", "w"))
