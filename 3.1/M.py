amount = int(input())
numbers = []
for i in range(amount):
    numbers.append(int(input()))
power = int(input())
for number in numbers:
    print(number**power)
