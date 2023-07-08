# Python program to print all Primes Smaller
# than or equal to N using Sieve of Eratosthenes


def sieve_of_eratosthenes(num):
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while p * p <= num:
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] == True:
            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            print(p)
