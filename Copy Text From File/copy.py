
with open("a.txt", 'r') as main_file:
    content = main_file.read()
    print(content)

with open("b.txt", 'w') as copy_file:
    copy_file.write(content)

    
print("Enter copy successfull.")