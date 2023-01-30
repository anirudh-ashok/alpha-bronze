#Plan
# iterate through the contents of the list to find the greatest number
# Set it to zero and iterate through list adding 1 to each number except for the number with that index
# go 5 times
num, plays = input().split(" ")
num = int(num)
plays = int(plays)
cards = []
for i in range(num):
    x = int(input())
    cards.append(x)

count = 0
for i in range(plays):
    max = 0
    for card in cards:
        if card > max:
            max = card
    ind = cards.index(max)
    cards[ind] = 0

    for nums in range(max+num-1):
        if count != ind:
            cards[count] = cards[count]+1
        count = count + 1
        if count > num-1:
            count = 0
    count = 0
    print(cards)



