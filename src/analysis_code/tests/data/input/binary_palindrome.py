# Function to check if binary representation of
# a number is palindrome or not


def binary_palindrome(num):
    # convert number into binary
    binary = bin(num)

    # skip first two characters of string
    # because bin function appends '0b' as
    # prefix in binary representation of
    # a number
    binary = binary[2:]

    # now reverse binary string and compare
    # it with original
    return binary == binary[-1::-1]
