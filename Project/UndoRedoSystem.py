class UndoRedoSystem:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_text):
        self.undo_stack.append(self.document)
        self.document = new_text
        self.redo_stack.clear()
        print("Change made.")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(self.document)
        self.document = self.undo_stack.pop()
        print("Undo performed.")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(self.document)
        self.document = self.redo_stack.pop()
        print("Redo performed.")

    def display(self):
        print("Current Document State:")
        print(self.document)


print("Simple Undo Redo System ")


def main():
    system = UndoRedoSystem()

    while True:
        print("\nChoose an option:")
        print("1. Make a Change")
        print("2. Undo Action")
        print("3. Redo Action")
        print("4. Display Document State")
        print("5. Exit")

        choice = input("Enter option (1-5): ")

        if choice == "1":
            new_text = input("Enter new document text: ")
            system.make_change(new_text)
        elif choice == "2":
            system.undo()
        elif choice == "3":
            system.redo()
        elif choice == "4":
            system.display()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()













'''
Dear Student and Teachers, 
We are members of Board of Studies Computer Engineering, 
are very happy to present Second Year Computer Engineering

'''