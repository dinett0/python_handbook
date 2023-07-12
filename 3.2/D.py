times_porridge1 = int(input())
times_porridge2 = int(input())
porridge1 = set()
for i in range(times_porridge1):
    porridge1.add(input())

porridge2 = set()
for i in range(times_porridge2):
    porridge2.add(input())

ans = len(porridge1 & porridge2)
print(ans if ans > 0 else "Таких нет")
