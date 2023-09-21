def recursive_sum(*members):
    if len(members) == 0:
        return 0
    return members[0] + recursive_sum(*members[1:])


print(recursive_sum(1, 2, 3))
