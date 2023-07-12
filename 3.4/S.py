import itertools

expr = input()
letters = sorted({x for x in expr if x.isupper()})
print(" ".join(letters) + " F")

for ones_zeros in itertools.product([0, 1], repeat=len(letters)):
    values = {letter: one_zero for letter, one_zero in zip(letters, ones_zeros)}
    for i in ones_zeros:
        print(i, end=" ")
    print(int(eval(expr, None, values)))
