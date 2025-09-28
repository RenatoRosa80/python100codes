# Write a Python Program to Print all Prime Numbers in an Interval of 1-100.
"""
Prime Numbers:
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because
they cannot be divided by any other positive integer except for 1 and their own value.
"""



start = 1
end = 100

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:  # 0 e 1 não são primos
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
