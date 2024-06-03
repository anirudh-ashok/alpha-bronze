"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

ttext = texts[0]
ftext = []
for i in ttext:
    nstr = ""
    for num in i:
        if num == "\t":
            nstr += " "
            continue
        nstr += num
    ftext.append(nstr)

print("First record of texts,", ftext[0]," texts", ftext[1],"at time", ftext[2])
number = len(calls)-1
lcall = list(calls[number][0].split("\t"))
print("Last record of calls,", lcall[0],"calls",lcall[1],"at time",lcall[2],", lasting",lcall[3],"seconds")

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""