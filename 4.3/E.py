def result_accumulator(func):
    storage = []

    def wrapper(*args, method="accumulate", **kwargs):
        nonlocal storage
        storage.append(func(*args, **kwargs))
        if method == "drop":
            tmp = storage
            storage = []
            return tmp
        return None

    return wrapper


@result_accumulator
def a_plus_b(a, b):
    return a + b


@result_accumulator
def func(str):
    return str


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))

print(func("ABC"))
print(func("DEF"))
print(func("ABC", method="drop"))
