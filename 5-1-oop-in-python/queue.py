class Queue():
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop(0)
    
    def is_empty(self):
        return len(self.arr) == 0


queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())
