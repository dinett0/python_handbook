from sys import stdin

lines = [line.rstrip("\n") for line in stdin]

for line in lines[: len(lines) - 1]:
    if lines[-1].lower() in line.lower():
        print(line)
