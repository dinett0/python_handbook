from sys import stdin

lines = stdin.readlines()
for line in lines:
    s = line[: line.index("#")]
    if s:
        print(s)
