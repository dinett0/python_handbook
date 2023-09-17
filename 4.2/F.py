def all_fit(first, second):
    flag = True
    for f, s in zip(first, second):
        if f < s:
            flag = False
    return flag


def order(*names):
    global in_stock

    menu = {
        "Эспрессо": (1, 0, 0),
        "Капучино": (1, 3, 0),
        "Макиато": (2, 1, 0),
        "Кофе по-венски": (1, 0, 2),
        "Латте Макиато": (1, 2, 1),
        "Кон Панна": (1, 0, 1),
    }

    for name in names:
        if all_fit(in_stock.values(), menu[name]):
            for key, spending in zip(in_stock.keys(), menu[name]):
                in_stock[key] -= spending
            return name
    return "К сожалению, не можем предложить Вам напиток"


in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(
    order(
        "Эспрессо",
        "Капучино",
        "Макиато",
        "Кофе по-венски",
        "Латте Макиато",
        "Кон Панна",
    )
)
print(
    order(
        "Эспрессо",
        "Капучино",
        "Макиато",
        "Кофе по-венски",
        "Латте Макиато",
        "Кон Панна",
    )
)
