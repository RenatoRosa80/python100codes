# Write a Python Program to Check if a Number is Positive, Negative or Zero.

number = float(input("enter a number: "))

if number > 0:
    print(f" The numer {number} is Positive!")
elif number < 0:
    print(f" The number {number} is Negative!")
else:
    print(f"{number} Its Zero")