class Queue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        res = self.data.pop(0)
        return res

    def is_empty(self):
        return not self.data


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
