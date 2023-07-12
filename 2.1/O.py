a = int(input())
b = int(input())
c = int(input())

minutes = (b + c % 60) % 60
hours = ((a + c // 60) + (b + c % 60) // 60) % 24

print(f"{hours:02d}:{minutes:02d}")
