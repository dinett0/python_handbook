queries = int(input())
flag = True
for query in range(queries):
    word = input()
    if word[0] not in ("абв"):
        flag = False
print("YES" if flag else "NO")
