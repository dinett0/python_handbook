import itertools

participants_number = int(input())
participants = [input() for _ in range(participants_number)]
for first, second in itertools.combinations(participants, 2):
    print(f"{first} - {second}")
