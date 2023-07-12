a = int(input())
b = int(input())

x = a % 100 // 10
y = a % 10
x1 = b % 100 // 10
y1 = b % 10

maxi = max(x, y, x1, y1)
mini = min(x, y, x1, y1)
middle = (x + y + x1 + y1 - maxi - mini) % 10


print(maxi, middle, mini, sep="")
