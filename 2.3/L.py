a = int(input())
max = 0
while a != 0:
    max = a % 10 if a % 10 > max else max
    a //= 10
print(max)
