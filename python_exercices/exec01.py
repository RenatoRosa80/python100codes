#Write a Python program to do arithmetical operations addition and division.
#Adition

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

print()

#Division

num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))

if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    division_result = num3 / num4
    print(f"Division:  {num3} / {num4} = {division_result}")

