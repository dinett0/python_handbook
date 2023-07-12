a = input()
b = input()
c = input()

if "зайка" not in a:
    a = "\U0010FFFF"
if "зайка" not in b:
    b = "\U0010FFFF"
if "зайка" not in c:
    c = "\U0010FFFF"

print(min(a, b, c), len(min(a, b, c)))
