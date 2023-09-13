with open(input(), "r", encoding="UTF-8") as first:
    f_set = set(first.read().split())

with open(input(), "r", encoding="UTF-8") as second:
    s_set = set(second.read().split())

with open(input(), "w", encoding="UTF-8") as ans:
    for item in sorted(f_set ^ s_set):
        print(item, file=ans)
