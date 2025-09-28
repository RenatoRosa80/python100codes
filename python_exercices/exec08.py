# Write a Python program to display calendar.
import calendar

year = int(input("Enter the Year: "))
month = int(input("Enter the Month: "))

# Cria objeto TextCalendar
cal = calendar.month(year, month)

# Mostra o mês no formato de texto
print(cal)