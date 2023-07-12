radix = 2
numbers = input()
ans = []
for n in numbers.split():
    number = int(n)
    binary = ""
    while number > 0:
        binary += str(number % radix)
        number //= radix
    ans.append(
        {"digits": len(binary), "units": binary.count("1"), "zeros": binary.count("0")}
    )

print(ans)
