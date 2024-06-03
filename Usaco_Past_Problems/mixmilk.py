# USACO 2018 December Contest, Bronze
#
# Problem 1. Mixing Milk

read = open("mixmilk.in")
b1 = list([int(i) for i in read.readline().split()])
b2 = list([int(i) for i in read.readline().split()])
b3 = list([int(i) for i in read.readline().split()])


class Bucket:
    def __init__(self, volume, quantity):
        self.volume = volume
        self.quantity = quantity
        self.remaining_volume = 0
        self.current_quantity = 0


bucket1 = Bucket(b1[0], b1[1])
bucket2 = Bucket(b2[0], b2[1])
bucket3 = Bucket(b3[0], b3[1])

switch_num = 100
pails = 3
# buckets = (b1, b2, b3)
buckets = (bucket1, bucket2, bucket3)
previous_bucket = buckets[0]
for i in range(1, switch_num):
    '''
    1. 
    '''
    current_bucket = buckets[i % pails]
    # Get this formula right
    current_bucket.current_capacity += (previous_bucket.current_quantity % current_bucket.volume)

    previous_bucket = current_bucket
    for j in range(pails):
        print(f"  {j}: {buckets[j].volume}")
