def merge_sort(x):
    def merge(first, second):
        f_pointer = 0
        s_pointer = 0
        res = []
        while f_pointer < len(first) and s_pointer < len(second):
            if first[f_pointer] > second[s_pointer]:
                res.append(second[s_pointer])
                s_pointer += 1
            else:
                res.append(first[f_pointer])
                f_pointer += 1

        res += first[f_pointer:]
        res += second[s_pointer:]
        return res

    if len(x) < 2:
        return x
    left = merge_sort(x[: len(x) // 2])
    right = merge_sort(x[len(x) // 2 :])

    return merge(left, right)
