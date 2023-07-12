a = int(input())
b = int(input())
c = int(input())

first = max(a, b, c)
last = min(a, b, c)
middle = a + b + c - first - last

if first == a:
    name_first = "Петя"
elif first == b:
    name_first = "Вася"
else:
    name_first = "Толя"

if last == a:
    name_last = "Петя"
elif last == b:
    name_last = "Вася"
else:
    name_last = "Толя"

if middle == a:
    name_middle = "Петя"
elif middle == b:
    name_middle = "Вася"
else:
    name_middle = "Толя"

print(
    f"          {name_first}          ",
    f"  {name_middle}  ",
    f"                  {name_last}  ",
    "   II      I      III   ",
    sep="\n",
)
