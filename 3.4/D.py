import itertools

sequence = [x + " " for x in input().split()]
for i in itertools.accumulate(sequence):
    print(i.strip())
