# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
"""
Prime Numbers:
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because
they cannot be divided by any other positive integer except for 1 and their own value.
"""
# Functions: get_primes(1, 10) ou get_primes(100, 200) ...

import math

def get_primes(start: int, end: int) -> list:
    """Retorna uma lista de números primos dentro do intervalo [start, end]."""
    primes = []
    for num in range(start, end + 1):
        if num > 1:  # 0 e 1 não são primos
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes


# Exemplo de uso
print("Primos entre 1 e 10:", get_primes(1, 10))
print("Primos entre 50 e 100:", get_primes(50, 100))
print("Primos entre 50 e 100:", get_primes(100, 150))

