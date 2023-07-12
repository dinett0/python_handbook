import itertools

numbers = [float(x) for x in input().split()]
for i in itertools.count(numbers[0], numbers[2]):
    if i > numbers[1]:
        break
    print(f"{round(i, 2):0.2f}")
