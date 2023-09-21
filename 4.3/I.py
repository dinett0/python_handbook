def cycle(n):
    i = 0
    while True:
        yield n[i % len(n)]
        i += 1


print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
