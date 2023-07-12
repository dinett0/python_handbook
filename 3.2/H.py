times = int(input())
dict_porridge = {}

for i in range(times):
    data = input().split()
    for key in data[1:]:
        dict_porridge[key] = dict_porridge.get(key, []) + [data[0]]

ans = sorted(dict_porridge.get(input(), []))
if ans:
    for i in ans:
        print(i)
else:
    print("Таких нет")
