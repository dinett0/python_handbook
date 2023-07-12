import itertools

times = int(input())
buff = []
for list in range(times):
    buff.append(input().split(", "))

for seq_num, value in enumerate(sorted(itertools.chain.from_iterable(buff)), 1):
    print(f"{seq_num}. {value}")
