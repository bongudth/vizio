# Python program to find minimum
# sum of product of number


# To find minimum sum of
# product of number
def find_min_sum(num):
    sum = 0

    # Find factors of number
    # and add to the sum
    i = 2
    while i * i <= num:
        while num % i == 0:
            sum += i
            num //= i
        i += 1
    sum += num

    # Return sum of numbers
    # having minimum product
    return sum
