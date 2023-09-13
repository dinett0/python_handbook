offset = int(input())
with open("public.txt", "r") as numbers:
    string = numbers.read()

ans = []
for c in string:
    if c.isalpha():
        start = "A" if c.isupper() else "a"
        ans.append(chr((ord(c) + offset - ord(start)) % 26 + ord(start)))
    else:
        ans.append(c)

with open("private.txt", "w") as result:
    result.write("".join(ans))
