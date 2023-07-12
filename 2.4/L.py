a = int(input())
b = int(input())

# number of digits
number = a * b
count = 0
while number != 0:
    number //= 10
    count += 1

for i in range(a):
    for j in range(1, b + 1):
        print(f"{i*b+j:{count}d}", end=" ")
    print()
