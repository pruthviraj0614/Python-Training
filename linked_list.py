#1
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)        
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4
current=node1
for i in range(4):
    print(current.data)
    current=current.next
print(node1.data,node1.next.data,node1.next.next.data,node1.next.next.next.data)

  


