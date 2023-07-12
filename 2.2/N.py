a = int(input())

x = a // 100
y = a % 100 // 10
z = a % 10

maxi = max(x, y, z)
mini = min(x, y, z)
middle = (x + y + z) - maxi - mini

print(mini, middle, sep="", end=" ") if mini > 0 else print(
    middle, mini, sep="", end=" "
)
print(maxi, middle, sep="")
