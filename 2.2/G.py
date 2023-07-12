# a = int(input())
# b = int(input())

a = int(input())

print("YES" if a // 1000 == a % 10 and a % 1000 // 100 == a % 100 // 10 else "NO")
