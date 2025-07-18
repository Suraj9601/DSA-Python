arr = [1, 2, 4, 5,  6, 7, 8, 9, 10]

# arr.reverse()
# print(arr )

for i in range(len(arr)):
    arr[i] = arr[len(arr)-1]
    


print(arr)