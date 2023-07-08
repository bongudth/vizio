# Python program to find sum of given
# series.


def product_prime_factors(n):
    product = 1

    for i in range(2, n + 1):
        if n % i == 0:
            is_prime = 1

            for j in range(2, int(i / 2 + 1)):
                if i % j == 0:
                    is_prime = 0
                    break

            # condition if \'i\' is Prime number
            # as well as factor of num
            if is_prime:
                product = product * i

    return product
