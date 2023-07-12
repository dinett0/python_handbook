inputs = int(input())
cnt = 0
for i in range(inputs):
    a = int(input())
    original_number = a
    reversed_number = 0
    while a != 0:
        reversed_number = (reversed_number * 10) + a % 10
        a //= 10
    if original_number == reversed_number:
        cnt += 1
print(cnt)
