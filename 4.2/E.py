def to_string(*data, sep=" ", end="\n"):
    res = sep.join(map(str, data))
    return res + end


data = [7, 3, 1, "hello", (1, 2, 3)]
print(to_string(1, 2, 3))
