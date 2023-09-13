def merge(first, second):
    first_p = 0
    second_p = 0
    res = []
    while first_p < len(first) and second_p < len(second):
        if first[first_p] > second[second_p]:
            res.append(second[second_p])
            second_p += 1
        else:
            res.append(first[first_p])
            first_p += 1

    if first_p < len(first):
        res += first[first_p:]
    else:
        res += second[second_p:]
    return tuple(res)


print(merge((7, 12), (1, 9, 50)))
