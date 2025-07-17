
with open("a.txt", 'r') as main_file:
    content = main_file.read()
    

with open("b.txt", 'w') as copy_file:
    copy_file.write(content)

    
print("Text copy successful.")