class EventSystem:
    def __init__(self):
        self.queue = []  

    def add_event(self, event_name):
        self.queue.append(event_name)
        print(f"✅ Event '{event_name}' added to the queue.\n")

    def process_next_event(self):
        if not self.queue:
            print("⚠️ No events to process.\n")
        else:
            event = self.queue.pop(0)   # remove first (FIFO)
            print(f"⚙️ Processing event: '{event}'\n")

    def display_pending_events(self):
        if not self.queue:
            print("🕒 No pending events.\n")
        else:
            print("📋 Pending events:")
            for i, event in enumerate(self.queue, start=1):
                print(f"{i}. {event}")
            print()

    def cancel_event(self, event_name):
        if event_name in self.queue:
            self.queue.remove(event_name)
            print(f"❌ Event '{event_name}' canceled.\n")
        else:
            print(f"⚠️ Event '{event_name}' not found or already processed.\n")


# main menu
if __name__ == "__main__":
    system = EventSystem()

    while True:
        print("===== Real-Time Event Processing System =====")
        print("1. Add an Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel an Event")
        print("5. Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '1':
            event_name = input("Enter event name: ")
            system.add_event(event_name)
        elif choice == '2':
            system.process_next_event()
        elif choice == '3':
            system.display_pending_events()
        elif choice == '4':
            event_name = input("Enter event name to cancel: ")
            system.cancel_event(event_name)
        elif choice == '5':
            print("👋 Exiting Event System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")
