from itertools import product

h = int(input())
w = int(input())
numbers = list(range(1, h * w + 1))
temp = 1
for i, j in product(range(h), range(w)):
    index = i * w + j
    print(
        f"{numbers[index]:>{len(str(h * w))}}", end=" " + ("\n" if j == (w - 1) else "")
    )
    temp += 1
