cards, plays = input().split(" ")

def func(list):
    copy = list[:]
    maxe = 0
    for i in copy:
        if i > maxe:
            maxe = i
    p = copy.index(maxe)
    list.remove(maxe)
    count = 0
    for i in range(maxe):
        if count == cards-1:
            count = 0
        list[count] += 1
        count += 1
    list.insert(p, 0)
    return list, p


cards = int(cards)
plays = int(plays)
deck = []
for i in range(cards):
    deck.append(int(input()))

for i in range(plays):
    deck, p = func(deck)
    print(p+1)





