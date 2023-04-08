num = (input())
past = len(str(num))
c = 0


def getBaseTen(binaryVal):
    count = 0

    # reverse the string
    binaryVal = binaryVal[::-1]

# go through the list and get the value of all 1's
    for i in range(0, len(binaryVal)):
        if (binaryVal[i] == "1"):
            count += 2 ** i

    return count
num = getBaseTen(num) * 17

def baseTwo(Val):
    count = ""
    while Val != 0:
        count += str(Val % 2)
        Val = Val // 2

    return count[::-1]

print(baseTwo(num))
