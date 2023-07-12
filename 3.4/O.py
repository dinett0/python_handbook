import itertools

times = int(input())
buff = []
for list in range(times):
    buff.append(input().split(", "))

for permut in sorted(itertools.permutations(itertools.chain.from_iterable(buff), 3)):
    print(" ".join(permut))
