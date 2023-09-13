filename = input()

with open(filename, "r") as file_input:
    numbers = [int(x) for x in file_input.read().split()]

print(len(numbers))
print(len([x for x in numbers if x > 0]))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(f"{sum(numbers)/len(numbers):.3}")
