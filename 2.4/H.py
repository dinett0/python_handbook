a = int(input())
max_number = 0
max_name = ""
for i in range(0, a):
    name = input()
    number = int(input())
    sum = 0
    while 0 < number:
        sum += number % 10
        number //= 10
    if sum >= max_number:
        max_number = sum
        max_name = name
print(max_name)
