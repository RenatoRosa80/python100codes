#Write a Python program to convert Celsius to Fahrenheit. 
# F = (C ⋅ 1,8) + 32

celcius = float(input("Enter temperature in Celsius: "))

#Converting C to F

fahrenheit = (celcius - 1.8) + 32

print(f"{celcius} degrees Celsius is equal to  {fahrenheit} degrees Fahr")