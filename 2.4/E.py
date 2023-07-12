a = int(input())
sum = 0
appeared = 0
for i in range(0, a):
    while (n := input()) != "ВСЁ":
        if n == "зайка":
            appeared = True
    sum += appeared
    appeared = 0

print(sum)
