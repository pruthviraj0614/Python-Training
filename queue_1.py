from queue import Queue
class CustomQueue(Queue):
    def __init__(self, max_size):
        super().__init__(maxsize=max_size)

    def is_empty(self):
        return self.qsize() == 0

    def is_full(self):
        return self.qsize() == self.maxsize

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
        else:
            self.put(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.get()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            # Temporarily remove item and put it back
            item = self.get()
            self.put(item)
            # Reordering queue to maintain original sequence
            for _ in range(self.qsize() - 1):
                self.put(self.get())
            return item

    def display(self):
        print('Queue size:', self.qsize())

# Example usage
n = CustomQueue(5)
n.enqueue(10)
n.enqueue(20)
n.enqueue(30)
print("Peek:", n.peek())
n.display()
