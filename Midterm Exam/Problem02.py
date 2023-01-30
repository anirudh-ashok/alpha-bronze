moo = input()
echo = input()
max_e = 0
count = 0

for j in range(1):
    for i in range(len(moo)):#used to be echo
        count = echo.find(moo[0:i])
        if count != -1:
            if len(moo[0:i]) > max_e:
                max_e = len(moo[0:i])
                lar = moo[0:i]
        count = 0

for j in range(1):
    for i in range(len(echo)):#used to be echo
        count = moo.find(echo[0:i])
        if count != -1:
            if len(echo[0:i]) > max_e:
                max_e = len(echo[0:i])
                lar = echo[0:i]
        count = 0
print(max_e)
'''
s = 'Johny Johny Yes Papa'
result = s.find('Johny')

print(result)
'''
'''
moo = input()
echo = input()
max_e = 0
count = 0

for j in range(1):
    for i in range(len(moo)):#used to be echo
        count = echo.find(moo[0:i])

        if count != -1:
            if len(moo[0:i]) > max_e:
                max_e = len(moo[0:i])
        count = 0

    moo.replace(moo[j], "")
print(max_e)
'''