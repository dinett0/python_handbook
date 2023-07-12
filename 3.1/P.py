length = int(input())
queries = int(input())
headings = []

for query in range(queries):
    headings.append(input())

whole = "+".join(headings)
ans = whole[: length - 3 + whole[: length - 3].count("+")] + "..."
for line in ans.split("+"):
    print(line)
