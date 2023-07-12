# a = int(input())
# b = int(input())

a = int(input())

x = a // 100 + a % 100 // 10
y = a % 100 // 10 + a % 10

print(x, y, sep="") if x > y else print(y, x, sep="")
