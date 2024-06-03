read = open("paint.in")
bs, bf = map(int, read.readline().split())
js, jf = map(int, read.readline().split())
if js >= bf:
    print((jf - js) + (bf - bs), file=open("paint.out", "w"))
elif jf > bf > js:
    print(jf - bs, file=open("paint.out", "w"))
elif bs >= jf:
    print((jf - js) + (bf - bs), file=open("paint.out", "w"))
else:
    print(bf - bs, file=open("paint.out", "w"))

