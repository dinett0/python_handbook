porridge1 = int(input())
porridge2 = int(input())
porridges = set()
for i in range(porridge1 + porridge2):
    porridges ^= {input()}
if len(porridges):
    for i in sorted(porridges):
        print(i)
else:
    print("Таких нет")
