# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
"""
Prime Numbers:
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because
they cannot be divided by any other positive integer except for 1 and their own value.
"""
# Functions: get_primes(1, 10) ou get_primes(100, 200) ...

# Using generators

import math

def prime_generator(start: int, end: int):
    """Gera números primos dentro do intervalo [start, end]."""
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield num  # gera um primo por vez


# Exemplo de uso:
print("Primos entre 1 e 10:")
for p in prime_generator(1, 10):
    print(p, end=" ")

print("\n\nPrimos entre 50 e 100:")
for p in prime_generator(50, 100):
    print(p, end=" ")


