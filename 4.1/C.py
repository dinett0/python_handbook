def number_length(number):
    res = 0
    number = abs(number)
    while number:
        number //= 10
        res += 1
    return res
