t = int(input())


def func(k, cards, scards):
    for i in scards:
        count = 0
        v = cards.count(i)
        if v == len(cards):
            return len(cards) - k + 1
        if v >= k:
            ind = scards.index(i)
            if ind == len(scards) - 1:
                repla = scards[0]
            else:
                repla = scards[ind + 1]
            for e in range(len(cards)):
                if cards[e] == i:
                    if count == k - 1:
                        cards.pop(e)
                        break
                    else:
                        count += 1
                        cards[e] = repla
    print(cards)
    '''
    if len(cards) < k:
        return len(cards)
    else:
        func(k, cards, scards)
    '''
    if len(cards) < k:
        return cards
    else:
        func(3, cards, [1,4])


e = (func(3, [4, 1, 1, 4, 4], [1, 4]))
print(e)
