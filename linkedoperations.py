#inseartion    (adding at first)

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_start(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node 
    def display(self):
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
obj=Linkedlist()
obj.add_start(10)
obj.add_start(20)
obj.display() 

#adding at last

