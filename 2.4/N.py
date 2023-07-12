a = int(input())
b = int(input())
# number of digits
number = a * b
count = 0
while number != 0:
    number //= 10
    count += 1
for i in range(a):
    x = range(1, b + 1) if i % 2 == 0 else range(b, 0, -1)
    for j in x:
        print(f"{i*b+j:{count}d}", end=" ")
    print()
