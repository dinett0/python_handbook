import itertools

sequence = input().split()
for seq_num, string in enumerate(sequence, 1):
    print(f"{seq_num}. {string}")
