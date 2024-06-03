read = open("censor.in")
n = read.readline()
omit = read.readline()
if omit[:-1] == "\n":
    omit = omit[:-1]
omit = str(omit)
processed = ""
for i in n:
    processed += i
    if len(processed) < 3:
        continue
    sub = processed[-3:]
    print(sub)
    if sub == omit:
        processed = processed[:-3]

print(processed)
with open("censor.out", "w") as f:
    f.write(processed)


