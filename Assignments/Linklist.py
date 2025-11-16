class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Student added successfully!")

    def delete_student(self, roll):
        temp = self.head
        prev = None
        while temp and temp.roll != roll:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Student not found!")
            return
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        print("Student deleted successfully!")

    def update_student(self, roll, name, marks):
        temp = self.head
        while temp:
            if temp.roll == roll:
                temp.name = name
                temp.marks = marks
                print("Student record updated!")
                return
            temp = temp.next
        print("Student not found!")

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"Found: Roll={temp.roll}, Name={temp.name}, Marks={temp.marks}")
                return
            temp = temp.next
        print("Student not found!")

    def sort_students(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if temp.roll > temp.next.roll:
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        print("Records sorted by Roll No!")

    def display_students(self):
        if self.head is None:
            print("No records found.")
            return
        temp = self.head
        print("\n--- Student Records ---")
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next


sll = StudentLinkedList()

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Records")
    print("6. Display All")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        sll.add_student(roll, name, marks)

    elif choice == 2:
        roll = int(input("Enter Roll No to Delete: "))
        sll.delete_student(roll)

    elif choice == 3:
        roll = int(input("Enter Roll No to Update: "))
        name = input("Enter New Name: ")
        marks = float(input("Enter New Marks: "))
        sll.update_student(roll, name, marks)

    elif choice == 4:
        roll = int(input("Enter Roll No to Search: "))
        sll.search_student(roll)

    elif choice == 5:
        sll.sort_students()

    elif choice == 6:
        sll.display_students()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
