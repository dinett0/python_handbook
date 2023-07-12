originX, originY = 0, 0

while (direction := input()) != "СТОП":
    x = int(input())
    match direction:
        case "СЕВЕР":
            originY += x
        case "ВОСТОК":
            originX += x
        case "ЮГ":
            originY -= x
        case "ЗАПАД":
            originX -= x
print(originY, originX, sep="\n")
