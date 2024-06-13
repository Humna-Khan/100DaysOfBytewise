class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtTail(1)
    ll.insertAtTail(2)
    ll.insertAtTail(3)
    ll.insertAtTail(4)
    ll.insertAtTail(5)

    print("Original Linked List:")
    ll.display()

    ll.reverse()

    print("\nReversed Linked List:")
    ll.display()
