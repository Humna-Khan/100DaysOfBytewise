class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self._insert(root.left, value)
        elif value > root.data:
            root.right = self._insert(root.right, value)
        return root

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return root

        if value < root.data:
            root.left = self._delete(root.left, value)
        elif value > root.data:
            root.right = self._delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self._find_minimum(root.right)
            root.data = min_node.data
            root.right = self._delete(root.right, min_node.data)

        return root

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None or root.data == value:
            return root
        if value < root.data:
            return self._search(root.left, value)
        return self._search(root.right, value)

if __name__ == "__main__":
    bst = BST()
    
    bst.insert(6)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)

    search_value = 2
    result = bst.search(search_value)
    if result:
        print(f"Node with value {search_value} found in BST.")
    else:
        print(f"Node with value {search_value} not found in BST.")

    delete_value = 6
    bst.delete(delete_value)
    print(f"BST after deleting node with value {delete_value}:")
    result = bst.search(delete_value)
    if result:
        print(f"Node with value {delete_value} found in BST.")
    else:
        print(f"Node with value {delete_value} not found in BST.")
