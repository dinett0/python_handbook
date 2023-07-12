a = int(input())
sum = 0
for i in range(0, a):
    n = int(input())
    while n > 0:
        sum += n % 10
        n //= 10
print(sum)
