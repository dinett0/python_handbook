foods = int(input())
foods_set = set()
for i in range(foods):
    foods_set.add(input())

recipes_count = int(input())
ans = []
for i in range(recipes_count):
    name = input()
    ingredients_count = int(input())
    ingredients_set = set()
    for j in range(ingredients_count):
        ingredients_set.add(input())
    if ingredients_set <= foods_set:
        ans.append(name)
if ans:
    for recipe in sorted(ans):
        print(recipe)
else:
    print("Готовить нечего")
