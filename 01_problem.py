

# Interchange first and last digit of a three-digit number

num = int(input("Enter a three-digit number: "))

first = num // 100
middle = (num // 10) % 10
last = num % 10

new_num = last * 100 + middle * 10 + first

print("Number after interchanging first and last digit:", new_num)
