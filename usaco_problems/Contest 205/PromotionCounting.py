read = open("promote.in")
b1, b2 = map(int, read.readline().split())
s1, s2 = map(int, read.readline().split())
g1, g2 = map(int, read.readline().split())
p1, p2 = map(int, read.readline().split())
gold_to_plat = p2 - p1
sliv_to_gold = g2 - g1 + gold_to_plat
bron_to_silv = s2 - s1 + sliv_to_gold
print(bron_to_silv, file=open("promote.out", "w"))
print(sliv_to_gold, file=open("promote.out", "a"))
print(gold_to_plat, file=open("promote.out", "a"))
