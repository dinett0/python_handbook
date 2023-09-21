def recursive_digit_sum(x):
    if x == 0:
        return 0
    return x % 10 + recursive_digit_sum(x // 10)


print(recursive_digit_sum(123))
