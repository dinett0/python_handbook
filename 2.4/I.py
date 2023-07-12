a = int(input())
res = ""
for i in range(0, a):
    number = int(input())
    max_digit = 0
    while 0 < number:
        if number % 10 >= max_digit:
            max_digit = number % 10
        number //= 10
    res += str(max_digit)
print(res)
