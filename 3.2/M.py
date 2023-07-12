dishes = int(input())
dishes_set = set()
for i in range(dishes):
    dishes_set.add(input())

dishes_present_set = set()
days = int(input())
for i in range(days):
    dishes_local = int(input())
    dishes_local_set = set()
    for j in range(dishes_local):
        dishes_local_set.add(input())
    dishes_present_set |= dishes_local_set

ans = dishes_set - dishes_present_set
if ans:
    for recipe in sorted(ans):
        print(recipe)
else:
    print("Готовить нечего")
