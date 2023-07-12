poridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
days = int(input())
for i in range(days // 5 + 1):
    week = 5 if days > 5 else days % 5
    for j in range(week):
        print(poridges[j])
    days -= 5
