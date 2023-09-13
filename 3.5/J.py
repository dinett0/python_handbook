with open(input(), "r", encoding="UTF-8") as first:
    content = first.readlines()
    tail = int(input())
    for s in content[len(content) - tail :]:
        print(s.rstrip())
