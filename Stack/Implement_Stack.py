stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print("Elemet added : ",stack)

removed = stack.pop()
print("Removed Element : ",removed)
print(stack)

top = stack[-1]
print("Top Element : ",top)

if not stack:
    print("Stack is Empty.")
else:
    print("Stack is not Empty.")