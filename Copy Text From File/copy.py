
with open("a.txt", 'r') as main_file:
    content1 = main_file.read()
    
with open("b.txt", 'r') as check_file:
    content2 = check_file.read()
    
    if (content2 != content1):
        with open("b.txt", 'w') as copy_file:
            copy_file.write(content1)
            print("Text copy successful.")
    else:
        print("Text already copyed")

