a = int(input())
b = int(input())
# number of digits
number = a * b
count = 0
while number != 0:
    number //= 10
    count += 1

for i in range(1, a + 1):
    concat = ""
    for j in range(i, b * i + 1, i):
        x = f"{j:{count}d}"
        center_align = 3 if count == 1 else 5 + 2 * (count // 2 - 1)
        concat += f"{x:^{center_align}}" + ("" if j >= b * i else "|")
    print(concat)
    if i < a:
        print("-" * len(concat))
