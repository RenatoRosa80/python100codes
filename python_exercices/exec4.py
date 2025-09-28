#Write a Python program to swap two variables.

a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")

print(f"Temporary variables are: a = {a}, b = {b}")
print()

temp = a
a = b
b = temp
print(f"Swapped values are a = {a}, b = {b}")
print()
