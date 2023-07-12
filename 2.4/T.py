number = int(input())
max = 0
max_radix = 0

for radix in range(2, 11):
    # debug_ = ""
    tmp = number
    digits_sum = 0
    while tmp > 0:
        digits_sum += tmp % radix
        # debug_ += str(tmp % radix)
        tmp //= radix
    # print(f"digits sum for {radix}: {digits_sum}")
    if max < digits_sum:
        max = digits_sum
        max_radix = radix
    # print(f"{radix}:{debug_[::-1]:0>10}")
print(max_radix)
