porridge1 = int(input())
porridge2 = int(input())
porridges = set()
for i in range(porridge1 + porridge2):
    porridges ^= {input()}
if len(porridges):
    print(len(porridges))
else:
    print("Таких нет")
