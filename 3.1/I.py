res = []
while (string := input()) != "":
    res.append(string.split("#")[0])
for token in res:
    if token != "":
        print(token)
