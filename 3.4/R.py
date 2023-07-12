import itertools

expr = input()
print("a b c f")
for a, b, c in itertools.product([0, 1], repeat=3):
    print(f"{a} {b} {c} {int(eval(expr))}")
