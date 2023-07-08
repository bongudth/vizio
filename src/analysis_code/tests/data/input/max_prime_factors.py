# Python3 code to find largest prime
# factor of number
import math

# A function to find largest prime factor


def max_prime_factors(n):
    # Initialize the maximum prime factor
    # variable with the lowest one
    max_prime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        max_prime = 2
        n >>= 1  # equivalent to n /= 2

    # n must be odd at this point,
    # thus skip the even numbers and
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n / i

    # This condition is to handle the
    # case when n is a prime number
    # greater than 2
    if n > 2:
        max_prime = n

    return int(max_prime)
