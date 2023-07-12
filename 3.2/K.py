dict_names = dict()
times = int(input())
for i in range(times):
    key = input()
    dict_names[key] = dict_names.get(key, 0) + 1

cnt = 0
for value in dict_names.values():
    if value > 1:
        cnt += value

print(cnt)
