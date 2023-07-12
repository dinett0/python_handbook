x = float(input())
y = float(input())

area_global = True if (x**2 + y**2) <= 100 else False

area_1 = True if (5 / 3) * x + (35 / 3) >= y and 0 <= y <= 5 and x <= 0 else False
area_2 = True if (x**2 + y**2) <= 25 and x > 0 and y > 0 else False
area_3 = True if (1 / 4) * (x + 1) ** 2 - 9 <= y and y <= 0 else False

if not area_global:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif area_1 or area_2 or area_3:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")
