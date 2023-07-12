import itertools

dimen = [x for x in range(1, int(input()) + 1)]
for x, y in itertools.product(dimen, dimen):
    print(x * y) if y == len(dimen) else print(x * y, end=" ")
