cnt = 0
while (line := input()) != "Приехали!":
    if "зайка" in line:
        cnt += 1
print(cnt)
