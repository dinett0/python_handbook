numbers = input()
power = int(input())
for number in numbers.split():
    print(int(number) ** power, end=" ")
