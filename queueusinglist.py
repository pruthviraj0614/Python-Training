class Node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next=None
class Deque:
    def __init__(self):
       self.frount=None
       self.rear=None
    def insert_front(self,data):
        new_node = Node(data)
        if self.frount is None:
            self.frount = self.rear = new_node
        else:
            new_node.next = self.frount
            self.frount.prev = new_node
            self.frount = new_node
    def insert_rear(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.frount = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
    def delete_front(self):
        if self.front is None:
            return None
        data =  self.front.data
        self.front=self.front.next
        if self.front.prev==None:
            return None
        else:
            self.front.prev=None
            return data
    def delete_rear(self):
        if self.rear is None:
            return None
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
            return data
    def get_front(self):
        if self.front is None:
          return None
        return self.front.data
    def get_rear(self):
        if self.rear is None:
          return None
        return self.rear.data
    def is_empty(self):
        return self.front is None
    def size(self):
        count = self.front
        curr = curr.next
        return count
    def display(self):
        if self.front is None:
            print("Empty")
            return
        curr = self.front
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()
dq=Deque()
dq.insert_front(5)
dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(1)
dq.display()
print('Front',dq.get_front())
print('Rear',dq.get_rear())
dq.delete_front()
dq.delete_rear()
dq.display()
print('Front:',dq.get_front())
print('Size:',dq.size())