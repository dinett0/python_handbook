a = int(input())
original_number = a
reversed_number = 0
while a != 0:
    reversed_number = (reversed_number * 10) + a % 10
    a //= 10
print("YES" if original_number == reversed_number else "NO")
