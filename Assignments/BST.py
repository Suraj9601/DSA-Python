# Binary Search Tree Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a new node
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


# Search a value in BST
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Find the minimum value node
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Delete a node
def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Node with one or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Display (Inorder Traversal)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# --- MAIN PROGRAM ---
root = None

while True:
    print("\n=== Binary Search Tree Menu ===")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display (Inorder)")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value to insert: "))
        root = insert(root, val)
        print(f"{val} inserted successfully.")
    elif ch == 2:
        key = int(input("Enter value to search: "))
        if search(root, key):
            print(f"{key} found in the tree.")
        else:
            print(f"{key} not found.")
    elif ch == 3:
        key = int(input("Enter value to delete: "))
        root = delete(root, key)
        print(f"{key} deleted (if existed).")
    elif ch == 4:
        print("Inorder Traversal (Ascending order):")
        inorder(root)
        print()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
