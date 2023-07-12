a = int(input())
b = int(input())
b += 1 if b > a else -1
step = -1 if b < a else 1

for i in range(a, b, step):
    print(i, end=" ")
