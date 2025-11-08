string = input("Enter a String or Word: ")

processed = ""
for i in range(len(string)):
    ch = string[i]
    if "A" <= ch <= "Z":
        ch = chr(ord(ch) + 32)
    if ch != " ":
        processed += ch

stack = []
for i in range(len(processed)):
    stack += [processed[i]]  

reversed_str = ""
while len(stack) > 0:
    reversed_str += stack[len(stack) - 1]
    stack = stack[: len(stack) - 1]  

is_palindrome = True
for i in range(len(processed)):
    if processed[i] != reversed_str[i]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"'{string}' is a Palindrome.")
else:
    print(f"'{string}' is NOT a Palindrome.")
