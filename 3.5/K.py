import json

source = input()
stats = input()

with open(source, "r") as file_input:
    numbers = [int(x) for x in file_input.read().split()]

serialize = {
    "count": len(numbers),
    "positive_count": len([x for x in numbers if x > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": sum(numbers),
    "average": round(sum(numbers) / len(numbers), 2),
}

with open(stats, "w") as file_output:
    json.dump(serialize, file_output, indent=4)
