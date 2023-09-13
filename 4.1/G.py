def can_eat(knight, unit):
    x = abs(unit[0] - knight[0])
    y = abs(unit[1] - knight[1])
    return x + y == 3
