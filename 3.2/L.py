dict_names = dict()
times = int(input())
for i in range(times):
    key = input()
    dict_names[key] = dict_names.get(key, 0) + 1

ans = []
for i in sorted(dict_names.items()):
    if i[1] > 1:
        ans.append(i)

if ans:
    for key, value in ans:
        print(f"{key} - {value}")
else:
    print("Однофамильцев нет")
