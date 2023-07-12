import itertools

times = int(input())
buff = []
for list in range(times):
    buff.append(input())

for permutation in sorted(itertools.permutations(buff)):
    print(", ".join(permutation))
