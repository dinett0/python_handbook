a = int(input())

x = a // 1000
y = a % 1000 // 100
z = a % 100 // 10
t = a % 10

print(y, x, t, z, sep="")
