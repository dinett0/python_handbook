# a = int(input())
# b = int(input())
# c = int(input())
d = input()
a = int(input())
b = int(input())
c = int(input())

x = f"{b}кг * {a}руб/кг"
y = f"{b*a}руб"
z = f"{c}руб"
t = f"{c - b*a}руб"

print("================Чек================")
print("Товар:" + " " * (29 - len(d)) + d)
print("Цена:" + " " * (30 - len(x)) + x)
print("Итого:" + " " * (29 - len(y)) + y)
print("Внесено:" + " " * (27 - len(z)) + z)
print("Сдача:" + " " * (29 - len(t)) + t)
print("===================================")
