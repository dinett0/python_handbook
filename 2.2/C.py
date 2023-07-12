a = int(input())
b = int(input())
c = int(input())

maximum = max(a, b, c)

print("Петя" if maximum == a else "Вася" if maximum == b else "Толя")
