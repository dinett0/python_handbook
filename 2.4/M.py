a = int(input())
b = int(input())
# number of digits
number = a * b
count = 0
while number != 0:
    number //= 10
    count += 1

for i in range(a):
    for j in range(b):
        print(f"{i+a*j+1:{count}d}", end=" ")
    print()
