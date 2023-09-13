# with open("3.5/first.txt", "r", encoding="UTF-8") as first:
#     content = first.read()

# print(content.strip().replace("\t", ""))

with open(input(), "r", encoding="UTF-8") as first:
    content = first.readlines()

with open(input(), "w", encoding="UTF-8") as second:
    for s in content:
        ans = " ".join(s.strip().replace("\t", "").split())
        if ans:
            print(ans, file=second)
