# Reverse Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse the linked list
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev  # New head after reversal

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print("None")

    def reverse(self):
        self.head = reverse_list(self.head)

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
print("Original List:")
ll.display()

ll.reverse()

print("Reversed List:")
ll.display()
