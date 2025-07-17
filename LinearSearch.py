arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
target = input("Enter element you want to search : ")

def linear (arr, target) : 
    for i in range(len(arr)):
        if arr[i] == target:
            print("Element is Found at",i+1, "Position.")
            return
        
    print("Element not found.")

linear(arr, target)
