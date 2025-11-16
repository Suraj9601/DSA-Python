# Real-Time Event Processing System

queue = []


def add_event():
    event_name = input("Enter event name: ")
    queue.append(event_name)
    print(f" Event '{event_name}' added to the queue.\n")


def process_next_event():
    if not queue:
        print("No events to process.\n")
    else:
        event = queue.pop(0)
        print(f" Processing event: '{event}'\n")


def display_pending_events():
    if not queue:
        print(" No pending events.\n")
    else:
        print("Pending events:")
        for i, event in enumerate(queue, start=1):
            print(f"{i}. {event}")
        print()


def cancel_event():
    event_name = input("Enter event name to cancel: ")
    if event_name in queue:
        queue.remove(event_name)
        print(f"Event '{event_name}' canceled.\n")
    else:
        print(f"Event '{event_name}' not found or already processed.\n")


while True:
    print("===== Real-Time Event Processing System =====")
    print("1. Add an Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_event()
    elif choice == "2":
        process_next_event()
    elif choice == "3":
        display_pending_events()
    elif choice == "4":
        cancel_event()
    elif choice == "5":
        print("Exiting Event System.")
        break
    else:
        print("Invalid choice! Please try again.\n")
