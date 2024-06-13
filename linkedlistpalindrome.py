class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def isPalindrome(self):
        if not self.head or not self.head.next:
            print("The linked list is a palindrome.")
            return
        
        # Find the middle of the linked list
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the linked list
        reversed_list = self.reverseList(slow)
        
        # Compare the first half and the reversed second half
        first_half, second_half = self.head, reversed_list
        while second_half:
            if first_half.data != second_half.data:
                print("The linked list is not a palindrome.")
                return
            first_half = first_half.next
            second_half = second_half.next
        
        print("The linked list is a palindrome.")

    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

def LList():
    data = input("Enter the elements of the linked list separated by '->' or spaces: ")
    elements = data.replace('->', ' ').split()
    linked_list = LinkedList()
    if elements:
        linked_list.head = Node(int(elements[0]))
        current = linked_list.head
        for element in elements[1:]:
            current.next = Node(int(element))
            current = current.next
    return linked_list

if __name__ == "__main__":
    l = LList()
    l.printList()
    l.isPalindrome()
