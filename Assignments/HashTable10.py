# Hash table size
SIZE = 10
hash_table = [[] for _ in range(SIZE)]


def hash_function(key):
    return key % SIZE


def insert(key, value):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print(f"Updated existing key {key} with new value '{value}'.")
            return
    hash_table[index].append([key, value])
    print(f"Inserted key={key}, value='{value}' at index {index}.")


def search(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            print(f"Found: key={key}, value='{pair[1]}' (index {index})")
            return
    print(f"Key {key} not found!")


def delete(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print(f"Deleted key={key} from index {index}.")
            return
    print(f"Key {key} not found to delete!")


def display():
    print("\nHash Table Contents:")
    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")
    print("-" * 40)


while True:
    print("\n====== HASH TABLE IMPLEMENTATION (Chaining) ======")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        key = int(input("Enter key (integer): "))
        value = input("Enter value: ")
        insert(key, value)

    elif ch == "2":
        key = int(input("Enter key to search: "))
        search(key)

    elif ch == "3":
        key = int(input("Enter key to delete: "))
        delete(key)

    elif ch == "4":
        display()

    elif ch == "5":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
