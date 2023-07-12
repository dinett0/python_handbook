digits = input()
current = digits[0]
cnt = 0
for digit in digits:
    if digit != current:
        print(current, cnt)
        current = digit
        cnt = 0
    cnt += 1
print(current, cnt)
