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
        if j % 2 == 0:
            print(f"{a*j-i:{count}d}", end=" ")
        else:
            print(f"{i+1+a*(j-1):{count}d}", end=" ")
    print()
