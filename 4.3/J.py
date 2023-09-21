def make_linear(x):
    res = []
    for i in x:
        if isinstance(i, (list, tuple)):
            res += make_linear(i)
        else:
            res.append(i)
    return res


result = make_linear([1, [2, [3, 4]], 5, 6])

print(result)
