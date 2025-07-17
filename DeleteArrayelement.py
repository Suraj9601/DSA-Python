arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

element = int(input("Enter element you want to delete: "))
found = False

for i in range(len(arr)):
    if arr[i] == element:
        arr.pop(i)
        found = True
        break 
if found:
    print("Updated array:", arr)
else:
    print("Invalid array element")
