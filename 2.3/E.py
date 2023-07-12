# E
sum = 0
while (n := input()) != "0":
    n = float(n) if "." in n else int(n)
    if n >= 500:
        n *= 0.9
    sum += n
print(sum)
