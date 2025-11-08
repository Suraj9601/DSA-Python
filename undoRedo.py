# Stack to store document history
undo_stack = []

# Current document
document = ""

def make_change(new_text):
    global document
    undo_stack.append(document)   # save previous version
    document = new_text
    print("Change made successfully!")

def display_document():
    print("Current Document:", document)


# --- Example Usage ---
make_change("Hello")
display_document()

make_change("Hello World")
display_document()

make_change("Hello World!!!")
display_document()
