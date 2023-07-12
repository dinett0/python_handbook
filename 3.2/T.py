ans = {}
numbers = input().split("; ")
for i, number in enumerate(numbers):
    numbers[i] = int(number)

numbers = set(numbers)

for i in sorted(numbers):
    index = i
    ans[i] = []
    for j in numbers:
        i = index
        value = j
        while j != 0:
            i, j = j, i % j
        if i == 1:
            ans[index].append(value)

keys = sorted(ans.keys())

for key in keys:
    output = ""
    if ans[key]:
        output += str(key) + " - "
        for i in ans[key]:
            output += str(i) + ", "
        print(output.rstrip(", "))
