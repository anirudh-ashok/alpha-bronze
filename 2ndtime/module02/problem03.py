'''cow_num, num = input().split(" ")
diff = list(input().split(" "))
'''
lis = [1,2,3,4,6,7]
def cow_work(start, move, lis):
    #This function should return changed list and new start poin
    moo = start + move
    if moo < len(lis) - 1:
        lis.pop(moo - 2)
        return lis, moo
    else:
        p = (len(lis) - 1) % moo
        lis.pop(p)
        return lis, p
print(cow_work(1,5, lis))