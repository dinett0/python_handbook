a = int(input())
step = 1
i = 1
max_len = 0
while i <= a:
    line = ""
    for j in range(i, i + step):
        if j <= a:
            line += str(j) + " "
    i += step
    step += 1
    if len(line) > max_len:
        max_len = len(line)
step = 1
i = 1
while i <= a:
    line = ""
    for j in range(i, i + step):
        if j <= a:
            line += str(j) + (" " if j < i + step - 1 else "")
    print(f"{line:^{max_len-1}}")
    i += step
    step += 1
