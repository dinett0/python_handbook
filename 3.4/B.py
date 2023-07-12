import itertools

sequence1 = input().split(", ")
sequence2 = input().split(", ")
for element1, element2 in zip(sequence1, sequence2):
    print(f"{element1} - {element2}")
