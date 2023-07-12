a = int(input())
b = int(input())

y = a % 1000 // 100
z = a % 100 // 10
t = a % 10

y2 = b % 1000 // 100
z2 = b % 100 // 10
t2 = b % 10

print((y + y2 % 10) % 10, (z + z2) % 10, (t + t2) % 10, sep="")
