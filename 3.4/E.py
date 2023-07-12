import itertools

sequence1 = input().split(", ")
sequence2 = input().split(", ")
sequence3 = input().split(", ")
for seq_num, value in enumerate(
    sorted(itertools.chain(sequence1, sequence2, sequence3)), 1
):
    print(f"{seq_num}. {value}")
