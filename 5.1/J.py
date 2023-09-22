class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        res = self.data.pop()
        return res

    def is_empty(self):
        return not self.data


stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())
