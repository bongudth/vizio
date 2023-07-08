# Formula based Python3
# program to find sum
# of alldivisors of n.
import math

# Returns sum of all
# factors of n.


def sum_of_factors(n):
    # If n is odd, then
    # there are no even
    # factors.
    if n % 2 != 0:
        return 0

    # Traversing through
    # all prime factors.
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1):
        # While i divides n
        # print i and divide n
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count = count + 1

            n = n // i

            # here we remove the
            # 2^0 that is 1. All
            # other factors
            if i == 2 and count == 1:
                curr_sum = 0

            curr_term = curr_term * i
            curr_sum = curr_sum + curr_term

        res = res * curr_sum

    # This condition is to
    # handle the case when
    # n is a prime number.
    if n >= 2:
        res = res * (1 + n)

    return res
