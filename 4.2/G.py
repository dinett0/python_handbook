import functools

results = []


def enter_results(*new):  # 1. *args
    global results
    results += new


# def get_sum():
#     global results  # global
#     return functools.reduce(lambda x, y: x + y, results[::2]), functools.reduce(
#         lambda x, y: x + y, results[1::2]
#     )  # functools, slicing, lambda


def get_sum():
    global results  # global
    return sum(results[::2]), sum(results[1::2])


def get_average():
    return tuple(i / (len(results) / 2) for i in get_sum())  # tuple comprehension


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
