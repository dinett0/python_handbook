a = int(input())
step = 1
i = 1
while i <= a:
    for j in range(i, i + step):
        if j <= a:
            print(j, end=" ")
    print()
    i += step
    step += 1
   