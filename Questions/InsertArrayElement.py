arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original Array :", arr)

element = int(input("Enter the element do you want insert : "))
position =   int(input("Enter position of element you want add : ")) 
position -= 1

arr.insert(position,element)
print(arr)