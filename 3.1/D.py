res = []
while (string := input()) != "":
    if string.endswith("@@@"):
        continue
    else:
        res.append(string.lstrip("##"))
for r in res:
    print(r)
