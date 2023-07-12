# a = int(input())
# b = int(input())

a = int(input())

x = a // 100
y = a % 100 // 10
z = a % 10

maxi = max(x, y, z)
mini = min(x, y, z)

print("YES" if maxi + mini == ((x + y + z) - maxi - mini) * 2 else "NO")
