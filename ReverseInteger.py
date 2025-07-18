        # Logic : 
# reminder = num % 10
# sum = sum * 10 + reminder
# num = num// 10
# if num < 0 then sign will be - otherwise +.

num = int(input("Enter the number: "))
print("Original number:", num)

def reverse_Int(num):
    result = 0
    sign = 1

    if num < 0:
        sign = -1
        num *= -1

    while num > 0:
        rem = num % 10
        result = result * 10 + rem
        num //= 10

    return sign * result

print("Reversed number:", reverse_Int(num))

        
        
