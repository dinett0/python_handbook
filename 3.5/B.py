from sys import stdin

records = [record.split() for record in stdin.readlines()]
diff = 0
for rec in records:
    diff += int(rec[2]) - int(rec[1])

print(round(diff / len(records)))
