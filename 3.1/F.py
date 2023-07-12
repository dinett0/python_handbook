queries = int(input())
cnt = 0
for query in range(queries):
    word = input()
    cnt += word.count("зайка")
print(cnt)
