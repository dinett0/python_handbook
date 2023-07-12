lines_number = int(input())
lines = []
for i in range(lines_number):
    lines.append(input())
query = input()
for line in lines:
    if query.lower() in line.lower():
        print(line)
