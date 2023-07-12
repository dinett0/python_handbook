import itertools

times = int(input())
buff = []
for a in range(times):
    buff.append(input())

for permutation in sorted(itertools.permutations(buff, 3)):
    print(", ".join(permutation))
