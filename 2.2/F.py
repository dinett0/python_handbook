# a = int(input())
# b = int(input())
a = int(input())
print(
    "YES" if (a % 100 == 0 and a % 400 == 0) or (a % 100 != 0 and a % 4 == 0) else "NO"
)
