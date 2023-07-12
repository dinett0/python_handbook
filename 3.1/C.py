length = int(input())
queries = int(input())
headings = []
for query in range(queries):
    headings.append(input())
for heading in headings:
    if len(heading) > length:
        print(heading[: length - 3] + "...")
    else:
        print(heading)
