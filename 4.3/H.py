def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        yield x
        y, x = x + y, y


print(*fibonacci(10), sep=", ")
