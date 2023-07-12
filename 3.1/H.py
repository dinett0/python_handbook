queries = int(input())
for query in range(queries):
    word = input()
    found = word.find("зайка")
    print(found + 1 if found != -1 else "Заек нет =(")
